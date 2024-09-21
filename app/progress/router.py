from fastapi import APIRouter

from app.progress.dao import ProgressDAO
from app.progress.schemas import ProgressList

router = APIRouter(prefix="/progress", tags=["Достижения"])

@router.get("/all")
async def get_all() -> list[ProgressList]:
    get_progress = await ProgressDAO.find_all()
    return get_progress