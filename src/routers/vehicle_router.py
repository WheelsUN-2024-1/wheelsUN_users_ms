from fastapi import APIRouter, Path
from src.models.vehicle_model import VehicleCreate, VehiclePatch, VehiclePut
from src.database.firestore_crud import getAll, getByParameter, create, patch, delete
from src.routers.driver_router import getDriverById

vehicle_router = APIRouter()

vehicleCollection = "vehicleCollection"

@vehicle_router.get("/")
async def getVehicles():
    doc_getAll = getAll(vehicleCollection)
    vehicles=[]
    for doc in doc_getAll:
        vehicles.append(doc.to_dict())
    return vehicles

@vehicle_router.get("/plate/{plate}")
async def getVehicleByPlate(plate:str):
    docs = getByParameter(vehicleCollection, "vehiclePlate", plate)
    for doc in docs:
        return doc.to_dict()
    return "VEHICLE_NOT_FOUND"

@vehicle_router.get("/ownerId/{id}")
async def getVehiclesById(id:int):
    docs = getByParameter(vehicleCollection, "vehicleOwnerId", id)
    vehicles=[]
    for doc in docs:
        vehicles.append(doc.to_dict())
    if len(vehicles) != 0:
        return vehicles
    else:
        return "NOT_VEHICLE_FOUND_FOR_THIS_ID"

@vehicle_router.post("/")
async def createVehicle(vehicle: VehicleCreate):
    print(getDriverById(vehicle.vehicleOwnerId))
    if (await getDriverById(vehicle.vehicleOwnerId)) == "DRIVER_NOT_FOUND":
        return "VEHICLE_OWNER_NOT_REGISTERED"
    docs = getByParameter(vehicleCollection, "vehiclePlate", vehicle.vehiclePlate)
    for doc in docs: #this verifies if there is a vehicle
        return "ALREADY_VEHICLE"
    create(vehicleCollection, vehicle)
    return await getVehicleByPlate(vehicle.vehiclePlate)

@vehicle_router.patch("/{plate}")
async def patchVehicle(plate: str, vehicle: VehiclePatch):
    patch(vehicleCollection, "vehiclePlate", plate, vehicle)
    return await getVehicleByPlate(plate)

@vehicle_router.put("/{plate}")
async def updateVehicle(plate: str, vehicle: VehiclePut):
    patch(vehicleCollection, "vehiclePlate", plate, vehicle)
    return await getVehicleByPlate(plate)

@vehicle_router.delete("/{plate}")
async def deleteVehicle(plate: str):
    return "VEHICLE_" + delete(vehicleCollection, "vehiclePlate", plate)