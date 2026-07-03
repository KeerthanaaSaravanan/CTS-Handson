# Hands-On 5: Flask + SQLAlchemy Course Management API

This project implements a Course Management API using Flask and SQLAlchemy for ORM, and Flask-Migrate for database migrations.

## Entity Relationship Overview

The system consists of four main entities:

1. **Department**
   - Attributes: id, name, head_of_dept, budget
   - Relationships: 
     - One-to-Many with Course (a department offers many courses)
     - One-to-Many with Student (a department has many students)

2. **Course**
   - Attributes: id, name, code (unique), credits, department_id
   - Relationships:
     - Many-to-One with Department (each course belongs to one department)
     - One-to-Many with Enrollment (a course can have many enrollments)

3. **Student**
   - Attributes: id, first_name, last_name, email (unique), department_id, enrollment_year
   - Relationships:
     - Many-to-One with Department (each student belongs to one department)
     - One-to-Many with Enrollment (a student can enroll in many courses)

4. **Enrollment**
   - Attributes: id, student_id, course_id, enrollment_date, grade
   - Relationships:
     - Many-to-One with Student (each enrollment is for one student)
     - Many-to-One with Course (each enrollment is for one course)

## SQLAlchemy Model Explanation

All models are defined in `flask_coursemanager/courses/models.py` and inherit from `db.Model` (provided by Flask-SQLAlchemy).

### Key Concepts:
- **Columns**: Defined using `db.Column` with appropriate data types (String, Integer, Float, DateTime).
- **Relationships**: Defined using `db.relationship` with `back_populates` to create bidirectional relationships.
- **Constraints**: 
  - `unique=True` for fields that must be unique (e.g., course code, student email)
  - `nullable=False` for required fields
  - `db.ForeignKey` to establish foreign key relationships

### Serialization:
Each model includes a `to_dict()` method that returns a dictionary representation of the object, suitable for JSON serialization. The method includes all relevant fields and handles special types (like datetime) by converting them to ISO format strings.

### Example Model (Course):
```python
class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)

    # Relationships
    department = db.relationship('Department', back_populates='courses')
    enrollments = db.relationship('Enrollment', back_populates='course', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Course {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'credits': self.credits,
            'department_id': self.department_id
        }
```

## Migration Workflow

We use Flask-Migrate to handle database schema changes. The typical workflow is:

1. **Initialize the migration repository** (run once):
   ```bash
   flask db init
   ```

2. **Generate a migration script** after modifying models:
   ```bash
   flask db migrate -m "description of changes"
   ```

3. **Apply the migration** to the database:
   ```bash
   flask db upgrade
   ```

### Detailed Steps:

#### Initial Setup
After setting up the Flask application and configuring the database URI in `config.py`, initialize Flask-Migrate:
```bash
flask db init
```
This creates a `migrations` directory containing Alembic configuration.

#### Making Changes to Models
When you modify a model (e.g., add a new column or table):
1. Edit the model in `flask_coursemanager/courses/models.py`.
2. Generate a migration script:
   ```bash
   flask db migrate -m "added email field to Student"
   ```
   This creates a new script in `migrations/versions/` that describes the changes.
3. Apply the migration:
   ```bash
   flask db upgrade
   ```
   This executes the migration script against the database, updating the schema.

#### Common Commands:
- `flask db migrate` - Auto-generate a migration script based on model changes
- `flask db upgrade` - Apply all pending migrations
- `flask db downgrade` - Revert the last migration
- `flask db history` - List all migration scripts

### Troubleshooting:
- **Migration fails due to existing tables**: If you're adding migrations to an existing database, you may need to stamp the current state first:
  ```bash
  flask db stamp head
  ```
  This tells Flask-Migrate to consider the current database as up-to-date.

- **Forgetting to apply migrations**: Remember that `flask db migrate` only generates the script; you must run `flask db upgrade` to apply it.

- **Conflicting migrations**: When working in a team, merge migration files carefully or rebase to avoid conflicts.

## Running the Application

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set environment variables (optional):
   ```bash
   export FLASK_APP=flask_coursemanager/app.py
   export FLASK_ENV=development
   ```

3. Initialize the database:
   ```bash
   flask db init
   flask db migrate -m "initial migration"
   flask db upgrade
   ```

4. Run the server:
   ```bash
   flask run
   ```

The API will be available at `http://localhost:5000/api/courses`.

## API Endpoints

- `GET /api/courses/` - List all courses
- `GET /api/courses/<id>` - Get a specific course
- `POST /api/courses/` - Create a new course
- `PUT /api/courses/<id>` - Update a course
- `DELETE /api/courses/<id>` - Delete a course
- `GET /api/courses/<id>/students/` - Get all students enrolled in a course

## Sample Data Creation

See `shell_examples.py` for examples of how to create sample data using the Flask shell.

Run the Flask shell with:
```bash
flask shell
```
Then execute the code from `shell_examples.py` to populate the database with sample departments, courses, students, and enrollments.