from flask import Flask, jsonify, render_template, request
import json


app = Flask(__name__)
jData = json.loads(open('./games.json').read())
data=jData["Games"]

# Intial request Ex: http://192.168.99.100:5000/
@app.route('/')
def route_main():
    return "Welcome to the world of Games."

# Returns JSON which containes all games
@app.route('/getgames/')
def games_all():
    return render_template("index.html",items=data)

# Returns games JSON which matches the id
@app.route('/getgames/<string:id>/')
def games_id(id=''):
    myList=[]
    for element in data:
        if element["id"] == id:
            myList.append(element)
    return render_template("index.html",items=myList)

# Returns the games JSON with particualr game type
@app.route('/getgames/type/<string:type>/')
def games_type(type=''):
    myList=[]
    for element in data:
        if element["type"].lower() == type.lower():
            myList.append(element)
    return render_template("index.html",items=myList)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
