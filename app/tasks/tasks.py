import smtplib
from pydantic import EmailStr
from app.config import settings
from app.tasks.celery import celery

from app.tasks.email_templates import create_message_template_call, create_message_template_request

@celery.task
def send_email_call(
    name: str,
    number: str,
    comment: str
):
    email_to = settings.SMTP_USER
    msg_content = create_message_template_call(name, number, comment, email_to)
    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)
        
        
@celery.task
def send_email_request(
    lastname: str,
    firstname_and_surname: str,
    number: str,
    organization: str,
    email: EmailStr,
    message: str
):
    email_to = settings.SMTP_USER
    msg_content = create_message_template_request(
        lastname,
        firstname_and_surname,
        number,
        organization,
        email,
        message,
        email_to
    )
    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)