from flask import Flask,render_template,request,redirect,url_for
from flask_cors import CORS
import os
import urllib.request
import urllib.parse
import json
import requests
import pandas as pd

webroot = 'src'
static_dir = os.path.join(webroot,'static')
template_dir = os.path.join(webroot,'templates')

app=Flask(__name__,template_folder=template_dir,static_folder=static_dir)

url = 'http://localhost:8082'
user = { 'email' : 'admin', 'password' : 'admin' }
# logging.basicConfig(filename="log_files.logs",format='%(asctime)s %(clientip)-15s %(user)-8s %(message)s',level=logging.INFO)

def login():
    request = urllib.request.Request(url + '/api/session')
    response = urllib.request.urlopen(request, urllib.parse.urlencode(user).encode("utf-8"))
    return response.headers.get('Set-Cookie')

login_credentials=login()  

login_credentials=login()
def get_data():
    request = urllib.request.Request(url + '/api/devices')
    request.add_header('Cookie', login_credentials)
    response = urllib.request.urlopen(request)
    data = json.load(response)
    return data

data=get_data()

with open("Server_Data.json","w") as write_data:
    json.dump(data,write_data)

json_data = [] 

with open('Server_Data.json',"r") as read_data:
   json_data = json.load(read_data)

id_=[]
name=[]
uniqueId=[]

for item in json_data:
    name.append((item["name"]))
    uniqueId.append((item["uniqueId"]))
    id_.append((item["id"]))

id_=tuple(id_)
name=tuple(name)
uniqueId=tuple(uniqueId)

results=zip(id_,name,uniqueId)
data=[]
for x in results:
    data.append(x)

# print(data)

headers=("#","ID","Device Name","IMEI")

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("tables.html",headers=headers,data=data)

if __name__=="__main__":
    app.run(debug=True,port=5000)