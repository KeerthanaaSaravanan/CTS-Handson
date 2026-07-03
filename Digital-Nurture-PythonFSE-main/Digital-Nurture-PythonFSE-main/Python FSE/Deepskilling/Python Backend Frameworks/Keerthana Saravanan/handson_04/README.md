# Hands-On 4 - Task 1: Flask App Structure and Basic Routing

## Project Overview
This task sets up a basic Flask application with:
- Application factory pattern (`create_app` function)
- Configuration class (`Config`)
- Blueprint for course-related routes
- Basic CRUD endpoints for courses (GET list, POST create)

## How to Run the Application
1. Ensure you have Python 3.7+ installed.
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Set the environment variable for the Flask app:
   ```bash
   export FLASK_APP=app.py
   ```
4. Run the application:
   ```bash
   flask run
   ```
   The application will be available at `http://127.0.0.1:5000`.

## Endpoints
### GET `/api/courses/`
- **Description**: Retrieve a list of all courses.
- **Response**: 
  - Status Code: 200 OK
  - Body: JSON array of course objects (empty list in this initial implementation)
  ```json
  []
  ```

### POST `/api/courses/`
- **Description**: Create a new course.
- **Request Body**: JSON object with course details (not validated in this initial implementation)
  ```json
  {
    "name": "Course Name",
    "code": "CS101",
    "credits": 3
  }
  ```
- **Response**:
  - Status Code: 201 Created
  - Body: 
    ```json
    {
      "message": "Course created"
    }
    ```

## Project Structure
See `project_structure.md` for a detailed explanation of the files and directories.

## Notes
- This is a basic setup for a Flask application using the factory pattern and blueprints.
- In subsequent tasks, we will add database integration, models, and more advanced features.
- The current implementation uses in-memory storage (no persistence) for simplicity.