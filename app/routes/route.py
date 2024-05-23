from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.CRUD import CRUD, Product,User
from typing import Optional

router = APIRouter()

@router.get("/users", response_model=list[User])
async def get_users(db: Session = Depends(get_db)):
    return CRUD(db).get_users()

@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = CRUD(db).get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users", response_model=User)
async def create_user(user: User, db: Session = Depends(get_db)):
    created_user = CRUD(db).create_user(user)
    if not created_user:
        raise HTTPException(status_code=400, detail="Failed to create user")
    return created_user


@router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    if CRUD(db).delete_user(user_id):
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=400, detail="Failed to delete user")

# Product Routes
@router.get("/products", response_model=list[Product])
async def get_products(db: Session = Depends(get_db)):
    return CRUD(db).get_products()

@router.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int, db: Session = Depends(get_db)):
    user = CRUD(db).get_product(product_id)  # Typo fixed (user -> product)
    if not user:
        raise HTTPException(status_code=404, detail="Product not found")
    return user

@router.post("/products", response_model=Product)
async def create_product(product: Product, db: Session = Depends(get_db)):
    created_product = CRUD(db).create_product(product)
    if not created_product:
        raise HTTPException(status_code=400, detail="Failed to create product")
    return created_product


@router.patch("/users/{user_id}")
def update_user(user_id: int, name: Optional[str] = None, self=None):
    user = self.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")

    try:
        if name is not None:
            user.name = name
        self.db.commit()
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating user: {e}")


@router.patch("/products/{product_id}")
def update_product(product_id: int, name: Optional[str] = None, self=None):
    product = self.get_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found")

    try:
        if name is not None:
            product.name = name
        self.db.commit()
        return product
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating product: {e}")

@router.delete("/products/{product_id}")
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    if CRUD(db).delete_product(product_id):
        return {"message": "Product deleted successfully"}
    raise HTTPException(status_code=400, detail="Failed to delete product")