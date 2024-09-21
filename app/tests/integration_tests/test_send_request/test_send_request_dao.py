import pytest

from app.email.send_request.dao import SendRequestDAO


@pytest.mark.parametrize("id,lastname,firstname_and_surname,number,organization,email,message", [
    (5,"Голузин","Иван Александрович","+79226402325","ООО Крутые","ivan@mail.ru","awdadwaadad adawd adw"),
    (6,"Петров","Петр Александрович","+79676402378","ООО Крутые2","petr@mail.ru","awdadwaadad 45444adawd adw")
])
async def test_order_call_add(id:int,lastname:str,firstname_and_surname:str,number:str,organization:str,email:str,message:str):
    new_send_request = await SendRequestDAO.add(id=id,
    lastname=lastname,
    firstname_and_surname=firstname_and_surname,
    number=number,
    organization=organization,
    email=email,
    message=message
    )
    
    assert new_send_request.id == id
    
    new_send_request = await SendRequestDAO.find_one_or_none(id=new_send_request.id)
    
    assert new_send_request is not None