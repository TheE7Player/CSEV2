# Python 3.7.9

# https://stackoverflow.com/a/60441931

from flask import Flask, render_template
from flaskwebgui import FlaskUI #get the FlaskUI class
import utils.config as cfg
import sys

app = Flask(__name__, template_folder='static')

# Disable the logger (faster)
app.logger.disabled = True

ui = None

cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None

# call the 'run' method
print("PRESS CTRL+SHIFT+R IF CONTENT DOESN'T LOAD AFTER BUILD")

print("checking for updates if possible")

def main():
  ui.run()

@app.route('/event/<string:item_name>')
def event(item_name):
  print("event on: " + item_name)

  target = cfg.events[item_name]

  cli = True if "gameevents" in target['type'] else False
  mod = True if "modevents" in target['type'] else False
  svr = True if "serverevents" in target['type'] else False

  onlyOneEvent = False if "," in target['type'] else True

  if not target == None:
    print("Successful! Found meta data on that event")

  tableResponce = {}

  import utils.createEventTable as ct

  if cli == False and mod == False and svr == False:
    tableResponce = None
  else:
    if cli:
        tableResponce['c'] = ct.CreateTable(target['attributes' if onlyOneEvent else 'attributes_g'])

    if mod:
        tableResponce['g'] = ct.CreateTable(target['attributes' if onlyOneEvent else 'attributes_m'])

    if svr:
        tableResponce['s'] = ct.CreateTable(target['attributes' if onlyOneEvent else 'attributes_s'])

  return render_template('index.html', 
  version=cfg.VERSION, lang=cfg.language, availableLanguages=cfg.selectLanguage,
  eventnames=cfg.eventNames, 
  eventTitle=item_name,
  supportsGame=mod, supportsClient=cli, supportsServer=svr, table=tableResponce)

@app.route("/")
def index():
  if not cfg.APPLICATION_LOADED:
    cfg.APPLICATION_LOADED = True

  return render_template('index.html', 
  version=cfg.VERSION, lang=cfg.language, availableLanguages=cfg.selectLanguage,
  eventnames=cfg.eventNames, 
  eventTitle=cfg.language['NoEvent'],
  supportsGame=False, supportsClient=False, supportsServer=False,
  askUpdate=cfg.needsUpdating, updateVersion=cfg.LATESTVERSION)

@app.route("/change/<string:lang>/<int:toChange>/")
def change(lang, toChange):

  print("Attempting to change to shorthand language: ", lang)

  returnLanguage = None
  import utils.languages as l
  import utils.reg as r

  if toChange == 1:
    print("Now attempting to change language")

    cfg.language = l.GetLanguage(lang)
    if not r.set_reg("defaultLanguage", lang):
      print("Failed to store as new language")

    return render_template('index.html', 
    version=cfg.VERSION, lang=cfg.language, availableLanguages=cfg.selectLanguage,
    eventnames=cfg.eventNames, 
    eventTitle=cfg.language['NoEvent'],
    supportsGame=False, supportsClient=False, supportsServer=False,
    askUpdate=cfg.needsUpdating, updateVersion=cfg.LATESTVERSION)

  if l.IfValidSupport(lang):
    returnLanguage = l.GetLanguage(lang)
  else:

    print("[?] Language lookup failed - now attempt to recover if possible [?]")

    try:
      supportList = l.GetSupportedList()

      for lg in supportList.keys():
        if lg[:3].upper() == lang:
          returnLanguage = l.GetLanguage(supportList[lg])
          break

      if returnLanguage == None:
        raise Exception(f"Unable to find support for: {lang}")

    except Exception as e:
      print("[!] FAILED TO SUPPORT SELECTED LANGUAGE - DISPLAYING ERROR PAGE INSTEAD [!]","\n",e)
    

  return render_template('change.html', normalLang=cfg.language, lang=returnLanguage)

# Creating an Entry Point here
if __name__ == '__main__':
  import utils.thread as thrd

  cfg.DoUpdate()

  ui = FlaskUI(app)

  ui.height = cfg.HEIGHT
  ui.width = cfg.WIDTH
  ui.app_mode = True
  
  # Now lets boot the application
  thrd.StartApplication(main)