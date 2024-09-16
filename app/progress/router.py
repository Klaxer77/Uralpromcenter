from fastapi import APIRouter

from app.recall.dao import RecallDAO

router = APIRouter(prefix="/progress", tags=["Достижения"])

@router.get("/all")
async def get_all():
    get_progress = await RecallDAO.find_all()
    return get_progress