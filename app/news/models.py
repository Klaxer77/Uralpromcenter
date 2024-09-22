from datetime import date
from sqlalchemy import Column, Integer, Text, String, Date, func
from app.database import Base
from sqlalchemy.orm import relationship, Mapped

class News(Base):
    __tablename__ = "news"
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(255), nullable=False)
    title = Column(Text, nullable=False)
    text = Column(Text, nullable=False)
    img = Column(String(255), nullable=False)
    created_at = Column(
        Date, default=date.today, server_default=func.current_date(), nullable=False
    )
    
    def __str__(self):
        return f"Новость: {self.name}"