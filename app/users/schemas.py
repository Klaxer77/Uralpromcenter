from pydantic import BaseModel, EmailStr
from uuid import UUID


class SUserAuth(BaseModel):
    email: EmailStr
    password: str
    
    
class SUser(BaseModel):
    id: int
    email: EmailStr
    
class SUserLogin(BaseModel):
    access_token: str