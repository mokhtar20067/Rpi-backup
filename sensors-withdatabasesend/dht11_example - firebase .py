import RPi.GPIO as GPIO
import dht11
import time

import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import db

cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred,{
'databaseURL' : "https://raspberrypi-11104-default-rtdb.firebaseio.com/"
})
ref = db.reference('dht11-readings')

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()

# read data using Pin GPIO21 
instance = dht11.DHT11(pin=21)

while True:
    result = instance.read()
    if result.is_valid():
        print("Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity)
        ref . push({
    "dh11_value":"Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity
    })
        time.sleep(1)