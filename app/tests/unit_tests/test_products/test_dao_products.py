import pytest
from uuid import UUID
from pydantic import ValidationError
from app.products.schemas import SProductSearch, SProductsList, SCategory, SSubcategory
from app.products.dao import ProductDAO

#1
@pytest.mark.parametrize("subcategory_id,limit,is_exists", [
    (1,2,True),
    (2,1,True),
    (3,1,False),
    (4,1,False),
    (5,1,False)
])
async def test_find_many_in_subcategory(subcategory_id: int, limit: int, is_exists: bool):
    products = await ProductDAO.find_many_in_subcategory(subcategory_id=subcategory_id,limit=limit)
    
    if is_exists:
        assert products
        assert len(products) == limit
        for product in products:
            try:
                product_data = {
                'id': product.id,
                'name': product.name,
                'img': product.img,
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
    (4,1,True),
    (5,1,True),
    (1,1,False),
    (2,1,False),
    (3,1,False),
])
async def test_find_many_in_parent_category(parent_category_id: int, limit: int, is_exists: bool):
    products = await ProductDAO.find_many_in_parent_category(parent_category_id=parent_category_id,limit=limit)
    
    if is_exists:
        assert products
        assert len(products) == limit
        for product in products:
            try:
                product_data = {
                'id': product.id,
                'name': product.name,
                'img': product.img,
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
        

        
        
    
