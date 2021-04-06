import datetime
import Emailsending
import dh11_check_optimal_condition
import dht11
import moisture_check_optimal_condition

# print(dir(datetime.datetime))

#checks farming conditions
class start_cycle:
    def __init__(self):

        # setting the start date and time of the cycle
        self.startTime = datetime.datetime.now()

#     def get_startTime(self):  # getting startTime and sending an Email of it
#         return self.startTime

    def check_dh11_optimal_values(self): #checks optimal values for temp and humid
        self.TEMP = dh11_check_optimal_condition.DH11_opject.temp
        self.HUMID = dh11_check_optimal_condition.DH11_opject.humid
        self.dh11_MSG = dh11_check_optimal_condition.DH11_opject.M
        print(self.dh11_MSG)
        if  self.TEMP > 23 and self.TEMP <30:
                self.T = "Temperature is optimal for farming \n"
                self.TFlag = 1
        else: 
                self.T = "Temperature is \"not\" optimal for farming \n"
                self.TFlag = 0
        print(self.T)
        print(f"Temp Flag = {self.TFlag} \n")
        if self.HUMID>65 and self.HUMID<85:
                self.H = "humidity is optimal for farming \n"
                self.HFlag = 1
        else:
                self.H ="humidity is \"not\" optimal for farming \n"
                self.HFlag = 0
        print(self.H)
        print(f"Humid Flag = {self.HFlag} \n")
        
    def check_moisture_optimal_values(self): #checks optimal values for moisture
        self.M_value = moisture_check_optimal_condition.moisture_opject.moisture_value
        self.M_MSG = moisture_check_optimal_condition.moisture_opject.M_value_msg
        print(self.M_MSG )
        if self.M_value > 20 and self.M_value < 30:
            self.M = "Moisture is optimal for Stage One \n"
            self.MFlag = 1
        else: 
            self.M = "Moisture is \"Not\" optimal for Stage One \n"
            self.MFlag = 0
        print(self.M)
        print(f"Moisture Flag = {self.MFlag} \n")

    def Email_Sending(self): #Sending Emails
        Emailsending.sender.sendmail(
            "mado10398@gmail.com", "Cycle Start Data And Conditions", f"""Cycle Start Date & Time is {self.startTime} ##### 
            {self.dh11_MSG} #### {self.T} #### {self.H}
            ##### {self.M_MSG}
            
            """)


stageOne = start_cycle()  # creating a farming cycle

# stageOne.get_startTime()
stageOne.check_dh11_optimal_values()
stageOne.check_moisture_optimal_values()

# stageOne.Email_Sending()
