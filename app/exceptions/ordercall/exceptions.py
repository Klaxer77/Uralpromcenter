from app.exceptions.base import BaseException
from fastapi import status


class OrderCallAccept(BaseException):
    status_code = status.HTTP_201_CREATED
    detail = "Спасибо за заявку! Мы свяжемся с вами в ближайшее время"