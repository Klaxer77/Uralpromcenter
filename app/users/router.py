from uuid import UUID
from fastapi import APIRouter, Depends, Response

from app.exceptions.schemas import SException
from app.exceptions.users.exceptions import (
    CannotAddDataToDatabase,
    UserAlreadyExistsException,
    UserExit,
    UsersRegisterOK,
)
from app.users.auth import get_password_hash
from app.users.dao import UsersDAO
from app.users.dependencies import get_current_user
from app.users.schemas import SUserAuth
from app.config import settings

router_auth = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

if settings.MODE in ["DEV","TEST"]:
    @router_auth.post("/register")
    async def register_user(user_data: SUserAuth) -> SException:
        existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
        if existing_user:
            raise UserAlreadyExistsException
        hashed_password = get_password_hash(user_data.password)
        new_user = await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)
        if not new_user:
            raise CannotAddDataToDatabase
        raise UsersRegisterOK


