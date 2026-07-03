# Hands-On 2: Django Models and Migrations

## Models Overview

This Django project defines the following models for a course management system:

### Department
- **name**: CharField
- **head_of_dept**: CharField
- **budget**: DecimalField (or IntegerField, depending on requirements)

### Course
- **name**: CharField
- **code**: CharField with `unique=True`
- **credits**: IntegerField
- **department**: ForeignKey to Department, `on_delete=models.CASCADE`

### Student
- **first_name**: CharField
- **last_name**: CharField
- **email**: EmailField with `unique=True`
- **department**: ForeignKey to Department, `on_delete=models.CASCADE`
- **enrollment_year**: IntegerField

### Enrollment
- **student**: ForeignKey to Student, `on_delete=models.CASCADE`
- **course**: ForeignKey to Course, `on_delete=models.CASCADE`
- **enrollment_date**: DateField
- **grade**: CharField, `null=True, blank=True`

## Relationships and Constraints

- **ForeignKey Relationships**:
  - Course.department → Department
  - Student.department → Department
  - Enrollment.student → Student
  - Enrollment.course → Course
  - All ForeignKey relationships use `on_delete=models.CASCADE` to ensure referential integrity.

- **Unique Constraints**:
  - Course.code is unique.
  - Student.email is unique.
  - Enrollment model has a `unique_together` constraint on the fields `['student', 'course']` to prevent duplicate enrollments of the same student in the same course.

## Meta Class in Enrollment
```python
class Meta:
    unique_together = [['student', 'course']]
```
This ensures that each student can enroll in a given course only once.

## Migrations
Run the following commands to create and apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
To see the migration status:
```bash
python manage.py showmigrations
```

## ORM Examples (Hands-On 2 - Task 2)

See `orm_queries.py` for runnable examples of the following ORM concepts.

### CRUD Examples
- **Create**: `Model.objects.create(field=value, ...)`
- **Read**: `Model.objects.all()`, `Model.objects.filter(...)`, `Model.objects.get(...)`
- **Update**: `instance.field = new_value; instance.save()` or `Model.objects.filter(...).update(field=new_value)`
- **Delete**: `instance.delete()` or `Model.objects.filter(...).delete()`

### ORM Lookup Examples
- **Exact match**: `MyModel.objects.field=value`
- **Case-insensitive**: `MyModel.objects.field__iexact="value"`
- **Greater than**: `MyModel.objects.field__gt=10`
- **In list**: `MyModel.objects.field__in=[1,2,3]`
- **Related fields (double underscore)**: `Course.objects.filter(department__name="Computer Science")`
  - The double underscore (`__`) traverses relationships, allowing you to filter on fields of related models.

### Aggregation Examples
- **Annotate**: Adds computed fields to each object in a QuerySet.
  ```python
  Department.objects.annotate(course_count=Count('course'))
  ```
  This adds a `course_count` attribute to each Department, representing the number of related courses.

- **Aggregate**: Returns a dictionary of aggregated values over the entire QuerySet.
  ```python
  from django.db.models import Avg
  Course.objects.aggregate(avg_credits=Avg('credits'))
  ```

### select_related Explanation
- `select_related` follows foreign-key relationships, performing a SQL JOIN to retrieve related objects in the same query.
- This avoids the "N+1 query problem": without `select_related`, accessing `student.department` for each student would trigger a separate query for each student's department.
- Example:
  ```python
  # Without select_related: 1 query for students + N queries for departments
  students = Student.objects.all()
  for student in students:
      print(student.department.name)  # Triggers a query per student if not prefetched

  # With select_related: 1 query with JOIN
  students = Student.objects.select_related('department').all()
  for student in students:
      print(student.department.name)  # No additional queries
  ```

### F() Explanation
- `F()` objects allow you to refer to model field values directly in the database, without loading them into Python.
- This enables database-side operations, which are more efficient and avoid race conditions.
- Example: Increase budget by 10% for all departments:
  ```python
  from django.db.models import F
  Department.objects.update(budget=F('budget') * 1.1)
  ```
  This generates a single SQL UPDATE statement that multiplies the `budget` column by 1.1 directly in the database.
  Without `F()`, you would have to load each object into Python, modify it, and save it back, resulting in multiple queries and potential race conditions.

