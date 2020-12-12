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
    return 'Hello, World!'

@app.route('/rest',methods=['GET', 'POST'])
def rest():
    filtr={'Username': 'admin'}
    online_users = mongo.db.players.find(filtr)
    i=[]
    l=[doc for doc in online_users]
    return json.dumps(l,default=str)

@app.route('/api/login',methods=['POST'])
def api_login():
    json_data = request.form
    username=json_data['username']
    passowrd = json_data['password']
    filtr = {'username':username,'password':passowrd}
    online_users = mongo.db.players.find(filtr)
    l=[doc for doc in online_users]
    if not l:
        return json.dumps({'Data':'None'})
    res = make_response("Setting a cookie")
    print(l)
    res.set_cookie('userName', str(l[0]['_id']),max_age=60*60*24*365*2)
    return res

@app.route('/api/register',methods=['POST'])
def api_register():
    json_data = request.form
    username = json_data['username']
    passowrd = json_data['password']
    email=json_data['email']
    filtr={'username':username,'password':passowrd,'email':email}
    try:
        online_users = mongo.db.players.insert_one(filtr)
    except:
        return 'Inset Failed'
    return 'Inset Successful'

if __name__ == "__main__":
    app.run(host='0.0.0.0')