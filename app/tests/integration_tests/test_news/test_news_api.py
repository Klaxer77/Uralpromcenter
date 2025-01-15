from datetime import datetime
from pydantic import ValidationError
import pytest
from httpx import AsyncClient
from app.news.schemas import NewsList


#1
@pytest.mark.asyncio
async def test_get_all(ac: AsyncClient):
    response = await ac.get("/news/all")
    news = response.json()
    
    assert news
    
    try:
        for new in news:
            
            if "created_at" in new:
                new["created_at"] = datetime.strptime(new["created_at"], "%d-%m-%Y").date()
                
            news_schem = NewsList(**new)
            
            assert isinstance(news_schem.id, int)
            assert isinstance(news_schem.name, str)
            assert isinstance(news_schem.text, str)
            assert isinstance(news_schem.img, str)
            assert isinstance(news_schem.created_at, str)
            
    except ValidationError as e:
        assert False, f"Validation Error: {e}"
    except TypeError as e:
        assert False, f"Type Error: {e}"
        
#2   
@pytest.mark.asyncio 
@pytest.mark.parametrize("news_id,if_exists", [
    (1,True),
    (2,True),
    (3,True),
    (50,False),
    (51,False),
])        
async def test_news_api_detail(news_id: int, if_exists: bool, ac: AsyncClient):
    response = await ac.get(f"/news/detail/{news_id}")
    news = response.json()

    if if_exists:
        assert news is not None  
        
        try:
            
            if "created_at" in news:
                news["created_at"] = datetime.strptime(news["created_at"], "%d-%m-%Y").date()

            news_data = {
                "id": news["id"],
                "name": news["name"],
                "text": news["text"],
                "img": news["img"],
                "created_at": news["created_at"]
            }
            
            news_schem = NewsList(**news_data)

            assert isinstance(news_schem.id, int)
            assert isinstance(news_schem.name, str)
            assert isinstance(news_schem.text, str)
            assert isinstance(news_schem.img, str)
            assert isinstance(news_schem.created_at, str)  

        except ValidationError as e:
            assert False, f"Validation Error: {e}"
        except TypeError as e:
            assert False, f"Type Error: {e}"
    else: 
        assert news is None  
            
    
    
    