from uuid import UUID
import httpx
from pydantic import ValidationError
import pytest
from httpx import AsyncClient
from app.products.dao import ProductDAO
from app.products.schemas import SCategory, SProductSearch, SProducts, SProductsList, SSubcategory
            
#1
@pytest.mark.asyncio
@pytest.mark.parametrize("subcategory_id, limit, expected_count, has_more", [
    (7,1,1,False),
    (1,1,1,True),
    (6,1,1,False),
    (3,1,0,False),
    (4,1,0,False)
])
async def test_get_products_in_subcategory(
    subcategory_id: int, 
    limit: int, 
    expected_count: int, 
    has_more: bool,
    ac: AsyncClient
    ):
    response = await ac.get(f"/product/subcategory/{subcategory_id}", params={
        "limit":limit
    })
    products = response.json()
    
    assert response.status_code == 200
    assert len(products["products"]) == expected_count
    
    if expected_count > 0:
        for product in products["products"]:
            try:
                product_data = {
                    'id': product["id"],
                    'name': product["name"],
                    'description': product["description"],
                    'img': product["img"],
                }
                
                product_schem = SProducts(**product_data)

                assert isinstance(product_schem.id, UUID)
                assert isinstance(product_schem.name, str)
                assert isinstance(product_schem.description, str)
                assert isinstance(product_schem.img, str)
                
            except ValidationError as e:
                assert False, f"Validation Error: {e}"
            except TypeError as e:
                assert False, f"Type Error: {e}"

    expected_products = await ProductDAO.find_many_in_subcategory(subcategory_id=subcategory_id, limit=limit + 1)
    assert (len(expected_products) > expected_count) == has_more
        
#2
@pytest.mark.asyncio
@pytest.mark.parametrize("parent_category_id, limit, expected_count, has_more", [
    (5,1,1,True),
    (4,1,1,True),
    (6,1,0,False),
    (3,1,0,False),
])
async def test_get_products_in_parent_category(
    parent_category_id: int, 
    limit: int, 
    expected_count: int, 
    has_more: bool,                                                                   
    ac: AsyncClient
    ):
    response = await ac.get(f"/product/parent_category/{parent_category_id}", params={
        "limit":limit
    })
    products = response.json()
    
    assert response.status_code == 200
    assert len(products["products"]) == expected_count
    
    if expected_count > 0:
        for product in products["products"]:
            try:
                product_data = {
                    'id': product["id"],
                    'name': product["name"],
                    'description': product["description"],
                    'img': product["img"],
                }
                
                product_schem = SProducts(**product_data)

                assert isinstance(product_schem.id, UUID)
                assert isinstance(product_schem.name, str)
                assert isinstance(product_schem.description, str)
                assert isinstance(product_schem.img, str)
                
            except ValidationError as e:
                assert False, f"Validation Error: {e}"
            except TypeError as e:
                assert False, f"Type Error: {e}"

    expected_products = await ProductDAO.find_many_in_parent_category(parent_category_id=parent_category_id, limit=limit + 1)
    assert (len(expected_products) > expected_count) == has_more
        
        
#3 
@pytest.mark.asyncio      
@pytest.mark.parametrize("product_name,is_exists", [
    ("Продукт1", True),
    ("Продукт2", True),
    ("Продукт", True),
    ("П", True),
    ("П", True),
    ("Й", False),
    ("нанана", False)
])        
async def test_product_search(product_name: str, is_exists: bool, ac: AsyncClient):
    response = await ac.get("/product/search", params={"product_name": product_name})
    
    products = response.json()
    assert response.status_code == 200
    
    if is_exists:
        assert products  
        
        for product in products:
            product_data = {
                "id": product["id"],     
                "name": product["name"],
                "img": product["img"]
            }
            
            try:
                product_schem = SProductSearch(**product_data)  
                
                assert isinstance(product_schem.id, UUID)
                assert isinstance(product_schem.name, str)
                assert isinstance(product_schem.img, str)

            except ValidationError as e:
                assert False, f"Validation Error for product {product_data}: {e}"

    else:
        assert products == []
        
#4     
@pytest.mark.asyncio   
@pytest.mark.parametrize("product_id,if_exists", [
    ("1364c781-47d0-4d02-8eef-798630816b8e",True),
    ("680c7a49-bcbc-4241-8330-788b2f001555",True),
    ("680c7a49-bcbc-4241-8330-788b2f001556",False),
    ("680c7a49-bcbc-4241-8330-788b2f001557",False),
])        
async def test_product_api_detail(product_id: str, if_exists: bool, ac: AsyncClient):
    response = await ac.get(f"/product/detail/{product_id}")
    product = response.json()
    
    if if_exists:
        assert product
        try:
            product_data = {
                    "id": product["id"],
                    "name": product["name"],
                    "description": product["description"],
                    "img": product["img"]
                    }
            product_schema = SProducts(**product_data)
            
            assert isinstance(product_schema.id, UUID)
            assert isinstance(product_schema.name, str)
            assert isinstance(product_schema.description, str)
            assert isinstance(product_schema.img, str)
            
        except ValidationError as e:
                assert False, f"Validation Error: {e}"
        except TypeError as e:
                assert False, f"Type Error: {e}"
    else: 
        assert product is None