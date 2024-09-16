from fastapi import HTTPException, status
from app.exceptions.base import BaseException

class UserExit(BaseException):
    status_code = status.HTTP_200_OK
    detail = "Пользователь вышел из системы"

class UsersRegisterOK(BaseException):
    status_code = status.HTTP_201_CREATED
    detail = "Пользователь зарегистрирован"

class UserAlreadyExistsException(BaseException):
    status_code=status.HTTP_409_CONFLICT
    detail="Пользователь уже существует"
        
class IncorrectEmailOrPasswordException(BaseException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Неверная почта или пароль"
        
class TokenExpiredException(BaseException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Срок действия токена истек"
        
class TokenAbsentException(BaseException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Токен отсутствует"
        
class IncorrectTokenFormatException(BaseException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Неверный формат токена"
        
class UserIsNotPresentException(BaseException):
    status_code=status.HTTP_401_UNAUTHORIZED

class RoomFullyBooked(BaseException):
    status_code=status.HTTP_409_CONFLICT
    detail="Не осталось свободных номеров"

class RoomCannotBeBooked(BaseException):
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    detail="Не удалось забронировать номер ввиду неизвестной ошибки"

class DateFromCannotBeAfterDateTo(BaseException):
    status_code=status.HTTP_400_BAD_REQUEST
    detail="Дата заезда не может быть позже даты выезда"

class CannotBookHotelForLongPeriod(BaseException):
    status_code=status.HTTP_400_BAD_REQUEST
    detail="Невозможно забронировать отель сроком более месяца"

class CannotAddDataToDatabase(BaseException):
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    detail="Не удалось добавить запись"

class CannotProcessCSV(BaseException):
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    detail="Не удалось обработать CSV файл"