import pytest 
from httpx import AsyncClient
from app.exceptions.schemas import SException


@pytest.mark.parametrize("name,number,comment,detail,status_code", [
    ("Иван","+79226402325","фцвффцвфвфвфцвфцвфвфцвф","Спасибо за заявку! Мы свяжемся с вами в ближайшее время",201),
    ("Иван","+79226402325","фцвффцвфвфвфцвфцвфвфцвф","Спасибо за заявку! Мы свяжемся с вами в ближайшее время",201),
    ("Дмитрий","+77825602325","фцвффцвфвфвфцвфцвфвфцвф 4545 4545 аыыуа 556","Спасибо за заявку! Мы свяжемся с вами в ближайшее время",201),
    ("Дмитрий","+77825602325","awdadawdawdadad","Rate limit exceeded: Слишком много обращений, повторите попытку позже",429),
    ("Дмитрий","+778256023","фцвффцвфвфвфцвфцвфвфцвф 4545 4545 аыыуа 556","Номер телефона должен начинаться с '+' и содержать 12 цифр (включая код страны)",422),
    ("Дмитрийфцвввввввввввввввввввввввввввввввввввввввввввввввввввввввввввввввввввввввв","+77825602345","фцвффцвфвфвфцвфцвфвфцвф 4545 4545 аыыуа 556","Слишком много символов в имени",422)
])
async def test_api_order_call_add(name:str,number:str,comment:str,detail:str,status_code:int,ac: AsyncClient):
    response = await ac.post("/api/callorder/add", json={
        "name":name,
        "number":number,
        "comment":comment 
    })
    
    assert response.status_code == status_code
    if response.status_code == 429:
        assert response.json()["error"] == detail
    elif str(status_code).startswith("4"):
        assert response.json()["detail"] == detail
    