from typing import Optional
from fastapi import APIRouter

from app.news.dao import NewsDAO
from app.news.schemas import NewsList

router = APIRouter(prefix="/news", tags=["Новости"])


@router.get("/all")
async def get_all() -> list[NewsList]:
    news = await NewsDAO.find_all()
    return news

@router.get("/detail/{news_id}")
async def news_detail(news_id: int) -> Optional[NewsList]:
    news = await NewsDAO.find_one_or_none(id=news_id)
    return news
