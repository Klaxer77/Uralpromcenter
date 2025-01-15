from datetime import date
from pydantic import ValidationError
import pytest
from app.news.dao import NewsDAO
from app.news.schemas import NewsList

#1
@pytest.mark.asyncio
async def test_find_all():
    news_items = await NewsDAO.find_all()
    
    assert news_items

    for item in news_items:
        try:
            
            news_schem = NewsList(**item)

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
async def test_news_detail(news_id: int, if_exists: bool):
    news = await NewsDAO.find_one_or_none(id=news_id)
    
    if if_exists:
        assert news
        try:
            news_schem = NewsList(**news)
            
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
 
        

    