from fastapi import APIRouter, Request

from app.email.order_call.dao import OrderCallDAO
from app.email.order_call.schemas import SOrderCall
from app.exceptions.ordercall.exceptions import OrderCallAccept
from app.exceptions.schemas import SException
from app.tasks.tasks import send_email_call
from app.utils.limiter import limiter

router = APIRouter(prefix="/callorder", tags=["Заказать звонок"])


@router.post("/add")
@limiter.limit("3/minute", error_message="Слишком много обращений, повторите попытку позже")
async def add_callorder(order: SOrderCall, request: Request) -> SException:
    await OrderCallDAO.add(name=order.name,number=order.number,comment=order.comment)
    send_email_call.delay(name=order.name,number=order.number,comment=order.comment)
    raise OrderCallAccept
    