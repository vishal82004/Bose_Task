from pydantic import BaseModel, EmailStr, Field
from datetime import date, datetime
from typing import Optional, List

class UserBase(BaseModel):
    full_name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    # Since this is a number now, I used "greater than" and "less than" to make sure it's exactly 12 digits long.
    aadhaar_application_id: int = Field(..., ge=100000000000, le=999999999999) 
    phone_number: int = Field(..., ge=1000000000, le=999999999999999) 
    address: Optional[str] = None
    dob: date

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class PaginatedUserResponse(BaseModel):
    data: List[UserResponse]
    total: int
    page: int
    page_size: int
    total_pages: int
