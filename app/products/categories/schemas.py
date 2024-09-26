from typing import List
from pydantic import BaseModel


class SCategory(BaseModel):
    name: str
    
class SSubcategory(BaseModel):
    id: int
    name: str

class SCategoryList(BaseModel):
    id: int
    name: str
    subcategories: list[SSubcategory]