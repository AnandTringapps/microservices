from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class User(UserCreate):
    id: int

    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    name: str
    description: str
    price: int

class Product(ProductCreate):
    id: int

    class Config:
        orm_mode = True