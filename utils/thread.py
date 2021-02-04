import psutil # Used to cycle through the processes
import threading # Used to create threads (IMPORTANT)
import time # Used along side of events (Allows the thread sleep)
import os
import signal # Used to exit the script completly

import utils.config as cfg

chromeID = 0

def StartWindowCheck():

  foundChrome = False

  windowOpen = True

  target = "chrome"
  argu = "--incognito"

  while not cfg.APPLICATION_LOADED:
    time.sleep(2)

  print("Waiting thread is now searching...")
  while True:
    if not foundChrome:
      for process in psutil.process_iter():
          if target in process.name():         
            if argu in process.cmdline():
              print("Found the window to test for:", process.pid)
              foundChrome = True
              chromeID = process.pid
    else:
      windowOpen = False
      for process in psutil.process_iter():
          if target in process.name():         
            if argu in process.cmdline():
              windowOpen = True

      if not windowOpen:
        print("Cannot find window - assuming its closed. Shuting down server.")
        break
    time.sleep(2)

def StartApplication(FlaskAppFunc):
    uiThread = threading.Thread(target=FlaskAppFunc)
    uiThread.daemon = True  
    uiThread.start()

    searchThread = threading.Thread(target=StartWindowCheck)
    searchThread.daemon = True  
    searchThread.start()

    searchThread.join()

    print("EXITING")
    os.kill(os.getpid(), signal.SIGTERM)
