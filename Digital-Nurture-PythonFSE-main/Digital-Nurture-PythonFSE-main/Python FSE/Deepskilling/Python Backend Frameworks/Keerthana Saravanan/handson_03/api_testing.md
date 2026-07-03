# API Testing Guide for Hands-On 3 - Task 1

This document outlines how to test the Django REST Framework API endpoints for the Course Management system.

## Base URL
All endpoints are under `/api/` as defined in the project's `urls.py`.

```
http://127.0.0.1:8000/api/
```

## Endpoints

### 1. List and Create Courses
**URL:** `/api/courses/`  
**Methods:** `GET`, `POST`

#### GET /api/courses/
- **Description:** Returns a list of all courses.
- **Success Response:**
  - **Code:** 200 OK
  - **Body:** JSON array of course objects.
    ```json
    [
      {
        "id": 1,
        "name": "Introduction to Programming",
        "code": "CS101",
        "credits": 3,
        "department": 1
      },
      {
        "id": 2,
        "name": "Data Structures",
        "code": "CS102",
        "credits": 3,
        "department": 1
      }
    ]
    ```
- **Error Response:** None (returns empty list if no courses).

#### POST /api/courses/
- **Description:** Creates a new course.
- **Request Body:** JSON object with course fields.
    ```json
    {
      "name": "Algorithms",
      gorithms",
      "code": "CS2",
      "credits: 3,
      "department": 1
    }
    ```
    Note: `code` is required and must be unique.
- **Success Response:**
  - **Code:** 201 Created
  - **Body:** JSON object of the created course.
    ```json
    {
      "id": 3,
      "name": "Algorithms",
      "code": "CS103",
      "credits": 3,
      "department": 1
    }
    ```
- **Error Response:**
  - **Code:** 400 Bad Request
  - **Body:** JSON with validation errors.
    ```json
    {
      "code": [
        "Course with this Code already exists."
      ]
    }
    ```

### 2. Retrieve, Update, and Delete a Specific Course
**URL:** `/api/courses/<int:pk>/`  
**Methods:** `GET`, `PUT`, `DELETE`

#### GET /api/courses/{id}/
- **Description:** Returns a single course by its ID.
- **Success Response:**
  - **Code:** 200 OK
  - **Body:** JSON object of the course.
    ```json
    {
      "id": 1,
      "name": "Introduction to Programming",
      "code": "CS101",
      "credits": 3,
      "department": 1
    }
    ```
- **Error Response:**
  - **Code:** 404 Not Found
  - **Body:**
    ```json
    {
      "error": "Course not found."
    }
    ```

#### PUT /api/courses/{id}/
- **Description:** Updates an existing course (full update).
- **Request Body:** JSON object with all fields.
    ```json
    {
      "name": "Advanced Programming",
      "code": "CS101",
      "credits": 4,
      "department": 2
    }
    ```
- **Success Response:**
  - **Code:** 200 OK
  - **Body:** JSON object of the updated course.
- **Error Response:**
  - **Code:** 400 Bad Request (validation errors)
  - **or** 404 Not Found if course does not exist.

#### DELETE /api/courses/{id}/
- **Description:** Deletes a course.
- **Success Response:**
  - **Code:** 204 No Content (empty body)
- **Error Response:**
  - **Code:** 404 Not Found
  - **Body:**
    ```json
    {
      "error": "Course not found."
    }
    ```

## Testing Steps

1. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

2. **Test the endpoints using a tool like `curl`, Postman, or the browser.**

   Example `curl` commands:
   ```bash
   # List courses
   curl -X GET http://127.0.0.1:8000/api/courses/

   # Create a course
   curl -X POST http://127.0.0.1:8000/api/courses/ \
        -H "Content-Type: application/json" \
        -d '{"name":"Operating Systems","code":"CS301","credits":3,"department":1}'

   # Retrieve a course (replace 1 with actual ID)
   curl -X GET http://127.0.0.1:8000/api/courses/1/

   # Update a course
   curl -X PUT http://127.0.0.1:8000/api/courses/1/ \
        -H "Content-Type: application/json" \
        -d '{"name":"Operating Systems - Advanced","code":"CS301","credits":4,"department":2}'

   # Delete a course
   curl -X DELETE http://127.0.0.1:8000/api/courses/1/
   ```

## Expected Status Codes Summary
- **GET list:** 200
- **GET detail:** 200 (or 404 if not found)
- **POST:** 201 (created) or 400 (invalid data)
- **PUT:** 200 (updated) or 400 (invalid data) or 404 (not found)
- **DELETE:** 204 (deleted) or 404 (not found)

## Notes
- Ensure the database has been migrated (`python manage.py migrate`) before testing.
- The `department` field expects the primary key of a `Department` object. Create departments via the admin or API if needed.
- The `code` field must be unique; attempting to duplicate it will result in a validation error.