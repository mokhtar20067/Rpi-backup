import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import db

cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred,{
'databaseURL' : "https://raspberrypi-11104-default-rtdb.firebaseio.com/"
})
ref = db.reference('moisture-readings')

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
 
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.CE0)
 
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
 
# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)
 

#print('ADC Voltage: ' + str(chan.voltage) + 'V')

moisture_value = (chan.voltage - 3.28)/(-0.0196)

print("Moisture = {:.2f} %".format(moisture_value))
#print(moisture_value)
newmoisture_value = int(moisture_value)
ref . push({
    "moisture_value":str(newmoisture_value)
    
  
})
