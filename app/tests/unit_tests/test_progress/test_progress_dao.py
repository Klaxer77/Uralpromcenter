import pytest
from pydantic import ValidationError

from app.progress.dao import ProgressDAO
from app.progress.schemas import ProgressList


#1
@pytest.mark.asyncio
async def test_progress_all():
    progress = await ProgressDAO.find_all()
    
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