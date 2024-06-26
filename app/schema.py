from pydantic import BaseModel,EmailStr

class ForecastWeather(BaseModel):
    city: str
    country: str

class User(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: str

class TokenData(BaseModel):
    id: int