from app.database import Base
from sqlalchemy import Column, Integer, String, Text


class OrderCall(Base):
    __tablename__ = "order_call"
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(255), nullable=False)
    number = Column(String(15), nullable=False)
    comment = Column(String(255), nullable=False)
    
    

