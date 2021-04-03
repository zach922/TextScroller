import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")
            return False

cred = credentials.Certificate("/home/zach/code/TextScroll/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

cont = True
contStr = ''
while(cont):
    date = input("Enter a date (ex. YYYY-MM-DD): ")

    if(validate(date)):
        date = str(datetime.datetime.strptime(date, '%Y-%m-%d'))[:10]

        msg = input("Enter the message: ")

        data = {"message" : msg}

        db.collection("messages").document(date).set(data)

        print("Message for %s set. Thank you!" % {date})
        contStr = input("Would you like to continue? Y/n?")

        if (upper(contStr) != 'Y'):
            cont = False