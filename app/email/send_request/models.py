from app.database import Base
from sqlalchemy import Column, Integer, String, Text


class SendRequest(Base):
    __tablename__ = "send_request"
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    lastname = Column(String(255), nullable=False)
    firstname_and_surname = Column(String(255), nullable=False)
    number = Column(String(15), nullable=False)
    organization = Column(String(15), nullable=False)
    email = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)
    
    def __str__(self) -> str:
        return f"Зявка от {self.organization}"