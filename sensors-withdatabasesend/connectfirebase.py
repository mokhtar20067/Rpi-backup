import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import db

cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred,{
'databaseURL' : "https://raspberrypi-11104-default-rtdb.firebaseio.com/"
})
ref = db.reference('/')

ref . push({
    "moisture_value":int(moisture_value)
})
            

    

