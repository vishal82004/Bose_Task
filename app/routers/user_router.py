from fastapi import APIRouter, Depends, HTTPException, Query, status
from app.schemas.user_schema import UserCreate, UserResponse, PaginatedUserResponse
from app.services.user_service import UserService
from app.dependencies import get_user_service
from typing import List, Optional

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(
    user: UserCreate, 
    service: UserService = Depends(get_user_service)
):
    try:
        return service.create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{aadhaar_id}", response_model=UserResponse)
def read_user(
    aadhaar_id: int, 
    service: UserService = Depends(get_user_service)
):
    user = service.get_user(aadhaar_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=PaginatedUserResponse) 
def list_users(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(10, ge=1, le=100, description="Items per page"),
    sort_by: str = Query("id", description="Field to sort by"),
    sort_order: str = Query("asc", regex="^(asc|desc)$", description="Sort order (asc/desc)"),
    service: UserService = Depends(get_user_service)
):
    return service.list_users(page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order)
