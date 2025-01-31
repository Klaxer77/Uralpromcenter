import pytest
from uuid import UUID
from pydantic import ValidationError
from app.products.schemas import SProductSearch, SProducts, SProductsList, SCategory, SSubcategory
from app.products.dao import ProductDAO

#1
@pytest.mark.asyncio
@pytest.mark.parametrize("subcategory_id, limit, expected_count, has_more", [
    (1, 1, 1, True), 
    (2, 1, 1, True),  
    (3, 1, 0, False),  
    (4, 1, 0, False),  
    (5, 1, 0, False)   
])
async def test_find_many_in_subcategory(subcategory_id: int, limit: int, expected_count: int, has_more: bool):
    response = await ProductDAO.find_many_in_subcategory(subcategory_id=subcategory_id, limit=limit)

    assert len(response) == expected_count
    
    if expected_count > 0:
        for product in response:
            try:
                product_data = {
                    'id': product.id,
                    'name': product.name,
                    'description': product.description,
                    'img': product.img,
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
@pytest.mark.parametrize("parent_category_id, limit, expected_count, has_more", [
    (4,1,1,True),
    (5,1,1,True),
    (1,1,0,False),
    (2,1,0,False),
    (3,1,0,False),
])
async def test_find_many_in_parent_category(parent_category_id: int, limit: int, expected_count: int, has_more: bool):
    response = await ProductDAO.find_many_in_parent_category(parent_category_id=parent_category_id, limit=limit)
    
    assert len(response) == expected_count
    
    if expected_count > 0:
        for product in response:
            try:
                product_data = {
                    'id': product.id,
                    'name': product.name,
                    'description': product.description,
                    'img': product.img,
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
@pytest.mark.parametrize("product_name,is_exists",[
    ("Продукт1",True),
    ("Продукт2",True),
    ("Продукт",True),
    ("П",True),
    ("П",True),
    ("Й",False),
    ("нанана",False)
])
async def test_product_search(product_name: str, is_exists: bool):
    products = await ProductDAO.search(product_name=product_name)
    
    if is_exists:
        assert products
        
        for product in products:
            try:
                product_data = {
                        "id": product.id,
                        "name": product.name,
                        "img": product.img
                        }
            
                product_schem = SProductSearch(**product_data)
                
                assert isinstance(product_schem.id, UUID)
                assert isinstance(product_schem.name, str)
                assert isinstance(product_schem.img, str)
            except ValidationError as e:
                assert False, f"Validation Error: {e}"
            except TypeError as e:
                assert False, f"Type Error: {e}"
    
    else:
        assert products == []

#4     
@pytest.mark.parametrize("product_id,if_exists", [
    ("1364c781-47d0-4d02-8eef-798630816b8e",True),
    ("680c7a49-bcbc-4241-8330-788b2f001555",True),
    ("680c7a49-bcbc-4241-8330-788b2f001556",False),
    ("680c7a49-bcbc-4241-8330-788b2f001557",False),
])   
async def test_product_detail(product_id: UUID,if_exists: bool):
    product = await ProductDAO.find_one_or_none(id=product_id)
    
    if if_exists:
        assert product
        try:
            product_schema = SProducts(**product)
            
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
        

        
        
    
