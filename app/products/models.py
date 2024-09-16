import uuid
from sqlalchemy import Column, UUID, Boolean, ForeignKey, Integer, String, Table
from app.database import Base
from sqlalchemy.orm import relationship, Mapped


products_categories = Table(
    "products_categories",
    Base.metadata,
    Column("product_id", UUID(as_uuid=True), ForeignKey("products.id"), primary_key=True),
    Column("category_id", Integer, ForeignKey("categories.id"), primary_key=True)
)


class Products(Base):
    __tablename__ = "products"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), unique=True, nullable=False)
    img = Column(String(255), unique=True, nullable=False)
    
    subcategories = relationship(
        "Categories",
        secondary=products_categories,
        back_populates="products"
    )
    
    
    def __str__(self):
        return f"{self.name}"

