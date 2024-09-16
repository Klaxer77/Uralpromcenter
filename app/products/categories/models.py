import uuid
from sqlalchemy import Column, UUID, Boolean, ForeignKey, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship, Mapped


class Categories(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    parent_category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    
    parent_category = relationship(
        "Categories", 
        remote_side=[id],
        backref="subcategories",
        single_parent=True
    )
    
    products = relationship(
        "Products",
        secondary="products_categories",
        back_populates="subcategories"
    )
    
    
    def __str__(self):
        return f"Категория: {self.name}"
    
    
