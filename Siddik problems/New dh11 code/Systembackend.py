import datetime
import Emailsending
import dh11_instance_result
import dht11


# print(dir(datetime.datetime))


class start_cycle:
    def __init__(self):

        # setting the start date and time of the cycle
        self.startTime = datetime.datetime.now()

    def get_startTime(self):  # getting startTime and sending an Email of it
        Emailsending.sender.sendmail(
            "mado10398@gmail.com", "Cycle Start Date and Time", f"Cycle Start Date & Time is {self.startTime}")
        return self.startTime

    # def getDH11_Value(self): #seting dh11 sensor values
    #     dh11_instance_result.dh11_instance_result_method()
    #     dh11read = dh11_instance_result.instance.read()
    #     temp = dh11read.temperature
    #     humid = dh11read.humidity
    #     return temp, humid
    

    def check_dh11_optimal_values(self):
        dh11_instance_result.dh11_instance_result_method()
        dh11read = dh11_instance_result.instance.read()
        temp = dh11read.temperature
        humid = dh11read.humidity
        if 30 > temp > 23:
            print("Temperature is optimal for farming")
        else: print("Temperature is \"not\" optimal for farming")
        if 50 > humid > 70:
            print("humidity is optimal for farming")
        else: print("humidity is \"not\" optimal for farming")


stageOne = start_cycle()  # creating a farming cycle

stageOne.get_startTime()
stageOne.check_dh11_optimal_values()