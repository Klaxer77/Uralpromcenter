from app.database import Base
from sqlalchemy import Column, Integer,String


class Progress(Base):
    __tablename__ = "progress"
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    img = Column(String, nullable=False, unique=True)