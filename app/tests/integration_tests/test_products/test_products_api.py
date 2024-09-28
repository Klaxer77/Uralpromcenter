from uuid import UUID
import httpx
from pydantic import ValidationError
import pytest
from httpx import AsyncClient
from fastapi_pagination import Page
from app.products.schemas import SCategory, SProductSearch, SProductsList, SSubcategory
            
#1
@pytest.mark.parametrize("subcategory_id,page,size,is_exists", [
    (7,1,1,True),
    (1,1,1,True),
    (6,1,1,True),
    (3,1,1,False),
    (4,1,1,False)
])
async def test_get_products_in_subcategory(subcategory_id: int, 
    page: int, 
    size: int, 
    is_exists: bool,
    ac_pagination: AsyncClient
    ):
    response = await ac_pagination.get(f"/product/subcategory/{subcategory_id}", params={
        "page":page,
        "size":size
    })
    products = response.json()
    
    assert response.status_code == 200
    
    if is_exists:
        assert products["items"]
        assert len(products["items"]) == size
        for product in products["items"]:
            try:
                product_data = {
                'id': product["id"],
                'name': product["name"],
                'description': product["description"],
                'img': product["img"],
            }
                
                product_schem = (SProductsList(**product_data))

                assert isinstance(product["id"], str)
                assert isinstance(product["name"], str)
                assert isinstance(product["description"], str)
                assert isinstance(product["img"], str)
                
            except ValidationError as e:
                assert False, f"Validation Error: {e}"
            except TypeError as e:
                assert False, f"Type Error: {e}"
    else: 
        assert products == {
            "items": [],
            "total": len(products["items"]),
            "page": page,
            "size": size,
            "pages": 0
        }
        
#2
@pytest.mark.parametrize("parent_category_id,page,size,is_exists", [
    (5,1,1,True),
    (4,1,1,True),
    (6,1,1,False),
    (3,1,1,False),
])
async def test_get_products_in_parent_category(parent_category_id: int, 
                                        page: int, 
                                        size: int, 
                                        is_exists: bool, 
                                        ac_pagination: AsyncClient):
    response = await ac_pagination.get(f"/product/parent_category/{parent_category_id}", params={
        "page":page,
        "size":size
    })
    products = response.json()
    
    assert response.status_code == 200
    
    if is_exists:
        assert products["items"]
        assert len(products["items"]) == size
        for product in products["items"]:
            try:
                product_data = {
                'id': product["id"],
                'name': product["name"],
                'description': product["description"],
                'img': product["img"],
            }
                
                product_schem = (SProductsList(**product_data))

                assert isinstance(product["id"], str)
                assert isinstance(product["name"], str)
                assert isinstance(product["description"], str)
                assert isinstance(product["img"], str)
                
            except ValidationError as e:
                assert False, f"Validation Error: {e}"
            except TypeError as e:
                assert False, f"Type Error: {e}"
    else: 
        assert products == {
            "items": [],
            "total": len(products["items"]),
            "page": page,
            "size": size,
            "pages": 0
        }
        
        
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