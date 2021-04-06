import RPi.GPIO as GPIO
import dht11
import time

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()

# read data using Pin GPIO21 
instance = dht11.DHT11(pin=21)
def final_result() :

    while True:
        result = instance.read()
        if result.is_valid():
            print("Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity)
            final_result2="Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity
            return final_result2
        time.sleep(1)
    
final_result()  
