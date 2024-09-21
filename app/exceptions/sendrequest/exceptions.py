from app.exceptions.base import BaseException
from fastapi import status


class SendRequestAccept(BaseException): 
    status_code = status.HTTP_201_CREATED
    detail = "Спасибо за заявку! Мы свяжемся с вами в ближайшее время"
    
    
class SendRequestOrganizationError(BaseException): 
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Слишком много символов в поле организации"
    
class SendRequestLastNameError(BaseException): 
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Слишком много символов в поле фамилии"
    
    
class SendRequestFirtsNameANDLastNameError(BaseException): 
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Слишком много символов в поле имени с отчеством"