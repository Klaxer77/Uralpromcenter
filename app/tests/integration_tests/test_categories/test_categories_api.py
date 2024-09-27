from pydantic import ValidationError
import pytest
from app.products.categories.schemas import SCategoryList
from httpx import AsyncClient



async def test_get_categories_api_all(ac: AsyncClient):
    response = await ac.get("/category/all")
    categories = response.json()
    
    assert response.status_code == 200
    assert categories
    
    for category in categories:
        try:
            category_data = {
                'id': category["id"],
                'name': category["name"],
                'subcategories': [
                    {
                        'id': subcategory["id"],
                        'name': subcategory["name"]
                    } for subcategory in category["subcategories"]
                ] if category["subcategories"] else []
            }

            category_schem = SCategoryList(**category_data)
            assert isinstance(category_schem.id, int)
            assert isinstance(category_schem.name, str)
            assert isinstance(category_schem.subcategories, list)

        except ValidationError as e:
            assert False, f"Validation Error for category {category.id}: {e}"
        except TypeError as e:
            assert False, f"Type Error for category {category.id}: {e}" 
    
    
    