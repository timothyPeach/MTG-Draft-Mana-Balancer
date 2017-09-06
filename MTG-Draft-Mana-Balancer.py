import math
import numpy as np
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route('/page')
def page():
    return render_template('page.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    '''Gets prediction using the HTML form'''
    if request.method == 'POST':

       inputs = request.form

       colors["blue"] = inputs['blue'][0]
       colors["red"] = inputs['red'][0]
       colors["green"] = inputs['green'][0]
       colors["black"] = inputs['black'][0]
       colors["white"] = inputs['white'][0]
       colors["colorless"] = inputs['colorless'][0]
       #
       out = {}
       colors = ["blue","red","green","black","white","colorless"]
       for i in colors:
           out[i] = 0
       #
       total = 0
       for i in colors.keys():
           total += colors[i]
           #print("total",total)
       for i in out.keys():
           out[i] = float(colors[i])/total
           #print("pre",i,out[i])
       #print(out)
       totalOut = 0
       for i in out.keys():
           if out[i] != 0:
               totalOut += 1
       for i in out.keys():
           if out[i] != 0 and i != "colorless":
               out[i] = int(round((out[i]+(out["colorless"]/2))*mana))
               #print("final",i,out[i])
       #
       label = []
       item = []
       #
       for i in out.keys():
           if i != "colorless" and out[i] != 0:
               label.append(i)
               item.append(out[i])

       results = {}
       for i in range(len(label)):
           results[label[i]] = item[i]
       return jsonify(results)

##def manaBalancer():
##    colors = {}
##    mana = int(raw_input("How many lands are you going to use?  "))
##    colors["blue"] = int(raw_input("How many blue symbols occur in your spells' mana costs?  "))
##    colors["red"] = int(raw_input("How many red symbols?  "))
##    colors["green"] = int(raw_input("How many green symbols?  "))
##    colors["black"] = int(raw_input("How many black symbols?  "))
##    colors["white"] = int(raw_input("How many white symbols?  "))
##    colors["colorless"] = int(raw_input("How much colorless cost?  "))
##    #####
##    out = {}
##    colors = ["blue","red","green","black","white","colorless"]
##    for i in colors:
##        out[i] = 0
##    #####
##    total = 0
##    for i in colors.keys():
##        total += colors[i]
##        #print("total",total)
##    for i in out.keys():
##        out[i] = float(colors[i])/total
##        #print("pre",i,out[i])
##    #print(out)
##    totalOut = 0
##    for i in out.keys():
##        if out[i] != 0:
##            totalOut += 1
##    for i in out.keys():
##        if out[i] != 0 and i != "colorless":
##            out[i] = int(round((out[i]+(out["colorless"]/2))*mana))
##            #print("final",i,out[i])
##    for i in out.keys():
##        if i != "colorless" and out[i] != 0:
##            print(i,out[i])
