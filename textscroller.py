import datetime as dt
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def fetch(db, date):

    try:
        docs = db.collection('messages').document(date).get()
        msg = docs.to_dict()["message"]
        return msg;
    except TypeError: #if a day isn't given
        return "have a good day!"

        
def display(msg):

    print(msg)

    return

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

msg = fetch(db, str(dt.date.today()))
date = str(dt.date.today())

while(True):
    if (date != str(dt.date.today())):
        msg = fetch(db,date)
        date = str(dt.date.today())

    display(msg)


