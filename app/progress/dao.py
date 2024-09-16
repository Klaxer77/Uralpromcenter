from app.dao.base import BaseDAO
from app.progress.models import Progress


class ProgressDAO(BaseDAO):
    model = Progress