## Django Admin Interface (Hands-On 2 - Task 3)

### Admin Registration Overview
All models (`Department`, `Course`, `Student`, `Enrollment`) are registered in the Django admin interface via `courses/admin.py`. Each model has a corresponding `ModelAdmin` class that defines how it appears and behaves in the admin.

### Search Functionality
- **Course Admin**: Searchable by `name` and `code` fields (enabled via `search_fields = ['name', 'code']`).
- **Student Admin**: Searchable by `first_name`, `last_name`, and `email`.
- **Enrollment Admin**: Searchable by related fields using the double underscore notation (e.g., `student__first_name`, `course__name`).

### Filtering Functionality
- **Course Admin**: Filter sidebar allows filtering by `department` (via `list_filter = ['department']`).
- **Student Admin**: Filter by `department` and `enrollment_year`.
- **Enrollment Admin**: Filter by `enrollment_date`, `grade`, and the related `course__department`.

### Enrollment Constraint Testing
The `Enrollment` model includes a `unique_together = [['student', 'course']]` constraint in its `Meta` class. This prevents a student from being enrolled in the same course more than once.

**Testing the constraint via the admin interface:**
1. Attempt to create an enrollment for a student-course pair that already exists.
2. After submitting the form, Django will display a validation error at the top of the form:
   ```
   Enrollment with this Student and Course already exists.
   ```
3. This error prevents the duplicate from being saved, ensuring data integrity.

**Note**: The constraint is enforced both at the form level (via Django's model validation) and at the database level (via a unique constraint). If one were to bypass the form (e.g., using raw SQL), the database would raise an integrity error.


## Admin Interface Overview (Hands-On 2 - Task 3)

The Django admin site provides a built-in interface for managing application data. All models from the `courses` app are registered in the admin.

### Admin Registration Overview
- **Department**: Registered with `DepartmentAdmin` (displays name, head of department, budget; searchable by name; filterable by head of department).
- **Course**: Registered with `CourseAdmin` (displays name, code, credits, department; searchable by name and code; filterable by department).
- **Student**: Registered with `StudentAdmin` (displays first name, last name, email, department, enrollment year; searchable by name and email; filterable by department and enrollment year).
- **Enrollment**: Registered with `EnrollmentAdmin` (displays student, course, enrollment date, grade; searchable by student name and course details; filterable by enrollment date, grade, and department course).

### Search Functionality
- The `search_fields` attribute enables a search bar in the admin list view for each model.
- For `CourseAdmin`, searching by `name` or `code` will filter the course list in real time (case-insensitive, partial matches).
- Example: Typing "Intro" in the course search will show courses like "Introduction to Programming".

### Filtering Functionality
- The `list_filter` attribute adds sidebar filters in the admin list view.
- For `CourseAdmin`, a filter for `department` appears, allowing you to show only courses belonging to a selected department.
- Multiple filters can be combined (e.g., filter by department and then by a date range for enrollments).

### Enrollment Constraint Testing
The `Enrollment` model includes a `unique_together = [['student', 'course']]` constraint in its `Meta` class. This prevents a student from being enrolled in the same course more than once.

**How to test:**
1. Via the admin interface, create an enrollment for a student and a course.
2. Attempt to create another enrollment for the same student-course pair.
3. Upon submitting the form, Django will display a validation error:
   ```
   Enrollment with this Student and Course already exists.
   ```
   This error is caught by the model's validation before saving, preventing duplicates.
4. If one attempts to insert a duplicate directly at the database level (bypassing the ORM), the database will raise an integrity error due to the unique constraint.

### Verifying Admin Features
After creating a superuser and running the development server:
- Visit `http://127.0.0.1:8000/admin/` and log in.
- Verify that all four models appear in the "Courses" section.
- Check that the course list displays the columns: Name, Code, Credits, Department.
- Use the search box to filter courses by name or code.
- Use the sidebar filter to narrow courses by department.
- Attempt to create a duplicate enrollment to see the validation error.

---
**Note**: The admin interface is primarily for development and internal use. In production, ensure proper access controls and consider customizing the admin further for security and usability.
