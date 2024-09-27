from httpx import AsyncClient
import pytest
from pydantic import ValidationError
from app.progress.schemas import ProgressList


#1
async def test_progress_all(ac: AsyncClient):
    response = await ac.get("/progress/all")
    progress = response.json()
    
    assert response.status_code == 200
    assert progress
    
    for p in progress:
        try:
            progress_schema = ProgressList(**p)
            
            assert isinstance(progress_schema.id, int)
            assert isinstance(progress_schema.img, str)
        
        except ValidationError as e:
            assert False, f"Validation Error: {e}"
        except TypeError as e:
            assert False, f"Type Error: {e}"