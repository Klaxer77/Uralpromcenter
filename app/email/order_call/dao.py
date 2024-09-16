from app.dao.base import BaseDAO
from app.email.order_call.models import OrderCall

class OrderCallDAO(BaseDAO):
    model = OrderCall