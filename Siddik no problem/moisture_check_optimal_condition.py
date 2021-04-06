import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
 
# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
 
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.CE0)
 
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
 
# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)

# print('Raw ADC Value: ', chan.value)
# print('ADC Voltage: ' + str(chan.voltage) + 'V')

class Moisture_Optimal:

    def Moisture_Check_optimal_condition_method(self):
    
        self.moisture_value = (chan.voltage - 3.28)/-0.0196
        self.M_value_msg = "Moisture = {:.2f} % \n".format(self.moisture_value)

        # print("Moisture = {:.2f} %".format(self.moisture_value))
#         print(self.Mvalue)
#         if self.moisture_value > 20 and self.moisture_value < 30:
#             self.M = "Moisture is optimal for Stage One \n"
#             self.MFlag = 1
#         else: 
#             self.M = "Moisture is \"Not\" optimal for Stage One \n"
#             self.MFlag = 0
#         print(self.M)
#         print(f"Moisture Flag = {self.MFlag} \n")

moisture_opject = Moisture_Optimal()
moisture_opject.Moisture_Check_optimal_condition_method()

