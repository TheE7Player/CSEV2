# Python 3.7.9

from flask import Flask, render_template, Markup, request, make_response
from flaskwebgui import FlaskUI #get the FlaskUI class
from datetime import datetime, timezone, timedelta

from languages import GetLanguage, IfValidSupport, GetSupportedList

# For URL request to fetch the url containing the current version
import requests

# For getting or setting keys on Windows OS Kernal
import winreg

app = Flask(__name__, template_folder='static')

# Constant variables (In Uppercaps)
VERSION = '0.3'
REG_PATH = r"SOFTWARE\CSEV2\DATA"
DEFAULT_LANGUAGE = "ENG"
APPLICATION_LOADED = False

# Feed it the flask app instance 
ui = FlaskUI(app)

ui.height = 720
ui.width = 1280
ui.app_mode = True

events = []
eventNames = []

language = []
selectLanguage = GetSupportedList()



# https://stackoverflow.com/a/23624136
def set_reg(name, value):
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
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_READ)
        value, _ = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None

def CreateTable(data):

  table = []
  paramNum = 1

  if len(data) == 0:
    table.append(f"<h1 class=\"title\">{language['NoArgumentsTitle']}</h1>")
    table.append(f"<br><p>{language['NoArgumentsText']}</p>")
  else: 

    table.append('<table class="table" style="width=inherit;">')

    table.append(f'<thead><tr><td>{language["ArgumentID"]}</td><td>{language["ArgumentName"]}</td><td>{language["ArgumentType"]}</td><td>{language["ArgumentComment"]}</td></tr></thead>')

    table.append('<tbody>')

    table.append('<tr>')

    for eachEvent in data:
      table.append(f'<td>{paramNum}</td>')
      for eachAttr in eachEvent:
        table.append(f'<td>{eachAttr}</td>')
      paramNum+=1
      table.append('</tr>')
    
    table.append('</tbody></table>')
  
  return Markup("".join(table))

# do your logic as usual in Flask
@app.route('/event/<string:item_name>')
def event(item_name):
  print("event on: " + item_name)

  target = events[item_name]

  cli = True if "gameevents" in target['type'] else False
  mod = True if "modevents" in target['type'] else False
  svr = True if "serverevents" in target['type'] else False

  onlyOneEvent = False if "," in target['type'] else True

  if not target == None:
    print("Successful! Found meta data on that event")

  tableResponce = {}

  if cli == False and mod == False and svr == False:
    tableResponce = None
  else:
    if cli:
        tableResponce['c'] = CreateTable(target['attributes' if onlyOneEvent else 'attributes_g'])

    if mod:
        tableResponce['g'] = CreateTable(target['attributes' if onlyOneEvent else 'attributes_m'])

    if svr:
        tableResponce['s'] = CreateTable(target['attributes' if onlyOneEvent else 'attributes_s'])

  return render_template('index.html', 
  version=VERSION, lang=language, availableLanguages=selectLanguage,
  eventnames=eventNames, 
  eventTitle=item_name,
  supportsGame=mod, supportsClient=cli, supportsServer=svr, table=tableResponce)

@app.route("/")
def index():
  global APPLICATION_LOADED

  if not APPLICATION_LOADED:
    APPLICATION_LOADED = True

  return render_template('index.html', 
  version=VERSION, lang=language, availableLanguages=selectLanguage,
  eventnames=eventNames, 
  eventTitle=language['NoEvent'],
  supportsGame=False, supportsClient=False, supportsServer=False,
  askUpdate=needsUpdating)

@app.route("/change/<string:lang>/<int:toChange>/")
def change(lang, toChange):
  global language
  
  print("Attempting to change to shorthand language: ", lang)

  returnLanguage = None

  if toChange == 1:
    print("pretend to change lang")

    language = GetLanguage(lang)
    if not set_reg("defaultLanguage", lang):
      print("Failed to store as new language")

    return render_template('index.html', 
    version=VERSION, lang=language, availableLanguages=selectLanguage,
    eventnames=eventNames, 
    eventTitle=language['NoEvent'],
    supportsGame=False, supportsClient=False, supportsServer=False,
    askUpdate=needsUpdating)

  if IfValidSupport(lang):
    returnLanguage = GetLanguage(lang)
  else:

    print("[?] Language lookup failed - now attempt to recover if possible [?]")

    try:
      supportList =  GetSupportedList()

      for l in supportList.keys():
        if l[:3].upper() == lang:
          returnLanguage = GetLanguage(supportList[l])
          break

      if returnLanguage == None:
        raise Exception()

    except:
      print("[!] FAILED TO SUPPORT SELECTED LANGUAGE - DISPLAYING ERROR PAGE INSTEAD [!]")
    

  return render_template('change.html', normalLang=language, lang=returnLanguage)

def VersionComparer(version):
  current = VERSION.split('.')
  latest = version.split('.')

  if len(latest) > len(current) or len(latest) < len(current): return True

  i = range(len(current))
  for idx in i:
    if not latest[idx] == current[idx]: return False

  return True

# call the 'run' method
print("PRESS CTRL+SHIFT+R IF CONTENT DOESN'T LOAD AFTER BUILD")

print("checking for updates if possible")

updateCheck = get_reg("updateCheck")
needsUpdating = get_reg("needsUpdate")

def main():
  global needsUpdating, updateCheck, events, eventNames, language, DEFAULT_LANGUAGE
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

  if not updateCheck or timeCheck == None or timeCheck == nextCheck or needsUpdating == True:
    print("Now Performing URL fetch")

    if get_reg("needsUpdate") == "1":
      if not set_reg("needsUpdate", "0"): print("Failed to set REVKEY 'needsUpdate' to false")

    try:
      url = "https://raw.githubusercontent.com/TheE7Player/CSEV2/main/version.txt"
      r = requests.get(url, timeout=5)

      r = r.content.decode("utf-8")

      needsUpdating = not VersionComparer(r)

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

  import yaml
  with open('events.yaml') as f:
      events = yaml.load(f, Loader=yaml.FullLoader)
      eventNames = list(events.keys())
      eventNames.sort()

  language = GetLanguage(DEFAULT_LANGUAGE)
  
  ui.run()
  
import psutil # Used to cycle through the processes
import threading # Used to create threads (IMPORTANT)
import time # Used along side of events (Allows the thread sleep)
import os
import signal # Used to exit the script completly

def SearchThread():
  global APPLICATION_LOADED

  foundChrome = False
  chromeID = 0

  windowOpen = True

  target = "chrome"
  argu = "--incognito"

  while not APPLICATION_LOADED:
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


# Creating an Entry Point here
if __name__ == '__main__':

    uiThread = threading.Thread(target=main)
    uiThread.daemon = True  
    uiThread.start()

    searchThread = threading.Thread(target=SearchThread)
    searchThread.daemon = True  
    searchThread.start()

    searchThread.join()

print("EXITING")
os.kill(os.getpid(), signal.SIGTERM)