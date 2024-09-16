from app.dao.base import BaseDAO
from app.products.categories.models import Categories
from app.database import async_session_maker
from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload


class CategoryDAO(BaseDAO):
    model = Categories
    