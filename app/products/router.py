from fastapi import APIRouter
from uuid import UUID
from app.exceptions.products.categories.exceptions import NoneCategory
from app.exceptions.products.exceptions import ProductCreated, ProductImgException, ProductNameException
from app.exceptions.schemas import SException
from app.products.categories.dao import CategoryDAO
from app.products.dao import ProductDAO
from app.products.schemas import SProductADD, SProductSearch, SProductsList
from app.logger import logger
from fastapi_pagination import Page, paginate

router = APIRouter(prefix="/product", tags=["Продукты"])

@router.get("/subcategory/{subcategory_id}")
async def get_products_in_subcategory(subcategory_id: int) -> Page[SProductsList]:
    get_products = await ProductDAO.find_many_in_subcategory(subcategory_id=subcategory_id)
    return paginate(get_products)

@router.get("/parent_category/{parent_category_id}")
async def get_products_in_category(parent_category_id: int) -> Page[SProductsList]:
    get_products = await ProductDAO.find_many_in_parent_category(parent_category_id=parent_category_id)
    return paginate(get_products)

@router.get("/search")
async def product_search(product_name: str) -> list[SProductSearch]:
    get_products = await ProductDAO.search(product_name=product_name)
    return get_products
