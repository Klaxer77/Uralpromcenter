from typing import List, Optional
from pydantic import BaseModel, field_validator
from uuid import UUID
from app.exceptions.products.categories.exceptions import CategoryValidate

class SProductADD(BaseModel):
    name: str
    category_id: int
    img: str
    
    @field_validator("category_id")
    def check_category(v: int):
        if v < 1:
            raise CategoryValidate
        return v
 

class SCategory(BaseModel):
    id: int
    name: str
    
class SSubcategory(BaseModel):
    id: int
    name: str

class SProductsList(BaseModel):
    id: UUID
    name: str
    description: str
    img: str
    
class SProductSearch(BaseModel):
    name: str
    img: str

    
    