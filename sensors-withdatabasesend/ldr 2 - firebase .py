#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import db

cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred,{
'databaseURL' : "https://raspberrypi-11104-default-rtdb.firebaseio.com/"
})
ref = db.reference('LDR - readings')


__author__ = 'Gus (Adapted from Adafruit)'
__license__ = "GPL"
__maintainer__ = "pimylifeup.com"

GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
pin_to_circuit = 13

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

#Catch when script is interupted, cleanup correctly
try:
    # Main loop
    #while True:
        print(rc_time(pin_to_circuit))
        ldrres = str(rc_time(pin_to_circuit))
        ldrres2 = int(rc_time(pin_to_circuit))
        #ref . push({
    #"ldr resistance": ldrres
    #})
        if ldrres2 > 50000 :
            print(" Light is OFF " )
            ref . push({
    "Light State": "OFF"
    })
        else :
            print("Light is ON " )
            ref . push({
    "Light State": "ON"
    })
            
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()