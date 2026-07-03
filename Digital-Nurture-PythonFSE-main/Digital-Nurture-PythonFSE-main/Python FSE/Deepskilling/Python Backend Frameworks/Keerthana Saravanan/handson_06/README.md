# Hands-On 6: FastAPI Course Management API with Async SQLAlchemy

This project implements a Course Management API using FastAPI with asynchronous SQLAlchemy (using `aiosqlite`) for database operations.

## Features

- **Async Operations**: Utilizes async SQLAlchemy for non-blocking database operations
- **Fast**: Built on Starlette and Pydantic, comparable to NodeJS and Go performance
- **Automatic Docs**: Interactive API documentation (Swagger UI and ReDoc)
- **Data Validation**: Pydantic models for request/response validation
- **Relational Data**: Proper foreign key relationships between courses and departments
- **Filtering & Pagination**: Course listing supports filtering by department and pagination

## Project Structure

```
handson_06/
│
├── app/                          # (Previous version, not used in this task)
├── fastapi_coursemanager/       # Main application package
│   ├── __init__.py              # Package initializer
│   ├── database.py              # Async SQLAlchemy setup and session dependency
│   ├── models.py                # SQLAlchemy ORM models
│   ├── schemas.py               # Pydantic models for validation
│   ├── crud.py                  # Async CRUD operations
│   └── main.py                  # FastAPI application with route definitions
│
├── async_api_testing.md         # Async API testing examples
└── README.md                    # This file
```

## Installation

1. Clone the repository to your local machine
2. Navigate to the handson_06 directory:
   ```bash
   cd handson_06
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Development Mode
```bash
uvicorn fastapi_coursemanager.main:app --reload
```

The API will be available at http://localhost:8000

### Production Mode
```bash
uvicorn fastapi_coursemanager.main:app --host 0.0.0.0 --port 8000
```

## API Documentation

Once the server is running, access the interactive documentation:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Database Setup

The application uses SQLite with the `aiosqlite` driver for asynchronous operations.
On startup, the database tables are automatically created.

Database file: `./course_manager.db` (created in the current directory)

## API Endpoints

### Courses

- **POST /api/courses/** - Create a new course
  - Request body: `CourseCreate` schema
  - Response: `CourseResponse` schema (201 Created)

- **GET /api/courses/** - List courses with optional filtering and pagination
  - Query Parameters:
    - `skip`: Number of records to skip (default: 0)
    - `limit`: Maximum number of records to return (default: 100)
    - `department_id`: Filter by department ID (optional)
  - Response: List of `CourseResponse` objects

- **GET /api/courses/{course_id}** - Get a specific course
  - Path parameter: `course_id` (integer)
  - Response: `CourseResponse` object

- **PUT /api/courses/{course_id}** - Update a specific course
  - Path parameter: `course_id` (integer)
  - Request body: `CourseUpdate` schema (all fields optional)
  - Response: `CourseResponse` object

- **DELETE /api/courses/{course_id}** - Delete a specific course
  - Path parameter: `course_id` (integer)
  - Response: 204 No Content

## Data Models

### Course
- `id`: Integer (auto-generated primary key)
- `name`: Required string (course name)
- `code`: Required string (unique course code)
- `credits`: Required integer (course credits)
- `department_id`: Required foreign key to Department

### Department (for reference)
- `id`: Integer (auto-generated primary key)
- `name`: Required string
- `head_of_dept`: Required string
- `budget`: Float

## Technology Stack

- **Framework**: FastAPI
- **ORM**: SQLAlchemy (async) with AeroSQLite
- **Data Validation**: Pydantic
- **ASGI Server**: Uvicorn
- **Database**: SQLite (for development/testing)

## Running Tests

See [async_api_testing.md](async_api_testing.md) for detailed examples of how to test the async API endpoints using `httpx.AsyncClient`.

## Key Features of This Implementation

1. **Asynchronous Database Operations**: All database operations use async/await with SQLAlchemy 2.0 style
2. **Dependency Injection**: Database session managed via FastAPI's `Depends` system
3. **Automatic Table Creation**: Tables created on application startup
4. **Proper Error Handling**: HTTP 404 for missing resources
5. **CORS Ready**: Can be extended with CORS middleware
6. **Production Ready**: Uses proper async session management

## Notes

- This implementation uses SQLite for simplicity. For production, consider using PostgreSQL or MySQL with appropriate async drivers.
- The database connection uses `check_same_thread=False` which is necessary for SQLite with async operations.
- All endpoints are fully asynchronous, allowing for better concurrency and performance under load.