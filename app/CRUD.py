from app.models.models import User, Product
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.orm import Session
from typing import Optional

class CRUD:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: User):
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:

            print(f"Error creating user: {e.__cause__}")
            return None
        except Exception as e:
            print(f"Unexpected error creating user: {e}")
            return None

    def get_user(self, user_id: int):
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            return user
        except NoResultFound:
            print(f"User with id {user_id} not found")
            return None
        except Exception as e:
            print(f"Unexpected error getting user: {e}")
            return None

    def get_users(self):
        return self.db.query(User).all()

    def delete_user(self, user_id: int):
        user = self.get_user(user_id)
        if user:
            try:
                self.db.delete(user)
                self.db.commit()
                return True
            except Exception as e:
                print(f"Error deleting user: {e}")
                return False
        print(f"User with id {user_id} not found")
        return False

    def create_product(self, product: Product):
        try:
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            return product
        except IntegrityError as e:
            print(f"Error creating product: {e.__cause__}")
            return None
        except Exception as e:
            print(f"Unexpected error creating product: {e}")
            return None

    def get_product(self, product_id: int):
        try:
            product = self.db.query(Product).filter(Product.id == product_id).first()
            return product
        except NoResultFound:
            print(f"Product with id {product_id} not found")
            return None
        except Exception as e:
            print(f"Unexpected error getting product: {e}")
            return None

    def get_products(self):
        return self.db.query(Product).all()

    def update_user(self, user_id: int, name: Optional[str] = None):
        user = self.get_user(user_id)
        if user:
            try:
                if name is not None:
                    user.name = name
                self.db.commit()
                return user
            except Exception as e:
                print(f"Error updating user: {e}")
                return None
        print(f"User with id {user_id} not found")
        return None

    def update_product(self, product_id: int, name: Optional[str] = None):
        product = self.get_product(product_id)
        if product:
            try:
                if name is not None:
                    product.name = name
                self.db.commit()
                return product
            except Exception as e:
                print(f"Error updating product: {e}")
                return None
        print(f"Product with id {product_id} not found")
        return None

    def delete_product(self, product_id: int):
        product = self.get_product(product_id)
        if product:
            try:
                self.db.delete(product)
                self.db.commit()
                return True
            except Exception as e:
                print(f"Error deleting product: {e}")
                return False
        print(f"Product with id {product_id} not found")
        return False

