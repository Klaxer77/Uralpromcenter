from app.dao.base import BaseDAO
from app.recall.models import Recall


class RecallDAO(BaseDAO):
    model = Recall