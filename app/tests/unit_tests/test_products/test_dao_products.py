import pytest
from uuid import UUID
from pydantic import ValidationError
from app.products.schemas import SProductSearch, SProductsList, SCategory, SSubcategory
from app.products.dao import ProductDAO

#1
@pytest.mark.parametrize("subcategory_id,is_exists", [
    (1,True),
    (2,True),
    (3,False),
    (4,False),
    (5,False)
])
async def test_find_many_in_subcategory(subcategory_id: int, is_exists: bool):
    products = await ProductDAO.find_many_in_subcategory(subcategory_id=subcategory_id)
    
    if is_exists:
        assert products
        for product in products:
            try:
                product_data = {
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'img': product.img,
            }
                
                product_schem = SProductsList(**product_data)

                assert isinstance(product_schem.id, UUID)
                assert isinstance(product_schem.name, str)
                assert isinstance(product_schem.description, str)
                assert isinstance(product_schem.img, str)
                
            except ValidationError as e:
                assert False, f"Validation Error: {e}"
            except TypeError as e:
                assert False, f"Type Error: {e}"
    else: 
        assert products == []
        

#2
@pytest.mark.parametrize("parent_category_id,is_exists", [
    (4,True),
    (5,True),
    (1,False),
    (2,False),
    (3,False),
])
async def test_find_many_in_parent_category(parent_category_id: int, is_exists: bool):
    products = await ProductDAO.find_many_in_parent_category(parent_category_id=parent_category_id)
    
    if is_exists:
        assert products
        for product in products:
            try:
                product_data = {
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'img': product.img,
            }
                
                product_schem = SProductsList(**product_data)

                assert isinstance(product_schem.id, UUID)
                assert isinstance(product_schem.name, str)
                assert isinstance(product_schem.description, str)
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
async def test_product_search(product_name: str, is_exists: bool):
    products = await ProductDAO.search(product_name=product_name)
    
    if is_exists:
        assert products
        
        for product in products:
            product_data = {
                    "name": product.name,
                    "img": product.img
                    }
        
        product_schem = SProductSearch(**product_data)
        
        assert isinstance(product_schem.name, str)
        assert isinstance(product_schem.img, str)
    
    else:
        assert products == []
        

        
        
    
