from sqlalchemy.orm import Session
from app.repositories.user_repo import UserRepository
from app.schemas.user_schema import UserCreate
from app.models.user_model import User
from typing import List, Optional

class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def create_user(self, user_data: UserCreate) -> User:
        # I'm checking for duplicates here so I can give a clear error message, instead of letting the database crash.
        if self.repo.get_user_by_email(user_data.email):
            raise ValueError("Email already registered")
        
        if self.repo.get_user_by_aadhaar_id(user_data.aadhaar_application_id):
            raise ValueError("Aadhaar Application ID already exists")

        return self.repo.create_user(user_data)

    def get_user(self, aadhaar_id: int) -> Optional[User]:
        return self.repo.get_user_by_aadhaar_id(aadhaar_id)

    def list_users(self, page: int = 1, page_size: int = 10, sort_by: str = "id", sort_order: str = "asc") -> dict:
        # I'm limiting these numbers so people can't ask for negative pages or too much data at once.
        if page < 1:
            page = 1
        if page_size < 1:
            page_size = 10
        if page_size > 100:
            page_size = 100

        skip = (page - 1) * page_size
        users = self.repo.get_users(skip=skip, limit=page_size, sort_by=sort_by, sort_order=sort_order)
        total = self.repo.count_users()

        return {
            "data": users,
            "total": total,
            "page": page,
            "page_size": page_size,
            "total_pages": (total + page_size - 1) // page_size
        }
