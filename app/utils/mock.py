from datetime import datetime
from app.database import Base, async_session_maker, engine
import json
from app.users.models import Users  #noqa
from app.products.models import Products, products_categories  #noqa
from app.news.models import News  #noqa
from app.products.categories.models import Categories  #noqa
from sqlalchemy import insert


async def mock_script():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        
    def open_mock_json(model: str):
        with open(f"app/tests/mock_{model}.json", encoding="utf-8") as file:
            return json.load(file)
        
    categories = open_mock_json("categories")   
    products = open_mock_json("products") 
    users = open_mock_json("users")
    news = open_mock_json("news")
    products_categories_data = open_mock_json("products_categories")
    
    for new in news:
        new["created_at"] = datetime.strptime(new["created_at"], "%d-%m-%Y")
    
    async with async_session_maker() as session:
        add_categories = insert(Categories).values(categories)
        add_products = insert(Products).values(products)
        add_users = insert(Users).values(users)
        add_news = insert(News).values(news)
        add_products_categories = insert(products_categories).values(products_categories_data)
        
        await session.execute(add_categories)
        await session.execute(add_products)
        await session.execute(add_users)
        await session.execute(add_news)
        await session.execute(add_products_categories)
        
        await session.commit()

    