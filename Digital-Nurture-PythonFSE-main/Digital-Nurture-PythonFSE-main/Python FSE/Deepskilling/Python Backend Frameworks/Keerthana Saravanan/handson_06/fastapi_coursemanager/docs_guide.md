# API Documentation Guide

This document explains how to access and use the automatically generated API documentation for the Course Management API.

## Automatic Documentation Generation

FastAPI automatically generates interactive API documentation based on your path operations and Pydantic models. Two documentation interfaces are available:

### 1. Swagger UI
Accessible at: `http://localhost:8000/docs`

Features:
- Interactive interface to test API endpoints directly in the browser
- Beautiful, responsive design
- Automatic code snippets for various languages (curl, Python, JavaScript, etc.)
- Real-time request/response formatting
- Authentication support (if implemented)

### 2. ReDoc
Accessible at: `http://localhost:8000/redoc`

Features:
- Clean, documentation-focused interface
- Three-pane layout (navigation, content, examples)
- Excellent for reading and understanding API structure
- Mobile-friendly responsive design
- Search functionality

## Customizing Documentation

You can customize the documentation appearance and behavior through FastAPI parameters:

```python
app = FastAPI(
    title="Course Management API",
    description="A RESTful API for managing courses and departments",
    version="1.0.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "API Support",
        "url": "http://example.com/contact/",
        "email": "support@example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)
```

## Documentation in Code

### Path Operation Docstrings
The docstring of your path operation functions becomes the description in the documentation:

```python
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    Retrieve an item by its ID.
    
    - **item_id**: The ID of the item to retrieve
    - Returns: The item object if found
    """
    return {"item_id": item_id}
```

### Parameter Documentation
Use `Query`, `Path`, `Body`, `Header`, `Form`, `File`, and `Cookie` from `fastapi` to add metadata:

```python
from fastapi import Query

@app.get("/items/")
async def read_items(
    q: str = Query(None, min_length=3, max_length=50, description="Search query")
):
    return {"q": q}
```

### Response Models
Define Pydantic models for response data to get automatic validation and documentation:

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item
```

## Viewing the OpenAPI Schema

FastAPI generates an OpenAPI schema that powers the documentation interfaces:

- JSON format: `http://localhost:8000/openapi.json`
- YAML format: `http://localhost:8000/openapi.yaml`

This schema can be used with various tools for:
- Code generation (client SDKs, server stubs)
- API testing and validation
- Documentation generation in other formats
- Integration with API management platforms

## Best Practices for Documentation

1. **Descriptive Path Operations**: Use clear, descriptive names for your endpoints
2. **Detailed Docstrings**: Explain what each endpoint does, its parameters, and return values
3. **Parameter Validation**: Use Pydantic models and Query/Path/Body parameters for validation
4. **Response Examples**: Provide examples in your response models when helpful
5. **Status Codes**: Specify expected status codes using `responses` parameter
6. **Tags**: Group related endpoints using tags for better organization
7. **Security Schemes**: Document authentication methods if applicable

## Example Documentation Output

When you navigate to `/docs`, you'll see:

1. **API Title**: "Course Management API" (from FastAPI constructor)
2. **Version**: "1.0.0" (from FastAPI constructor)
3. **Endpoints Grouped by Path**: Organized by URL pattern
4. **HTTP Methods**: Color-coded (GET=blue, POST=green, PUT=orange, DELETE=red)
5. **Try it Out Button**: Allows executing requests directly from the documentation
6. **Request/Response Examples**: Auto-generated from Pydantic models
7. **Schema Section**: Detailed definitions of all data models

## Troubleshooting Documentation Issues

### Blank Documentation Page
- Ensure your FastAPI app is running
- Check that you're accessing the correct URL (/docs or /redoc)
- Verify no JavaScript errors in browser console

### Missing Endpoints
- Confirm your path operations are decorated with `@app.*`
- Check for import errors preventing module loading
- Verify you're looking at the correct FastAPI instance

### Incorrect Data Models
- Review your Pydantic model definitions
- Ensure you're using the correct models in response_model parameters
- Check for circular imports affecting model resolution

## Production Considerations

In production environments, you may want to:
- Disable documentation endpoints for security:
  ```python
  app = FastAPI(docs_url=None, redoc_url=None)  # Disable both
  ```
- Or restrict access to internal networks only
- Consider customizing the documentation UI to match your brand
- Keep API documentation versioned alongside your API versions