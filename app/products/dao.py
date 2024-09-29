from uuid import UUID
from app.dao.base import BaseDAO
from app.products.categories.models import Categories
from app.products.models import Products
from app.database import async_session_maker
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.products.models import Products
from app.products.schemas import SCategory, SProductsList, SSubcategory
from app.logger import logger
from app.database import engine
from app.products.models import products_categories


class ProductDAO(BaseDAO):
    model = Products
    
    @classmethod
    async def search(cls, product_name: str):
        async with async_session_maker() as session:
            query = select(Products.id, Products.name, Products.img).where(Products.name.ilike(f"%{product_name}%"))
            result = await session.execute(query)
            return result.mappings().all()
        
    @classmethod
    async def find_many_in_subcategory(cls, subcategory_id: int, limit: int):
        async with async_session_maker() as session:
            query = select(Products).join(products_categories).where(
                products_categories.c.category_id == subcategory_id
            ).limit(limit)
            
            logger.debug(query.compile(engine, compile_kwargs={"literal_binds": True}))
            result = await session.execute(query)
            products = result.scalars().all()
            
            return products

            
    @classmethod
    async def find_many_in_parent_category(cls, parent_category_id: int, limit: int):
        async with async_session_maker() as session:
            query = select(Products).options(
                selectinload(Products.subcategories).options(selectinload(Categories.parent_category))
            ).join(products_categories).join(Categories).where(
                Categories.parent_category_id == parent_category_id
            ).limit(limit)
            
            logger.debug(query.compile(engine, compile_kwargs={"literal_binds": True}))
            result = await session.execute(query)
            return result.scalars().all()