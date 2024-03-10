from typing import Optional
from pydantic import BaseModel, Field, validator
from src.validation.parameter_checks import isValidPlate
import datetime

current_year = datetime.datetime.now().year

class VehicleCreate (BaseModel):
    vehicleOwnerId: int = Field(gt=0)
    vehiclePlate: str
    vehicleBrand: str = Field(min_length=1, max_length=50)
    vehicleModel: str = Field(min_length=1, max_length=50)
    vehicleCylinder: str  = Field(min_length=1, max_length=50)
    vehicleYear: int = Field(ge= 1900, le=current_year + 1)
    vehicleSeatingCapacity: int =Field(ge= 1)

    @validator('vehiclePlate')
    def validatePlate(cls, plate):
        if isValidPlate(plate):
            return plate
        else:
            raise ValueError("Not valid plate, accpeted format is: AAA000")
    

class VehiclePatch (BaseModel):
    vehicleBrand: str = Field(None, min_length=1, max_length=50)
    vehicleModel: str = Field(None, min_length=1, max_length=50)
    vehicleCylinder: str  = Field(None, min_length=1, max_length=50)
    vehicleYear: int = Field(None, ge= 1900, le=current_year + 1)
    vehicleSeatingCapacity: int =Field(None, ge= 1)
        
class VehiclePut (BaseModel):
    vehicleBrand: str = Field(min_length=1, max_length=50)
    vehicleModel: str = Field(min_length=1, max_length=50)
    vehicleCylinder: str  = Field(min_length=1, max_length=50)
    vehicleYear: int = Field(ge= 1900, le=current_year + 1)
    vehicleSeatingCapacity: int =Field(ge= 1)