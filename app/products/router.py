from fastapi import APIRouter
from uuid import UUID
from app.exceptions.products.categories.exceptions import NoneCategory
from app.exceptions.products.exceptions import ProductCreated, ProductImgException, ProductNameException
from app.exceptions.schemas import SException
from app.products.categories.dao import CategoryDAO
from app.products.dao import ProductDAO
from app.products.schemas import SProductADD, SProductSearch, SProductsList
from app.logger import logger

router = APIRouter(prefix="/product", tags=["Продукты"])

@router.get("/all")
async def get_all(limit: int) -> list[SProductsList]:
    get_products = await ProductDAO.get_products_all(limit=limit)
    return get_products

@router.get("/subcategory/{subcategory_id}")
async def get_products_in_subcategory(subcategory_id: int) -> list[SProductsList]:
    get_products = await ProductDAO.find_many_in_subcategory(subcategory_id=subcategory_id)
    return get_products

@router.get("/parent_category/{parent_category_id}")
async def get_products_in_category(parent_category_id: int) -> list[SProductsList]:
    get_products = await ProductDAO.find_many_in_parent_category(parent_category_id=parent_category_id)
    return get_products

@router.get("/search")
async def product_search(product_name: str) -> list[SProductSearch]:
    get_products = await ProductDAO.search(product_name=product_name)
    return get_products
