import pytest

from app.email.order_call.dao import OrderCallDAO


@pytest.mark.parametrize("id,name,number,comment", [
    (5,"Иван","+79226402325","фцвффцвфвфвфцвфцвфвфцвф"),
    (6,"Дмитрий","+77825602325","фцвффцвфвфвфцвфцвфвфцвф 4545 4545 аыыуа 556")
])
async def test_order_call_add(id:int,name:str,number:str,comment:str):
    new_order_call = await OrderCallDAO.add(id=id,name=name,number=number,comment=comment)
    
    
    assert new_order_call.id == id
    
    new_order_call = await OrderCallDAO.find_one_or_none(id=new_order_call.id)
    
    assert new_order_call is not None
    
    
    
    