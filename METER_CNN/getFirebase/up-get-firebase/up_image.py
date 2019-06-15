from google.cloud import storage
import pyrebase
import os
import urllib.request 
import requests
import datetime
import random


def readFile():
    mypath = 'img_for_upload/'
    for img in os.listdir(mypath):
        print(img)
        upimage(str(datetime.datetime.now()), str(random.randint(0, 9)), img)
    print(">>>>>>>>>>>>>>> finish <<<<<<<<<<<<<<<")


def internet_on():
    try:
        urllib.request.urlopen("http://www.google.com/")
        readFile()

    except urllib.error.URLError as err:
        print("Please check your internet.")


def upimage(date, rfid, image):
    config = {
        "apiKey": "AIzaSyB_jnpsPaxKs3xEhs-AbknZJXjcK-M4IeU",
        "authDomain": "water-meter-235712.firebaseapp.com",
        "databaseURL": "https://water-meter-235712.firebaseio.com",
        "projectId": "water-meter-235712",
        "storageBucket": "water-meter-235712.appspot.com",
        "messagingSenderId": "67042893322"   
    }

    filename = 'img_for_upload/'+image

    credential_path = "firebase-adminsdk-ebgws-8362ef71ab.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

    # ที่อยู่ bucket
    client = storage.Client()
    bucket = client.get_bucket('water-meter-235712.appspot.com')

    # อัพไฟล์ storage
    # pathรูปบนfirebase
    blob = bucket.blob('image/'+image)
    with open(filename, "rb") as fp:
        blob.upload_from_file(fp)

    # อัพไฟล์ database
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    # โหลดรูป
    # blob.public_url คือpathรูปบนfirebase
    image_storage = requests.get(blob.public_url)
    # ชื่อpath folderที่จะเซฟรูป
    with open('img_for_ocr/'+image, 'wb') as f:
        f.write(image_storage.content)

    db.child("room").push({
        "image": {
            "rfid": rfid,
            "url": blob.public_url,
            "date": date}})
    # open("nwdata.txt", 'w').close()

if __name__ == "__main__":
    internet_on()
