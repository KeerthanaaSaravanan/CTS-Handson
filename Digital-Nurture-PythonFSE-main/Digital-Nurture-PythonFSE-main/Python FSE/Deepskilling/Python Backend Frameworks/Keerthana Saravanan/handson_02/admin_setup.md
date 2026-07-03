# Django Admin Setup Guide

## A. Superuser Creation

To access the Django admin interface, you first need to create a superuser account.

Run the following command:
```bash
python manage.py createsuperuser
```

Follow the prompts to enter the desired credentials. For local testing, you can use:
- **Username**: `admin`
- **Email**: `admin@college.admin'

    above credentials for desides
    password:    strong       
    is:
- **Password**: `Admin@123`

> **Note**: These credentials are for local development only. Use strong, unique passwords in production.

## B. Accessing the Admin Interface

After creating the superuser, start the development server:
```bash
python manage.py runserver
```

Then, open your web browser and navigate to:
```
http://127.0.0.1:8000/admin/
```

Log in using the superuser credentials you just created.

## C. Managing Data via Admin

### Creating Departments
1. From the admin dashboard, click on "Departments" under the "Courses" section.
2. Click the "Add Department" button.
3. Fill in the form:
   - **Name**: e.g., "Computer Science"
   - **Head of Dept**: e.g., "Dr. Alice Smith"
   - **Budget**: e.g., `150000.00`
4. Click "Save".

### Creating Courses
1. Click on "Courses" in the admin dashboard.
2. Click "Add Course".
3. Fill in the form:
   - **Name**: e.g., "Introduction to Programming"
   - **Code**: e.g., `CS101` (must be unique)
   - **Credits**: e.g., `3`
   - **Department**: select the department you created (e.g., "Computer Science")
4. Click "Save".

### Creating Students
1. Click on "Students" in the admin dashboard.
2. Click "Add Student".
3. Fill in the form:
   - **First Name**: e.g., "John"
   - **Last Name**: e.g., "Doe"
   - **Email**: e.g., `john.doe@example.com` (must be unique)
   - **Department**: select the appropriate department
   - **Enrollment Year**: e.g., `2023`
4. Click "Save".

### Creating Enrollments
1. Click on "Enrollments" in the admin dashboard.
2. Click "Add Enrollment".
3. Fill in the form:
   - **Student**: select a student (e.g., "John Doe")
   - **Course**: select a course (e.g., "Introduction to Programming")
   - **Enrollment Date**: e.g., `2023-09-01`
   - **Grade**: optional, e.g., `A` (can be left blank)
4. Click "Save".

## Testing Steps

### 1. Create 3 Courses
- Create three distinct courses (e.g., CS101, CS102, MATH101) following the steps above.

### 2. Create 5 Students
- Create five students with unique emails and assign them to departments.

### 3. Create 4 Enrollments
- Enroll students in courses, ensuring at least one student is enrolled in two different courses.

### 4. Verifying `unique_together` Constraint
The `Enrollment` model has a `unique_together` constraint on `['student', 'course']`, meaning a student cannot be enrolled in the same course more than once.

To test this:
1. Try to create an enrollment for a student-course pair that already exists.
2. After submitting the form, Django will display a validation error:
   ```
   Enrollment with this Student and Course already exists.
   ```
   This prevents duplicate enrollments at the form level.
3. If you attempt to bypass the form (e.g., via the database directly), the database will raise an integrity error due to the unique constraint.

## Admin Features Highlighted

### Search Functionality
- The `search_fields` attribute in `CourseAdmin` enables a search box at the top of the course list.
- You can search by `name` or `code` (e.g., typing "Python" will find courses with "Python" in the name).

### Filtering Functionality
- The `list_filter` attribute in `CourseApp` adds a sidebar filter for the `department` field.
- This allows you to narrow down the list of courses to those belonging to a specific department.

### Custom CourseAdmin Configuration
- `list_display` controls which columns appear in the course list: name, code, credits, and department.
- Clicking on a column header (if the field is sortable) will sort the list by that column.

