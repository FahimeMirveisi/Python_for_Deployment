from pydantic import BaseModel

# pydantic models for request validation

class RegisterModel(BaseModel):
    username: str
    password: str
    city: str
    first_name: str
    last_name: str
    email: str
    age: str 
    country: str
    join_time: str


class LoginModel(BaseModel):
    username: str
    password: str