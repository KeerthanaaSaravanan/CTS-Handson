# Project Structure

handson_04/
│
├── app.py                 # Application factory function
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── project_structure.md   # This file
└── courses/
    ├── __init__.py        # Makes 'courses' a package
    └── routes.py          # Blueprint for course-related routes

## Description

- **app.py**: Contains the `create_app` factory function that creates and configures the Flask application.
- **config.py**: Defines the configuration class for the application.
- **requirements.txt**: Lists the Python packages required for the project.
- **courses/routes.py**: Defines the API endpoints for course management using a Flask Blueprint.
- **courses/__init__.py**: Empty file that makes the `courses` directory a Python package.

## Why This Structure?

- Separation of concerns: Configuration, application factory, and route definitions are in separate files.
- The application factory pattern allows for creating multiple instances of the app with different configurations.
- Blueprints help in organizing routes into modular components, making the application scalable and maintainable.