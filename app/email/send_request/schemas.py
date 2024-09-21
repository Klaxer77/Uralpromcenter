from pydantic import BaseModel, EmailStr, field_validator

from app.exceptions.base import NumberError, ValueLenCommentError
from app.exceptions.sendrequest.exceptions import SendRequestFirtsNameANDLastNameError, SendRequestLastNameError, SendRequestOrganizationError


class SSendRequest(BaseModel):
    lastname: str
    firstname_and_surname: str
    number: str = "+7"
    organization: str
    email: EmailStr
    message: str
    
    @field_validator("number")
    def check_number(v: str):
        if not (v.startswith('+') and v[1:].isdigit() and len(v) == 12):
            raise NumberError
        return v
    
    @field_validator("message")
    def check_message(v:str):
        if len(v) >= 500:
            raise ValueLenCommentError
        return v
    
    @field_validator("organization")
    def check_organization(v:str):
        if len(v) >= 50:
            raise SendRequestOrganizationError
        return v
    
    @field_validator("lastname")
    def check_lastname(v:str):
        if len(v) >= 50:
            raise SendRequestLastNameError
        return v
    
    @field_validator("firstname_and_surname")
    def check_firstname_and_surname(v:str):
        if len(v) >= 50:
            raise SendRequestFirtsNameANDLastNameError
        return v
