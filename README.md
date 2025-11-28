# Aadhaar Service Backend

Backend service for managing Aadhaar applicant details.

## Project Structure

```
aadhaar-service/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Application Entry Point
│   ├── config.py               # Environment Configuration
│   ├── database.py             # DB Connection & Session Management
│   ├── dependencies.py         # Dependency Injection
│   ├── routers/                # API Layer
│   │   ├── __init__.py
│   │   └── user_router.py      # User Endpoints
│   ├── schemas/                # Pydantic Models
│   │   ├── __init__.py
│   │   └── user_schema.py
│   ├── services/               # Business Logic Layer
│   │   ├── __init__.py
│   │   └── user_service.py
│   ├── repositories/           # Data Access Layer
│   │   ├── __init__.py
│   │   └── user_repo.py
│   └── models/                 # SQLAlchemy Models
│       ├── __init__.py
│       └── user_model.py
├── schema.sql                  # SQL Schema
└── README.md                   # Documentation
```

## Prerequisites

- Python 3.9+
- PostgreSQL
- pip

## Setup

1.  **Clone the repository** (if applicable)

2.  **Create a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**
    ```bash
    pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic-settings
    ```

4.  **Configure Environment**
    Create a `.env` file in the root directory (or set environment variables):
    ```
    DATABASE_URL=postgresql://user:password@localhost:5432/aadhaar_db
    ```

5.  **Run the Application**
    ```bash
    uvicorn app.main:app --reload
    ```

## API Endpoints

-   **POST /api/v1/users/**: Create a new user.
-   **GET /api/v1/users/{aadhaar_application_id}**: Retrieve a user by aadhaar application ID.
-   **GET /api/v1/users/**: List users with pagination and sorting.
    -   Query Params: `page`, `page_size`, `sort_by`, `sort_order`

## Features

-   **Layered Architecture**: Separation of concerns (Router -> Service -> Repository -> Model).
-   **Validation**: Pydantic models ensure data integrity.
-   **Database**: PostgreSQL with SQLAlchemy ORM.
-   **Pagination & Sorting**: Efficient data retrieval.
# Bose_Task
