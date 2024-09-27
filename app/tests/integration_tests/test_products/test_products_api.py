from uuid import UUID
from pydantic import ValidationError
import pytest
from httpx import AsyncClient

from app.products.schemas import SCategory, SProductSearch, SProductsList, SSubcategory
            
#1
@pytest.mark.parametrize("subcategory_id,limit,is_exists", [
    (1,2,True),
    (2,1,True),
    (3,1,False),
    (4,1,False)
])
async def test_get_products_in_subcategory(subcategory_id: int, limit: int, is_exists: bool, ac: AsyncClient):
    response = await ac.get(f"/product/subcategory/{subcategory_id}", params={
        "limit":limit
    })
    products = response.json()
    
    assert response.status_code == 200
    
    if is_exists:
        assert products
        assert len(products) == limit
        for product in products:
            try:
                product_data = {
                'id': product["id"],
                'name': product["name"],
                'img': product["img"],
            }
                
                product_schem = SProductsList(**product_data)

                assert isinstance(product_schem.id, UUID)
                assert isinstance(product_schem.name, str)
                assert isinstance(product_schem.img, str)
                
            except ValidationError as e:
                assert False, f"Validation Error: {e}"
            except TypeError as e:
                assert False, f"Type Error: {e}"
    else: 
        assert products == []
        
#2
@pytest.mark.parametrize("parent_category_id,limit,is_exists", [
    (1,1,False),
    (2,1,False),
    (3,1,False),
    (4,1,True),
    (5,1,True)
])
async def test_get_products_in_category(parent_category_id: int, limit: int,is_exists: bool, ac: AsyncClient):
    response = await ac.get(f"/product/parent_category/{parent_category_id}", params={
        "limit":limit
    })
    products = response.json()
    
    assert response.status_code == 200
    
    if is_exists:
        assert products
        assert len(products) == limit
        for product in products:
            try:
                product_data = {
                'id': product["id"],
                'name': product["name"],
                'img': product["img"],
            }
                
                product_schem = SProductsList(**product_data)

                assert isinstance(product_schem.id, UUID)
                assert isinstance(product_schem.name, str)
                assert isinstance(product_schem.img, str)
                
            except ValidationError as e:
                assert False, f"Validation Error: {e}"
            except TypeError as e:
                assert False, f"Type Error: {e}"
    else: 
        assert products == []
        
        
#3       
@pytest.mark.parametrize("product_name,is_exists",[
    ("Продукт1",True),
    ("Продукт2",True),
    ("Продукт",True),
    ("П",True),
    ("П",True),
    ("Й",False),
    ("нанана",False)
])        
async def test_product_search(product_name: str, is_exists: bool, ac: AsyncClient):
    response = await ac.get("/product/search", params={
        "product_name": product_name
    })
    
    products = response.json()
    assert response.status_code == 200
    
    if is_exists:
        assert response
        assert products
        
        for product in products:
            product_data = {
                    "name": product["name"],
                    "img": product["img"]
                    }
        
        product_schem = SProductSearch(**product_data)
        
        assert isinstance(product_schem.name, str)
        assert isinstance(product_schem.img, str)
    
    else:
        assert products == []