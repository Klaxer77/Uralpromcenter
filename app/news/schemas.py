from pydantic import BaseModel, field_validator
from datetime import date

class NewsList(BaseModel):
    id: int
    name: str
    title: str
    text: str
    img: str
    created_at: date
    
    @field_validator("created_at")
    def check_created_at(v:date):
        return v.strftime("%d-%m-%Y")
    
