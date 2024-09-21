from fastapi import APIRouter

from app.recall.dao import RecallDAO
from app.recall.schemas import RecallList

router = APIRouter(prefix="/recall", tags=["Отзывы"])

@router.get("/all")
async def get_all() -> list[RecallList]:
    get_recall = await RecallDAO.find_all()
    return get_recall