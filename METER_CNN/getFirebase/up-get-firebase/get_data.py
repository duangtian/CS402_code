import pyrebase
from google.cloud import storage
import pyrebase
import os
import urllib.request 
import requests
import json

config = { #confic for firebase
    "apiKey": "AIzaSyB_jnpsPaxKs3xEhs-AbknZJXjcK-M4IeU",
    "authDomain": "water-meter-235712.firebaseapp.com",
    "databaseURL": "https://water-meter-235712.firebaseio.com",
    "projectId": "water-meter-235712",
    "storageBucket": "water-meter-235712.appspot.com",
    "messagingSenderId": "67042893322"   
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
alldata = db.child("room").get()

data_fiba = []

urlpic = {
    'key': "", 
    'val': {}
    }


for data in alldata.each():
    urx = urlpic.copy()
    urx['key'] = data.key()
    urx['val'] = data.val()
    data_fiba.append(urx)

with open('datalist.json') as data_file:    
    old_list = json.load(data_file) 

#check old dada more than new data in firebase
if len(old_list) >= len(data_fiba):
    print("case A")
    for i in range(len(data_fiba)-1):
        image_storage = requests.get(data_fiba[i]['val']['image']['url'])
        image_name = data_fiba[i]['val']['image']['rfid']
        print(data_fiba[i]['val']['image']['url'])
        # print(image_storage)
        with open('img_for_ocr/'+image_name+'.jpg', 'wb') as f:
            f.write(image_storage.content)
else: #check new dada more than old data in firebase
    print("case B")
    for i in range(len(old_list), len(data_fiba)):
        image_storage = requests.get(data_fiba[i]['val']['image']['url'])
        image_name = data_fiba[i]['val']['image']['rfid']
        print(data_fiba[i]['val']['image']['url'])
        # print(image_storage)
        with open('img_for_ocr/'+image_name+'.jpg', 'wb') as f:
            f.write(image_storage.content)

with open('datalist.json', 'w') as json_file:  
    json.dump(data_fiba, json_file)

print("finish")

   
