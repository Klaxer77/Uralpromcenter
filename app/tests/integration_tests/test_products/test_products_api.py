from uuid import UUID
from pydantic import ValidationError
import pytest
from httpx import AsyncClient

from app.products.schemas import SCategory, SProductSearch, SProductsList, SSubcategory


#1
@pytest.mark.parametrize("limit",[
    (1),
    (2),
    (3)
])
async def test_get_all(limit:int, ac: AsyncClient):
    response = await ac.get("/api/product/all", params={
        "limit":limit
    })
    products = response.json()
    
    assert response.status_code == 200
    assert products
    assert len(products) == limit
    
    for product in products:
            try:
                product_data = {
                'id': product["id"],
                'name': product["name"],
                'img': product["img"],
                'subcategories': [
                    {
                        'id': subcategory["id"],
                        'name': subcategory["name"],
                        'parent_category': {
                            'id': subcategory["parent_category"]["id"],
                            'name': subcategory["parent_category"]["name"]
                        } if subcategory["parent_category"] else None
                    } for subcategory in product["subcategories"]
                ] if product["subcategories"] else []
            }
                
                product_schem = SProductsList(**product_data)

                assert isinstance(product_schem.id, UUID)
                assert isinstance(product_schem.name, str)
                assert isinstance(product_schem.img, str)
                assert isinstance(product_schem.subcategories, list)
                assert all(isinstance(subcat, SSubcategory) for subcat in product_schem.subcategories)
                
            except ValidationError as e:
                assert False, f"Validation Error: {e}"
            except TypeError as e:
                assert False, f"Type Error: {e}"
            
#2
@pytest.mark.parametrize("subcategory_id,is_exists", [
    (1,True),
    (2,True),
    (3,False),
    (4,False)
])
async def test_get_products_in_subcategory(subcategory_id: int, is_exists: bool, ac: AsyncClient):
    response = await ac.get(f"/api/product/subcategory/{subcategory_id}")
    products = response.json()
    
    assert response.status_code == 200
    
    if is_exists:
        assert products
        for product in products:
            try:
                product_data = {
                'id': product["id"],
                'name': product["name"],
                'img': product["img"],
                'subcategories': [
                    {
                        'id': subcategory["id"],
                        'name': subcategory["name"],
                        'parent_category': {
                            'id': subcategory["parent_category"]["id"],
                            'name': subcategory["parent_category"]["name"]
                        } if subcategory["parent_category"] else None
                    } for subcategory in product["subcategories"]
                ] if product["subcategories"] else []
            }
                
                product_schem = SProductsList(**product_data)

                assert isinstance(product_schem.id, UUID)
                assert isinstance(product_schem.name, str)
                assert isinstance(product_schem.img, str)
                assert isinstance(product_schem.subcategories, list)
                assert all(isinstance(subcat, SSubcategory) for subcat in product_schem.subcategories)
                
            except ValidationError as e:
                assert False, f"Validation Error: {e}"
            except TypeError as e:
                assert False, f"Type Error: {e}"
    else: 
        assert products == []
        
#3
@pytest.mark.parametrize("parent_category_id,is_exists", [
    (1,False),
    (2,False),
    (3,False),
    (4,True),
    (5,True)
])
async def test_get_products_in_category(parent_category_id: int, is_exists: bool, ac: AsyncClient):
    response = await ac.get(f"/api/product/parent_category/{parent_category_id}")
    products = response.json()
    
    assert response.status_code == 200
    
    if is_exists:
        assert products
        for product in products:
            try:
                product_data = {
                'id': product["id"],
                'name': product["name"],
                'img': product["img"],
                'subcategories': [
                    {
                        'id': subcategory["id"],
                        'name': subcategory["name"],
                        'parent_category': {
                            'id': subcategory["parent_category"]["id"],
                            'name': subcategory["parent_category"]["name"]
                        } if subcategory["parent_category"] else None
                    } for subcategory in product["subcategories"]
                ] if product["subcategories"] else []
            }
                
                product_schem = SProductsList(**product_data)

                assert isinstance(product_schem.id, UUID)
                assert isinstance(product_schem.name, str)
                assert isinstance(product_schem.img, str)
                assert isinstance(product_schem.subcategories, list)
                assert all(isinstance(subcat, SSubcategory) for subcat in product_schem.subcategories)
                
            except ValidationError as e:
                assert False, f"Validation Error: {e}"
            except TypeError as e:
                assert False, f"Type Error: {e}"
    else: 
        assert products == []
        
        
#4       
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
    response = await ac.get("/api/product/search", params={
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