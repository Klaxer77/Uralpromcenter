from fastapi import status
from app.exceptions.base import BaseException


class ProductCreated(BaseException):
    status_code = status.HTTP_201_CREATED
    detail = "Продукт добавлен"
    
class ProductNameException(BaseException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Продукт с таким названием уже существует"
    
class ProductImgException(BaseException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Продукт с таким изображением уже существует"