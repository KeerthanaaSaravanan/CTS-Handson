# OpenAPI Customization in FastAPI

FastAPI automatically generates OpenAPI documentation (available at `/docs` for Swagger UI and `/redoc` for ReDoc). You can customize various aspects of this documentation to make it more informative and aligned with your project.

## Customizing the FastAPI Instance

You can pass several parameters to the `FastAPI` constructor to customize the metadata:

```python
app = FastAPI(
    title="Course Management API",
    description="Course Management System built with FastAPI",
    version="1.0.0",
    contact={
        "name": "Digital Nurture Student",
        "email": "student@example.com"
    }
)
```

### Parameters:
- `title`: The title of the API.
- `description`: A brief description of the API (supports Markdown).
- `version`: The version of the API.
- `contact`: Contact information for the API maintainer.
- `license_info`: License information.
- `terms_of_service`: URL to the terms of service.

## Endpoint-Level Customization

You can add metadata to each endpoint using the `summary`, `description`, `tags`, and `response_description` parameters in the route decorators.

```python
@app.post(
    "/api/courses/",
    response_model=schemas.CourseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Courses"],
    summary="Create a new course",
    response_description="Successfully created course"
)
async def create_course(course: schemas.CourseCreate, db: AsyncSession = Depends(get_db)):
    ...
```

### Parameters:
- `summary`: A short summary of what the endpoint does.
- `description`: A longer description (supports Markdown).
- `tags`: A list of tags to group endpoints in the documentation.
- `response_description`: Description of the response.

## Tags for Grouping

Endpoints with the same tag are grouped together in the Swagger UI and ReDoc interfaces. In this project, we use:
- `Tags=["Courses"]` for course-related endpoints
- `Tags=["Students"]` for student-related endpoints
- `Tags=["Enrollments"]` for enrollment-related endpoints

## Viewing the Documentation

Once the application is running, you can access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## OpenAPI JSON Schema

The raw OpenAPI schema is available at:
- JSON: `http://localhost:8000/openapi.json`
- YAML: `http://localhost:8000/openapi.yaml`

This schema can be used for code generation, API testing, and integration with API management tools.

## Benefits of Customization

1. **Improved Developer Experience**: Clear summaries and descriptions help developers understand how to use the API.
2. **Better Organization**: Tags group related endpoints, making the documentation easier to navigate.
3. **Professional Appearance**: Contact information and license details add a professional touch.
4. **Enhanced Testing**: The interactive documentation allows testing endpoints directly from the browser.