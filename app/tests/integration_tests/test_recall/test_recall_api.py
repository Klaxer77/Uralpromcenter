from httpx import AsyncClient
import pytest
from pydantic import ValidationError
from app.recall.schemas import RecallList


#1
@pytest.mark.asyncio
async def test_recall_all(ac: AsyncClient):
    response = await ac.get("/recall/all")
    recall = response.json()
    
    assert response.status_code == 200
    assert recall
    
    for r in recall:
        try:
            recall_schema = RecallList(**r)
            
            assert isinstance(recall_schema.id, int)
            assert isinstance(recall_schema.img, str)
        
        except ValidationError as e:
            assert False, f"Validation Error: {e}"
        except TypeError as e:
            assert False, f"Type Error: {e}"
    
    