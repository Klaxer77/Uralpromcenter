import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("lastname,firstname_and_surname,number,organization,email,message,detail,status_code", [
    ("Голузин","Иван Александрович","+79226402325","ООО Крутые","ivan@mail.ru","awdadwaadad adawd adw","Спасибо за заявку! Мы свяжемся с вами в ближайшее время",201),
    ("Петров","Петр Александрович","+79676402378","ООО Крутые2","petr@mail.ru","awdadwaadad 45444adawd adw","Спасибо за заявку! Мы свяжемся с вами в ближайшее время",201),
    ("Петров","Петр Александрович","+79676402378","ООО Крутые2","petr@mail.ru","awdadwaadad 45444adawd adw","Спасибо за заявку! Мы свяжемся с вами в ближайшее время",201),
    ("Петров","Петр Александрович","+79676402378","ООО Крутые2","petr@mail.ru","awdadwaadad 45444adawd adw","Rate limit exceeded: Слишком много обращений, повторите попытку позже",429),
    ("Петров","Петр Александрович","+796764023","ООО Крутые2","petr@mail.ru","awdawdawdwad adwdawdad aw awdawdwad awd ad w d","Номер телефона должен начинаться с '+' и содержать 12 цифр (включая код страны)",422),
    ("Петров","Петр Александрович","+79676402378","ООО Крутые2цфвввввввввввввввввввввввввввввввввввввввввввввввввввввввввввввв","petr@mail.ru","awdadwaadad 45444adawd adw","Слишком много символов в поле организации",422),
    ("Петровфцвввввввввввввввввввввввввввввввввввввввввввввввввввввввв","Петр Александрович","+79676402378","ООО Крутые2","petr@mail.ru","awdadwaadad 45444adawd adw","Слишком много символов в поле фамилии",422),
    ("Петров","Петр Александровичвфцццццццццццццццццццццццццццццццццццццццццццццццццццццццццццц","+79676402378","ООО Крутые2","petr@mail.ru","awdadwaadad 45444adawd adw","Слишком много символов в поле имени с отчеством",422)
])
async def test_api_send_request_add(
    lastname:str,
    firstname_and_surname:str,
    number:str,
    organization:str,
    email:str,
    message:str,
    detail:str,
    status_code:int,
    ac:AsyncClient
):
    response = await ac.post("/api/sendrequest/add", json={
        "lastname":lastname,
        "firstname_and_surname":firstname_and_surname,
        "number":number,
        "organization":organization,
        "email":email,
        "message":message
    })
    
    assert response.status_code == status_code
    
    if response.status_code == 429:
        assert response.json()["error"] == detail
    elif str(status_code).startswith("4"):
        assert response.json()["detail"] == detail