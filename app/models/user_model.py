from sqlalchemy import Column, Integer, String, Date, DateTime, Text, BigInteger
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    # I used BigInteger because a normal Integer is too small for a 12-digit Aadhaar number.
    aadhaar_application_id = Column(BigInteger, unique=True, index=True, nullable=False)
    phone_number = Column(String, nullable=False)
    address = Column(Text, nullable=True)
    dob = Column(Date, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
