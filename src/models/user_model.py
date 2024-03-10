from typing import Optional
from pydantic import BaseModel, Field, validator
from src.validation.parameter_checks import isValidEmail, isValidDate

dateErrorMessage = "Not valid date, expected format: YYYY-MM-DD"
emailErrorMessage = "Not valid email"

class UserCreate (BaseModel):
    userIdNumber: int = Field(gt=0)
    userName: str = Field(min_length=1, max_length=50)
    userAge: int = Field(ge=18)
    userEmail: str
    userPhone: int = Field(gt=0, le=9999999999)
    userAddress: str
    userCity: str = Field(min_length=3, max_length=50)
    userCountry: str = Field(min_length=3, max_length=50)
    userPostalCode: str = Field(min_length=4,max_length=15)
    userLicenseExpirationDate: str

    @validator('userEmail')
    def validateEmail(cls, email):
        if isValidEmail(email):
            return email
        else:
            raise ValueError(emailErrorMessage)
        
    @validator('userLicenseExpirationDate')
    def validateDate(cls, date):
        if isValidDate(date):
            return date
        else:
            raise ValueError(dateErrorMessage)

class UserPatch (BaseModel):
    userName: str = Field(None, max_length=50, min_length= 3)
    userAge: int = Field(None, ge=18)
    userEmail: str | None = None
    userPhone: int = Field(None, gt=0, le=9999999999)
    userAddress: str | None = None
    userCity: str = Field(None, min_length=3, max_length=50)
    userCountry: str = Field(None, min_length=3, max_length=50)
    userPostalCode: str = Field(None, min_length=4,max_length=15)
    userLicenseExpirationDate: str | None = None

    @validator('userEmail')
    def validateEmail(cls, email):
        if isValidEmail(email):
            return email
        else:
            raise ValueError(emailErrorMessage)
        
    @validator('userLicenseExpirationDate')
    def validateDate(cls, date):
        if isValidDate(date):
            return date
        else:
            raise ValueError(dateErrorMessage)

class UserPut (BaseModel):
    userName: str = Field(min_length=1, max_length=50)
    userAge: int = Field(ge=18)
    userEmail: str
    userPhone: int = Field(gt=0, le=9999999999)
    userAddress: str
    userCity: str = Field(min_length=3, max_length=50)
    userCountry: str = Field(min_length=3, max_length=50)
    userPostalCode: str = Field(min_length=4,max_length=15)
    userLicenseExpirationDate: str | None = None

    @validator('userEmail')
    def validateEmail(cls, email):
        if isValidEmail(email):
            return email
        else:
            raise ValueError(emailErrorMessage)
        
    @validator('userLicenseExpirationDate')
    def validateDate(cls, date):
        if isValidDate(date):
            return date
        else:
            raise ValueError(dateErrorMessage)