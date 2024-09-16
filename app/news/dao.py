from app.news.models import News
from app.dao.base import BaseDAO


class NewsDAO(BaseDAO):
    model = News