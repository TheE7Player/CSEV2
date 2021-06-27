"""
config.py ~ Holds the variables and constants
"""
from datetime import datetime, timedelta
from .languages import GetSupportedList, IfValidSupport, DEFAULT_LANGUAGE, GetLanguage
from .reg import get_reg, set_reg
import requests

# Constant variables (In Uppercaps)
VERSION = '0.5'
APPLICATION_LOADED = False
WIDTH = 1280
HEIGHT = 720
LATESTVERSION = None

FORCEUPDATE = False

events = []
eventNames = []

language = {}
selectLanguage = GetSupportedList()

updateCheck = get_reg("updateCheck")
needsUpdating = get_reg("needsUpdate")

def VersionComparer(version) -> bool:
    current = VERSION.split('.')
    latest = version.split('.')

    if len(latest) > len(current) or len(latest) < len(current): return True

    i = range(len(current))
    for idx in i:
      if not latest[idx] == current[idx]: return False

    return True

def DoUpdate():

  global needsUpdating, updateCheck, set_reg, get_reg, DEFAULT_LANGUAGE, language, events, eventNames, LATESTVERSION, FORCEUPDATE

  if needsUpdating == None:
    if not set_reg("needsUpdate", "0"):
      needsUpdating = False
  elif needsUpdating == "1" or needsUpdating == "0":
      needsUpdating = True if needsUpdating == "1" else False

  if updateCheck == None:
    if not set_reg("updateCheck", "0"):
      updateCheck = False
  elif updateCheck == "1" or updateCheck == "0":
      updateCheck = True if updateCheck == "1" else False

  if updateCheck == None:
    if not set_reg("updateCheck", "0"):
      updateCheck = False
  elif updateCheck == "1" or updateCheck == "0":
      updateCheck = True if updateCheck == "1" else False

  nextCheck = datetime.now()
  nextCheck = f"{nextCheck.day}/{nextCheck.hour}"

  timeCheck = get_reg("timeNextCheck")

  # Check if language has been set (if any) - Default to english (ENG)

  targetLanguage = get_reg("defaultLanguage")

  if targetLanguage == None:
    set_reg("defaultLanguage", DEFAULT_LANGUAGE)
    print("Setting default language key to ENGLISH")
  else:
    if not targetLanguage == DEFAULT_LANGUAGE:
      print("DEFAULT LANUAGE IS CHANGED TO: ", targetLanguage)

      if not IfValidSupport(targetLanguage):
        print("[!] LANGUAGE", targetLanguage, "isn't supported or spelt wrong! Defaulting into English [!]")
      else:
        DEFAULT_LANGUAGE = targetLanguage

  if not updateCheck or timeCheck == None or timeCheck == nextCheck or needsUpdating or FORCEUPDATE:
    print("Now Performing URL fetch")

    if FORCEUPDATE:
      print("FORCE UPDATE IS TURNED ON")

    if get_reg("needsUpdate") == "1":
      if not set_reg("needsUpdate", "0"): print("Failed to set REVKEY 'needsUpdate' to false")

    try:
      url = "https://raw.githubusercontent.com/TheE7Player/CSEV2/main/version.txt"
      r = requests.get(url, timeout=5)

      r = r.content.decode("utf-8")
      LATESTVERSION = r
      result = VersionComparer(r)

      needsUpdating = not result

      if not set_reg("updateCheck", "1"): print("Failed to set REVKEY 'updateCheck' to true")

      if needsUpdating:
        if not set_reg("needsUpdate", "1"): print("Failed to set REVKEY 'needsUpdate' to true")

      nextCheck = datetime.now() + timedelta(hours=1)
      nextCheck = f"{nextCheck.day}/{nextCheck.hour}"
      if not set_reg("timeNextCheck", nextCheck): print(f"Failed to set REVKEY 'timeNextCheck' to {nextCheck}")

    except (requests.ConnectionError, requests.Timeout):
      print("No internet connection.")
  else:
    print("Update check has already been made - ignoring the update logic")

  print("Parsing events.yaml now")

  import yaml, os, sys

  eventPath = 'events.yaml'

  if not os.path.isfile(eventPath):
    print("[WARNING] Noticed you didnt run it from a suitable location - thats okay, I'll fix it (I hope)")
    
    # Grab the path location and check on it
    currentPath = sys.argv[0].split('\\')
    
    # Then we flip the list around so the script is the first element
    currentPath.reverse()

    print(currentPath)

    # Then we modify that element and get rid of the '/' and script name ( if any )

    if '/' in currentPath[0]:
      currentPath[0] = currentPath[0][:currentPath[0].index('/')]
    else:
      currentPath.pop(0)

    # Flip again to get the correct pathing
    currentPath.reverse()

    # We finally now have our correct path to look for - lets join it up then free the list from memory
    newpath = '\\'.join(currentPath)
    eventPath = f"{newpath}\\{eventPath}"


  with open(eventPath) as f:
      events = yaml.load(f, Loader=yaml.FullLoader)
      eventNames = list(events.keys())
      eventNames.sort()

  language = GetLanguage(DEFAULT_LANGUAGE)