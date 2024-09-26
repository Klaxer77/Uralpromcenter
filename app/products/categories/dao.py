from app.dao.base import BaseDAO
from app.products.categories.models import Categories
from app.database import async_session_maker
from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload

from app.products.categories.schemas import SCategoryList
from app.products.models import Products
from app.products.schemas import SCategory, SSubcategory


class CategoryDAO(BaseDAO):
    model = Categories
    
    @classmethod
    async def get_categories_all(cls):
        async with async_session_maker() as session:
            query = select(Categories)
            results = await session.execute(query)
            result_orm = results.scalars().all()

            result_dto = []
            for category in result_orm:
                if category.parent_category is None:
                    subcategories = []
                    for subcategory in result_orm:
                        if subcategory.parent_category_id == category.id:
                            subcategories.append(SSubcategory(
                                id=subcategory.id,
                                name=subcategory.name
                            ))
                    result_dto.append(SCategoryList(
                        id=category.id,
                        name=category.name,
                        subcategories=[s.dict() for s in subcategories]
                    ))

            return result_dto