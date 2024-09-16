from fastapi import status
from app.exceptions.base import BaseException


class CategoryValidate(BaseException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Категория не может быть 0"
    
    
class NoneCategory(BaseException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Такой категории не существует"
    
    
class CategoryCreated(BaseException):
    status_code = status.HTTP_201_CREATED
    detail = "Категория создана"