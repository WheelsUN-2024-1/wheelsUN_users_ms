from fastapi import APIRouter, Path
from src.models.user_model import UserCreate, UserPatch, UserPut
from src.database.firestore_crud import getAll, getByParameter, create, patch, delete

passanger_router = APIRouter()

passangerCollection = "passangerCollection"

@passanger_router.get("/")
async def getPassangers():
    doc_getAll = getAll(passangerCollection)
    users=[]
    for doc in doc_getAll:
        users.append(doc.to_dict())
    return users

@passanger_router.get("/{id}")
async def getPassangerById(id:int):
    docs = getByParameter(passangerCollection, "userIdNumber", id)
    for doc in docs:
        return doc.to_dict()
    return "PASSANGER_NOT_FOUND"

@passanger_router.post("/")
async def createPassanger(user: UserCreate):
    docs = getByParameter(passangerCollection, "userIdNumber", user.userIdNumber)
    for doc in docs: #this verifies if there is a vehicle
        return "ALREADY_PASSANGER"
    create(passangerCollection, user)
    return await getPassangerById(user.userIdNumber)

@passanger_router.patch("/{id}")
async def patchPassanger(id: int, user: UserPatch):
    patch(passangerCollection, "userIdNumber", id, user)
    return await getPassangerById(id)

@passanger_router.put("/{id}")
async def patchPassanger(id: int, user: UserPut):
    patch(passangerCollection, "userIdNumber", id, user)
    return await getPassangerById(id)

@passanger_router.delete("/{id}")
async def deletePassanger(id: int):
    return "PASSANGER_" + delete(passangerCollection, "userIdNumber", id)