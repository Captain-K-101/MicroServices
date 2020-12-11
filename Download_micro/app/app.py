from flask import Flask,request,send_file
from flask import jsonify
import json
from pytube import YouTube
import random
from flask_pymongo import PyMongo

app= Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://root:toor@cloudproj.xgny0.mongodb.net/<dbname>?retryWrites=true&w=majority"
mongo = PyMongo(app)



@app.route('/')
def hello_world():
    return 'API EnDPOINT FOR DOWNLOADS'

@app.route('/download/youtube',methods=['POST'])
def download_ytd():
    json_data = request.json
    url=json_data['url']
    link='https://www.youtube.com/watch?v='+url
    try:
        yt = YouTube(link)  
    except:
        print("Connection Error") #to handle exception  
    stream = yt.streams.first()
    filename = yt.streams[0].title+'.mp4'
    stream.download('./uploads/')
    return 'File Has been Downloaded' 

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8081)
