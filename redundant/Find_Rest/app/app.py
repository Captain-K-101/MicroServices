from flask import Flask,request,send_file,make_response
from flask_pymongo import PyMongo
from flask import jsonify
import json
import random
import string

app= Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://root:toor@cloudproj.xgny0.mongodb.net/ctf?retryWrites=true&w=majority"
mongo = PyMongo(app)


@app.route('/')
def hello_world():
    return 'Welcome to the advanced Search Api'

@app.route('/rest',methods=['GET', 'POST'])
def rest():
    filtr={'Username': 'admin'}
    online_users = mongo.db.players.find(filtr)
    l=[doc for doc in online_users]
    return json.dumps(l,default=str)

@app.route('/api/Resturants/<variable>',methods=['GET'])
def api_rest(variable):
    if not request.cookies.get('userName'):
        return 'Login First'
    filtr = {'name':{"$regex" : "^"+str(variable)+".*","$options" :'i'}}
    online_users = mongo.db.Restaurant.find(filtr)
    l=[doc for doc in online_users]
    if not l:
        return json.dumps({'name':'found','Rating':''})
    return json.dumps(l,default=str)

if __name__ == "__main__":
    app.run(host='0.0.0.0')