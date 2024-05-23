from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = BaseModel
class Product(Base):
    __tablename__ = "products"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, index=True)
    owner_id: int = Column(Integer, ForeignKey("users.id"))
    owner: 'User' = relationship("User", back_populates="products")

class User(Base):
    __tablename__ = "users"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, index=True)
    products: list[Product] = relationship("Product", back_populates="owner")
