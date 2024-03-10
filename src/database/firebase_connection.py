import firebase_admin
from firebase_admin import credentials,firestore

def initialize_firestore():
    cred = credentials.Certificate(r"C:\Users\Johan Ivan\Documents/firebaseKey.json")
    firebase_admin.initialize_app(cred)

    return firestore.client()

db = initialize_firestore()