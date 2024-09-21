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
            query = select(Products.name, Products.img).where(Products.name.ilike(f"%{product_name}%"))
            result = await session.execute(query)
            return result.scalars().all()
        
    @classmethod
    async def get_products_all(cls,limit: int):
        async with async_session_maker() as session:
            query = select(Products).options(
                selectinload(Products.subcategories).options(selectinload(Categories.parent_category))
            ).limit(limit)
            result = await session.execute(query)
            result_orm = result.scalars().all()

            result_dto = []
            for row in result_orm:
                subcategories = []
                
                for category in row.subcategories:
                    parent_category = None
                    if category.parent_category:
                        parent_category = SCategory(
                            id=category.parent_category.id,
                            name=category.parent_category.name
                        )

                    subcategories.append(SSubcategory(
                        id=category.id,
                        name=category.name,
                        parent_category=parent_category
                    ))

                product_dto = SProductsList(
                    id=row.id,
                    name=row.name,
                    img=row.img,
                    subcategories=subcategories
                )
                result_dto.append(product_dto)

            return result_dto
        
    @classmethod
    async def find_many_in_subcategory(cls, subcategory_id: int):
        async with async_session_maker() as session:
            query = select(Products).options(
                selectinload(Products.subcategories)
                .options(selectinload(Categories.parent_category))
            ).join(products_categories).where(products_categories.c.category_id == subcategory_id)
            
            logger.debug(query.compile(engine, compile_kwargs={"literal_binds": True}))
            result = await session.execute(query)
            result_orm = result.scalars().all()

            result_dto = []
            for row in result_orm:
                subcategories = []
                
                for category in row.subcategories:
                    parent_category = None
                    if category.parent_category:
                        parent_category = SCategory(
                            id=category.parent_category.id,
                            name=category.parent_category.name
                        )

                    subcategories.append(SSubcategory(
                        id=category.id,
                        name=category.name,
                        parent_category=parent_category
                    ))

                product_dto = SProductsList(
                    id=row.id,
                    name=row.name,
                    img=row.img,
                    subcategories=subcategories
                )
                result_dto.append(product_dto)

            return result_dto

            
    @classmethod
    async def find_many_in_parent_category(cls, parent_category_id: int):
        async with async_session_maker() as session:
            query = select(Products).options(
                selectinload(Products.subcategories).options(selectinload(Categories.parent_category))
            ).join(products_categories).join(Categories).where(
                Categories.parent_category_id == parent_category_id
            )
            
            logger.debug(query.compile(engine, compile_kwargs={"literal_binds": True}))
            result = await session.execute(query)
            result_orm = result.scalars().all()

            result_dto = []
            for row in result_orm:
                subcategories = []
                
                for category in row.subcategories:
                    parent_category = None
                    if category.parent_category:
                        parent_category = SCategory(
                            id=category.parent_category.id,
                            name=category.parent_category.name
                        )

                    subcategories.append(SSubcategory(
                        id=category.id,
                        name=category.name,
                        parent_category=parent_category
                    ))

                product_dto = SProductsList(
                    id=row.id,
                    name=row.name,
                    img=row.img,
                    subcategories=subcategories
                )
                result_dto.append(product_dto)

            return result_dto
        
    @classmethod
    async def search(cls, product_name: str):
        async with async_session_maker() as session:
            query = select(Products.name, Products.img).where(Products.name.ilike(f"%{product_name}%"))
            result = await session.execute(query)
            return result.mappings().all()