import RPi.GPIO as GPIO
import dht11
import time
import Emailsending

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# GPIO.cleanup()

# read data using Pin GPIO21
instance = dht11.DHT11(pin=21)

class DH11_Optimal:
    
    def dh11_Check_optimal_condition_method(self):

        self.result = instance.read()
        if self.result.is_valid():

            self.temp = self.result.temperature
            self.humid = self.result.humidity
            self.M = f"Temp: {self.result.temperature} C" + ' '+f"Humid: {self.result.humidity}% \n"

#             print(f"Temp: {self.result.temperature} C" + ' '+f"Humid: {self.result.humidity}% \n" )
#             if  self.temp > 23 and self.temp <30:
#                 self.T = "Temperature is optimal for farming \n"
#                 self.TFlag = 1
#             else: 
#                 self.T = "Temperature is \"not\" optimal for farming \n"
#                 self.TFlag = 0
#             print(self.T)
#             print(f"Temp Flag = {self.TFlag} \n")
#             if self.humid>65 and self.humid<85:
#                 self.H = "humidity is optimal for farming \n"
#                 self.HFlag = 1
#             else:
#                 self.H ="humidity is \"not\" optimal for farming \n"
#                 self.HFlag = 0
#             print(self.H)
#             print(f"Humid Flag = {self.HFlag} \n")
            # Emailsending.sender.sendmail( "mado10398@gmail.com", "DH 11", f"{self.M} \n {self.T} \n {self.H}")
        

    # def dh11_optimal_flag(self, flag):
    #     self.dh11_flag = flag
    #     return self.dh11_flag

DH11_opject = DH11_Optimal()
DH11_opject.dh11_Check_optimal_condition_method()

