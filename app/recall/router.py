from fastapi import APIRouter

from app.recall.dao import RecallDAO

router = APIRouter(prefix="/recall", tags=["Отзывы"])

@router.get("/all")
async def get_all():
    get_recall = await RecallDAO.find_all()
    return get_recall