from fastapi import APIRouter
from uuid import UUID

from fastapi.responses import JSONResponse
from app.exceptions.products.categories.exceptions import NoneCategory
from app.exceptions.products.exceptions import ProductCreated, ProductImgException, ProductNameException
from app.exceptions.schemas import SException
from app.products.categories.dao import CategoryDAO
from app.products.dao import ProductDAO
from app.products.schemas import SProductADD, SProductSearch, SProductsList
from app.logger import logger

router = APIRouter(prefix="/product", tags=["Продукты"])

@router.get("/subcategory/{subcategory_id}")
async def get_products_in_subcategory(subcategory_id: int, limit: int) -> SProductsList:
    adjusted_limit = (limit // 6) * 6 if limit % 6 == 0 else ((limit // 6) + 1) * 6
    
    get_products = await ProductDAO.find_many_in_subcategory(subcategory_id=subcategory_id, limit=adjusted_limit)
    
    if len(get_products) < limit:
        limit = len(get_products)

    has_more_items = len(get_products) > limit or len(get_products) == adjusted_limit
    
    return {
        "products": get_products[:limit],
        "has_more": has_more_items
    }

@router.get("/parent_category/{parent_category_id}")
async def get_products_in_category(parent_category_id: int, limit: int) -> SProductsList:
    adjusted_limit = (limit // 6) * 6 if limit % 6 == 0 else ((limit // 6) + 1) * 6
    
    get_products = await ProductDAO.find_many_in_parent_category(parent_category_id=parent_category_id, limit=adjusted_limit)
    
    if len(get_products) < limit:
        limit = len(get_products)

    has_more_items = len(get_products) > limit or len(get_products) == adjusted_limit
    
    return {
        "products": get_products[:limit],
        "has_more": has_more_items
    }

@router.get("/search")
async def product_search(product_name: str) -> list[SProductSearch]:
    get_products = await ProductDAO.search(product_name=product_name)
    return get_products
