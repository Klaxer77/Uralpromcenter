import pytest
from pydantic import ValidationError

from app.recall.dao import RecallDAO
from app.recall.schemas import RecallList


#1
async def test_recall_all():
    recall = await RecallDAO.find_all()
    
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