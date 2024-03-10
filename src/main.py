from fastapi import FastAPI
from src.routers.driver_router import driver_router
from src.routers.passanger_router import passanger_router
from src.routers.vehicle_router import vehicle_router


app = FastAPI()
app.title = "wheelsUN_users_ms"
app.version = "0.3.3"

app.include_router(tags=["Driver"] ,prefix="/driver", router=driver_router)
app.include_router(tags=["Passanger"] ,prefix="/passanger", router=passanger_router)
app.include_router(tags=["Vehicle"] ,prefix="/vehicle", router=vehicle_router)