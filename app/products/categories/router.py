from fastapi import APIRouter

from app.exceptions.products.categories.exceptions import CategoryCreated
from app.products.categories.dao import CategoryDAO
from app.products.categories.schemas import SCategory, SCategoryList

router = APIRouter(prefix="/category", tags=["Категории"])

@router.get("/all")
async def get_all() -> list[SCategoryList]:
    categories = await CategoryDAO.get_categories_all()
    return categories
