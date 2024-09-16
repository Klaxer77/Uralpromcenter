from pydantic import BaseModel, field_validator

from app.exceptions.base import NumberError, ValueLenError


class SOrderCall(BaseModel):
    name: str
    number: str = "+7"
    comment: str
    
    @field_validator("number")
    def check_number(cls, v: str):
        if not (v.startswith('+') and v[1:].isdigit() and len(v) == 12):
            raise NumberError
        return v
    
    @field_validator("name")
    def check_name(v:str):
        if len(v) >= 100:
            raise ValueLenError
        return v
    
    @field_validator("comment")
    def check_comment(v:str):
        if len(v) >= 500:
            raise ValueLenError
        return v