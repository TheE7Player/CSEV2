# Python 3.7.9
from flask import Flask, render_template, Markup
from flaskwebgui import FlaskUI #get the FlaskUI class

"""
import yaml
with open('items.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
"""

app = Flask(__name__, template_folder='static')

# Feed it the flask app instance 
ui = FlaskUI(app)
ui.height = 720
ui.width = 1280
ui.app_mode = True

events = []
eventNames = []

def AddElement(element_type, element_content):
  return f'<{element_type}>{element_content}</{element_type}>'

def CreateTable(data):

  table = []
  paramNum = 1

  if len(data) == 0:
    table.append("<h1 class=\"title\">This event is just an empty invoker</h1>")
    table.append("<br><p>That means that this event doesn't pass or carry any information - It just invokes the event argumentless.</p>")
  else: 

    table.append('<table class="table" style="width=inherit;">')

    table.append('<thead><tr><td>Param Order</td><td>Param Name</td><td>Param Type</td><td>Param Comment</td></tr></thead>')

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
      tableResponce['c'] = []

      if onlyOneEvent:
        tableResponce['c'] = CreateTable(target['attributes'])

    if mod:
      tableResponce['g'] = []

      if onlyOneEvent:
        tableResponce['g'] = CreateTable(target['attributes'])

    if svr:
      tableResponce['s'] = []

      if onlyOneEvent:
        tableResponce['s'] = CreateTable(target['attributes'])


  #Markup("<p>no</p>")
  return render_template('index.html', 
  version=0.1, 
  eventnames=eventNames, 
  eventTitle=item_name,
  supportsGame=mod, supportsClient=cli, supportsServer=svr, table=tableResponce)

@app.route("/")
def index():
  return render_template('index.html', 
  version=0.1, 
  eventnames=eventNames, 
  eventTitle="No Event Selected",
  supportsGame=False, supportsClient=False, supportsServer=False)

# call the 'run' method
print("PRESS CTRL+SHIFT+R IF CONTENT DOESN'T LOAD AFTER BUILD")

print("Parsing events.yaml now")

import yaml
with open('events.yaml') as f:
    events = yaml.load(f, Loader=yaml.FullLoader)
    eventNames = list(events.keys())
    eventNames.sort()

ui.run()