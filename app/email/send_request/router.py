from fastapi import APIRouter

from app.email.send_request.dao import SendRequestDAO
from app.email.send_request.schemas import SSendRequest
from app.exceptions.schemas import SException
from app.exceptions.sendrequest.exceptions import SendRequestAccept
from app.tasks.tasks import send_email_request

router = APIRouter(prefix="/sendrequest", tags=["Создать заявку"])


@router.post("/add")
async def add_sendrequest(order: SSendRequest) -> SException:
    await SendRequestDAO.add(
        lastname=order.lastname,
        firstname_and_surname=order.firstname_and_surname,
        number=order.number,
        organization=order.organization,
        email=order.email,
        message=order.message
    )
    send_email_request.delay(
        lastname=order.lastname,
        firstname_and_surname=order.firstname_and_surname,
        number=order.number,
        organization=order.organization,
        email=order.email,
        message=order.message
    )
    raise SendRequestAccept