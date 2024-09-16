from pydantic import BaseModel, EmailStr, field_validator

from app.exceptions.base import NumberError


class SSendRequest(BaseModel):
    lastname: str
    firstname_and_surname: str
    number: str = "+7"
    organization: str
    email: EmailStr
    message: str
    
    @field_validator("number")
    def check_number(cls, v: str):
        if not (v.startswith('+') and v[1:].isdigit() and len(v) == 12):
            raise NumberError
        return v
