"""
createEventTable.py ~ Creates the table for the selected event
"""
from flask import Markup
import utils.config as cfg

def CreateTable(data):

  table = []
  paramNum = 1

  if len(data) == 0:
    table.append(f"<h1 class=\"title\">{cfg.language['NoArgumentsTitle']}</h1>")
    table.append(f"<br><p>{cfg.language['NoArgumentsText']}</p>")
  else: 

    table.append('<table class="table" style="width=inherit;">')

    table.append(f'<thead><tr><td>{cfg.language["ArgumentID"]}</td><td>{cfg.language["ArgumentName"]}</td><td>{cfg.language["ArgumentType"]}</td><td>{cfg.language["ArgumentComment"]}</td></tr></thead>')

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