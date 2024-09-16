from app.database import Base
from sqlalchemy import Column, Integer,String


class Recall(Base):
    __tablename__ = "recall"
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    img = Column(String, nullable=False, unique=True)