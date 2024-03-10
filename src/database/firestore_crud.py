from src.database.firebase_connection import db
from google.cloud.firestore_v1.base_query import FieldFilter

def getAll(collection: str):
    return db.collection(collection).stream()

def getByParameter(collection:str, field:str, parameter:str | int):
    doc_ref = db.collection(collection)
    query = doc_ref.where(filter=FieldFilter(field, "==", parameter))
    return query.stream()

def create(collection:str, model):
    doc_create = db.collection(collection).document()
    doc_create.set(model.model_dump())

def patch(collection: str,field:str, parameter:str, model):
    collection_ref = db.collection(collection)
    query = collection_ref.where(filter=FieldFilter(field, "==", parameter))
    docs = query.stream()
    for doc in docs:
        doc_ref = collection_ref.document(doc.id)
        doc_ref.update(model.model_dump(exclude_none=True))
        return
    
def delete(collection:str, field:str, parameter:str):
    try:
        collection_ref = db.collection(collection)
        query = collection_ref.where(filter=FieldFilter(field, "==", parameter))
        docs = query.stream()

        for doc in docs:
            doc_ref = collection_ref.document(doc.id)
            doc_ref.delete()
            return "SUCCESSFULLY_DELETED"

        return "NOT_FOUND"
    except Exception as e:
        return f"DELETION_ERROR: {str(e)}"
    