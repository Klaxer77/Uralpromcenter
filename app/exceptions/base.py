from fastapi import HTTPException, status


class BaseException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)
        
        
class ServerError(BaseException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Ошибка сервера"
    

class NumberError(BaseException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Номер телефона должен начинаться с '+' и содержать 12 цифр (включая код страны)"
    
class ValueLenError(BaseException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Слишком много символов"