from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from app.models.user_model import User
from app.schemas.user_schema import UserCreate
from typing import List, Optional

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserCreate) -> User:
        db_user = User(
            full_name=user.full_name,
            email=user.email,
            aadhaar_application_id=user.aadhaar_application_id,
            phone_number=user.phone_number,
            address=user.address,
            dob=user.dob
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter(User.email == email).first()

    def get_user_by_aadhaar_id(self, aadhaar_id: int) -> Optional[User]:
        return self.db.query(User).filter(User.aadhaar_application_id == aadhaar_id).first()

    def get_users(self, skip: int = 0, limit: int = 10, sort_by: str = "id", sort_order: str = "asc") -> List[User]:
        query = self.db.query(User)
        
        # I'm using this to sort by whatever column the user asks for. I check if the column exists first so the app doesn't break.
        if hasattr(User, sort_by):
            column = getattr(User, sort_by)
            if sort_order.lower() == "desc":
                query = query.order_by(desc(column))
            else:
                query = query.order_by(asc(column))
        else:
            query = query.order_by(User.id)

        return query.offset(skip).limit(limit).all()
    
    def count_users(self) -> int:
        return self.db.query(User).count()
