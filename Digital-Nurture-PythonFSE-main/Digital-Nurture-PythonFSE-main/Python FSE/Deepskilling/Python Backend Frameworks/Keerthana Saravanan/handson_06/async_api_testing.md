# Async API Testing Guide

This document provides examples of how to test the async Course Management API endpoints using `httpx.AsyncClient`.

## Base URL
```
http://localhost:8000
```

## Testing with httpx.AsyncClient

### Install httpx
```bash
pip install httpx
```

### Example Test Script
```python
import asyncio
import httpx

BASE_URL = "http://localhost:8000"

async def test_course_endpoints():
    async with httpx.AsyncClient() as client:
        # Test root endpoint
        response = await client.get(f"{BASE_URL}/")
        assert response.status_code == 200
        assert response.json() == {"message": "API running"}

        # Create a course
        course_data = {
            "name": "Introduction to Computer Science",
            "code": "CS101",
            "credits": 3,
            "department_id": 1
        }
        response = await client.post(f"{BASE_URL}/api/courses/", json=course_data)
        assert response.status_code == 201
        created_course = response.json()
        course_id = created_course["id"]

        # Get all courses
        response = await client.get(f"{BASE_URL}/api/courses/")
        assert response.status_code == 200
        courses = response.json()
        assert len(courses) > 0

        # Get course by ID
        response = await client.get(f"{BASE_URL}/api/courses/{course_id}")
        assert response.status_code == 200
        assert response.json()["id"] == course_id

        # Update course
        update_data = {
            "name": "Advanced Computer Science",
            "credits": 4
        }
        response = await client.put(f"{BASE_URL}/api/courses/{course_id}", json=update_data)
        assert response.status_code == 200
        updated_course = response.json()
        assert updated_course["name"] == "Advanced Computer Science"
        assert updated_course["credits"] == 4

        # Delete course
        response = await client.delete(f"{BASE_URL}/api/courses/{course_id}")
        assert response.status_code == 204

        # Verify deletion
        response = await client.get(f"{BASE_URL}/api/courses/{course_id}")
        assert response.status_code == 404

        print("All tests passed!")

if __name__ == "__main__":
    asyncio.run(test_course_endpoints())
```

## Testing with Pytest and AsyncClient

### Install pytest and pytest-asyncio
```bash
pip install pytest pytest-asyncio httpx
```

### Example Test File (test_courses.py)
```python
import pytest
import httpx
from fastapi.testclient import TestClient

# Alternatively, use AsyncClient for async tests
@pytest.mark.asyncio
async def test_create_and_get_course():
    async with httpx.AsyncClient(app=app, base_url="http://test") as client:
        # Create course
        course_data = {
            "name": "Test Course",
            "code": "TEST101",
            "credits": 3,
            "department_id": 1
        }
        response = await client.post("/api/courses/", json=course_data)
        assert response.status_code == 201
        data = response.json()
        course_id = data["id"]

        # Get course
        response = await client.get(f"/api/courses/{course_id}")
        assert response.status_code == 200
        assert response.json()["name"] == "Test Course"

# To run: pytest test_courses.py
```

## Testing Filtering by Department

### Example
```python
async def test_filter_by_department():
    async with httpx.AsyncClient() as client:
        # Create two departments (if not already created)
        # For simplicity, assume department 1 and 2 exist

        # Create course in department 1
        course1 = {
            "name": "Dept1 Course",
            "code": "DEPT101",
            "credits": 3,
            "department_id": 1
        }
        await client.post("/api/courses/", json=course1)

        # Create course in department 2
        course2 = {
            "name": "Dept2 Course",
            "code": "DEPT201",
            "credits": 4,
            "department_id": 2
        }
        await client.post("/api/courses/", json=course2)

        # Get courses for department 1
        response = await client.get("/api/courses/?department_id=1")
        assert response.status_code == 200
        courses = response.json()
        assert all(c["department_id"] == 1 for c in courses)
        assert len(courses) >= 1

        # Get courses for department 2
        response = await client.get("/api/courses/?department_id=2")
        assert response.status_code == 200
        courses = response.json()
        assert all(c["department_id"] == 2 for c in courses)
        assert len(courses) >= 1

        print("Department filter test passed!")
```

## Running the Application for Testing

### Start the server
```bash
uvicorn main:app --reload
```

### Run the test scripts
```bash
python test_async.py  # For the first example
pytest test_courses.py  # For the pytest example
```

## Notes

- The async API uses the same endpoints as the synchronous version, but the error handling.
- Ensure the database is initialized (tables created) before running tests.
- For isolation, consider using a test database (e.g., SQLite in-memory) in a testing environment.