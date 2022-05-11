"""
reg.py - Handles the Windows Registry for storing things
"""
import os
# We now need to import os for OS validation

REG_PATH = r"SOFTWARE\CSEV2\DATA"
NON_WINDOWS = False

# For getting or setting keys on Windows OS Kernal
try:
    import winreg
except ImportError:
    print("NOT RUNNING AS WINDOWS - CONFIGURING FOR NON-WINDOWS")

    # Creating a dummy exception class to avoid lint errors (on linux)
    class WindowsError(Exception):
        pass

    # Setting the property class in the running folder
    REG_PATH = r"./csev_config.yaml"
    NON_WINDOWS = True

    from pathlib import Path
    if not Path(REG_PATH).is_file():
        config = open(REG_PATH, "w")
        config.write(f"# CONFIG FOR CSEV2 - DON'T MODIFY UNLESS NECESSARY!\n")
        config.close()


# https://stackoverflow.com/a/23624136
def set_reg(name, value):
    global NON_WINDOWS

    if NON_WINDOWS:
        import yaml
        cfg = None

        try:
            r = open(REG_PATH, "r")
            cfg = yaml.load( r, Loader=yaml.FullLoader) 
            r.close()

            if cfg == None:
                cfg = {}

            cfg[name] = str(value)

            r = open(REG_PATH, "w")
            r.write(f"# CONFIG FOR CSEV2 - DON'T MODIFY UNLESS NECESSARY!\n")
            for k, v in cfg.items():
                r.write(f"{k}: {v}\n")
            r.close()

        except Exception as e:
            print(f"[NON-WINDOWS] ERROR WRITING FOR KEY {name} WITH VALUE {value}\n{e}")
            return False
    else:
        try:
            winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_WRITE)
            winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)
            winreg.CloseKey(registry_key)
            return True
        except WindowsError:
            return False

# https://stackoverflow.com/a/23624136
def get_reg(name):
    global NON_WINDOWS

    if NON_WINDOWS:
        import yaml
        cfg = None

        try:
            r = open(REG_PATH, "r")
            cfg = yaml.load( r, Loader=yaml.FullLoader) 
            r.close()

            return cfg[name] if name in cfg else None

        except Exception as e:
            print(f"[NON-WINDOWS] ERROR READING FOR KEY {name} FROM CONFIG FILE\n{e}")
            return False
    else:
        try:
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_READ)
            value, _ = winreg.QueryValueEx(registry_key, name)
            winreg.CloseKey(registry_key)
            return value
        except WindowsError:
            return None