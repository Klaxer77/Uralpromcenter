from datetime import date
from pydantic import ValidationError
import pytest
from app.news.dao import NewsDAO
from app.news.schemas import NewsList

#1
async def test_find_all():
    news_items = await NewsDAO.find_all()
    
    assert news_items

    for item in news_items:
        try:
            
            news_schem = NewsList(**item)

            assert isinstance(news_schem.id, int)
            assert isinstance(news_schem.name, str)
            assert isinstance(news_schem.title, str)
            assert isinstance(news_schem.text, str)
            assert isinstance(news_schem.created_at, str)

        except ValidationError as e:
            assert False, f"Validation Error: {e}"
        except TypeError as e:
            assert False, f"Type Error: {e}"
 
        

    