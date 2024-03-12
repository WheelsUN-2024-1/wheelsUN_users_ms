from fastapi import APIRouter, Path
from src.models.user_model import UserCreate, UserPatch, UserPut
from src.database.firestore_crud import getAll, getByParameter, create, patch, delete

passenger_router = APIRouter()

passengerCollection = "passengerCollection"

@passenger_router.get("/")
async def getPassengers():
    doc_getAll = getAll(passengerCollection)
    users=[]
    for doc in doc_getAll:
        users.append(doc.to_dict())
    return users

@passenger_router.get("/{id}")
async def getPassengerById(id:int):
    docs = getByParameter(passengerCollection, "userIdNumber", id)
    for doc in docs:
        return doc.to_dict()
    return "PASSENGER_NOT_FOUND"

@passenger_router.post("/")
async def createPassenger(user: UserCreate):
    docs = getByParameter(passengerCollection, "userIdNumber", user.userIdNumber)
    for doc in docs: #this verifies if there is a vehicle
        return "ALREADY_PASSENGER"
    create(passengerCollection, user)
    return await getPassengerById(user.userIdNumber)

@passenger_router.patch("/{id}")
async def patchPassenger(id: int, user: UserPatch):
    patch(passengerCollection, "userIdNumber", id, user)
    return await getPassengerById(id)

@passenger_router.put("/{id}")
async def patchPassenger(id: int, user: UserPut):
    patch(passengerCollection, "userIdNumber", id, user)
    return await getPassengerById(id)

@passenger_router.delete("/{id}")
async def deletePassenger(id: int):
    return "PASSENGER_" + delete(passengerCollection, "userIdNumber", id)