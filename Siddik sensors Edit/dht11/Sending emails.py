import dht11_example
import smtplib
    
    
    
    
#Email Variables
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = 'hfgraduationproject@gmail.com' #change this to match your gmail account
GMAIL_PASSWORD = 'HF1234567!'  #change this to match your gmail password


class Emailer:
    def sendmail(self, recipient, subject, content):
         
        #Create Headers
        headers = ["From: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient,
                   "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)
 
        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()
 
        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
 
        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit
 
sender = Emailer()


sendTo = 'anotheremail@email.com'
emailSubject = "Hello World"
emailContent = "This is a test of my Emailer Class"


#Sends an email to the "sendTo" address with the specified "emailSubject" as the subject and "emailContent" as the email content.
#sender.sendmail("mohameddeveloper98@gmail.com", "sensor data", dht11_example.final_result())
sender.sendmail("mokhtar200678@gmail.com", "sensor data", dht11_example.final_result())
sender.sendmail("newmody_98@hotmail.com", "sensor data", dht11_example.final_result())
sender.sendmail("yossrymonia@gmail.com", "sensor data", dht11_example.final_result())


    