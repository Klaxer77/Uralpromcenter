from fastapi import APIRouter

from app.exceptions.products.categories.exceptions import CategoryCreated
from app.products.categories.dao import CategoryDAO
from app.products.categories.schemas import SCategory

router = APIRouter(prefix="/category", tags=["Categories"])
