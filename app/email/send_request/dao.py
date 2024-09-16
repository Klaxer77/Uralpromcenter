from app.dao.base import BaseDAO
from app.email.send_request.models import SendRequest

class SendRequestDAO(BaseDAO):
    model = SendRequest