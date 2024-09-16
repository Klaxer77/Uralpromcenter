import pytest
from uuid import UUID
from pydantic import ValidationError
from app.products.schemas import SProductsList, SCategory, SSubcategory
from app.products.dao import ProductDAO


#1
async def test_get_products_all():
    products = await ProductDAO.get_products_all()
    
    assert products
    
    for product in products:
        try:
            product_data = {
                'id': product.id,
                'name': product.name,
                'img': product.img,
                'subcategories': [
                    {
                        'id': subcategory.id,
                        'name': subcategory.name,
                        'parent_category': {
                            'id': subcategory.parent_category.id,
                            'name': subcategory.parent_category.name
                        } if subcategory.parent_category else None
                    } for subcategory in product.subcategories
                ] if product.subcategories else []
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
                'img': product.img,
                'subcategories': [
                    {
                        'id': subcategory.id,
                        'name': subcategory.name,
                        'parent_category': {
                            'id': subcategory.parent_category.id,
                            'name': subcategory.parent_category.name
                        } if subcategory.parent_category else None
                    } for subcategory in product.subcategories
                ] if product.subcategories else []
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
                'img': product.img,
                'subcategories': [
                    {
                        'id': subcategory.id,
                        'name': subcategory.name,
                        'parent_category': {
                            'id': subcategory.parent_category.id,
                            'name': subcategory.parent_category.name
                        } if subcategory.parent_category else None
                    } for subcategory in product.subcategories
                ] if product.subcategories else []
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
        

        
        
    
