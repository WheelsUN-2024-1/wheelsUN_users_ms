from fastapi import APIRouter, Path
from src.models.user_model import DriverCreate, DriverPatch, DriverPut
from src.database.firestore_crud import getAll, getByParameter, create, patch, delete

driver_router = APIRouter()

driversCollection = "driverCollection"

@driver_router.get("/")
async def getDrivers():
    doc_getAll = getAll(driversCollection)
    users=[]
    for doc in doc_getAll:
        users.append(doc.to_dict())
    return users

@driver_router.get("/{id}")
async def getDriverById(id:int):
    docs = getByParameter(driversCollection, "userIdNumber", id)
    for doc in docs:
        return doc.to_dict()
    return "DRIVER_NOT_FOUND"

@driver_router.post("/")
async def createDriver(user: DriverCreate):
    docs = getByParameter(driversCollection, "userIdNumber", user.userIdNumber)
    for doc in docs: #this verifies if there is a Driver
        return "ALREADY_DRIVER"
    create(driversCollection, user)
    return await getDriverById(user.userIdNumber)

@driver_router.patch("/{id}")
async def patchDriver(id: int, user: DriverPatch):
    patch(driversCollection, "userIdNumber", id, user)
    return await getDriverById(id)

@driver_router.put("/{id}")
async def putDriver(id: int, user: DriverPut):
    patch(driversCollection, "userIdNumber", id, user)
    return await getDriverById(id)

@driver_router.delete("/{id}")
async def deleteDriver(id: int):
    return "DRIVER_" + delete(driversCollection, "userIdNumber", id)