from datetime import datetime
from pydantic import ValidationError
import pytest
from httpx import AsyncClient
from app.news.schemas import NewsList


#1
async def test_get_all(ac: AsyncClient):
    response = await ac.get("/api/news/all")
    news = response.json()
    
    assert news
    
    try:
        for new in news:
            
            if "created_at" in new:
                new["created_at"] = datetime.strptime(new["created_at"], "%d-%m-%Y").date()
                
            news_schem = NewsList(**new)
            
            assert isinstance(news_schem.id, int)
            assert isinstance(news_schem.name, str)
            assert isinstance(news_schem.title, str)
            assert isinstance(news_schem.text, str)
            assert isinstance(news_schem.img, str)
            assert isinstance(news_schem.created_at, str)
            
    except ValidationError as e:
        assert False, f"Validation Error: {e}"
    except TypeError as e:
        assert False, f"Type Error: {e}"
            
    
    
    