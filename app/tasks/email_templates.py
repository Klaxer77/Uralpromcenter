from email.message import EmailMessage
from app.config import settings
from pydantic import EmailStr

def create_message_template_call(
    name: str,
    number: str,
    comment: str,
    email_to: EmailStr
):
    email = EmailMessage()
    email['subject'] = 'Заказ звонка'
    email['from'] = settings.SMTP_USER
    email['To'] = email_to
    
    email.set_content(
        f"""
        <h1>Заказ звонка</h1>
        Имя: {name}
        Номер: {number}
        Комментарий: {comment}
        """,
        subtype='html'
    )
    return email


def create_message_template_request(
    lastname: str,
    firstname_and_surname: str,
    number: str,
    organization: str,
    email: EmailStr,
    message: str,
    email_to: EmailStr
):
    email_lib = EmailMessage()
    email_lib['subject'] = 'Новая заявка'
    email_lib['from'] = settings.SMTP_USER
    email_lib['To'] = email_to
    
    email_lib.set_content(
        f"""
        <h1>Заявка</h1>
        Организация: {organization}
        Имя и отчество: {firstname_and_surname}
        Фамилия: {lastname}
        Номер: {number}
        Email: {email}
        Сообщение: {message}
        """,
        subtype='html'
    )
    return email_lib
    
