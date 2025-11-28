from fastapi import FastAPI
from app.routers import user_router
from app.database import engine, Base
from app.config import settings

# I'm creating tables automatically here to keep things simple. In a real job, I'd use a proper migration tool like Alembic.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(user_router.router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    return {"message": "Welcome to Aadhaar Service API"}
