#!/usr/bin/env python
"""
ORM Queries Demonstration for Hands-On 2 - Task 2

This script demonstrates various Django ORM queries as required by the exercise.
It creates sample data and then runs various query examples.

To run this script:
    python orm_queries.py

Make sure you are in the handson_02 directory (where manage.py is located in the coursemanager subdirectory)
and that the Django environment is set up correctly.
"""

import os
import sys
import django
from django.db import connection
from django.db.models import Count, F

# Set up Django environment
# We are in handson_02, and the settings are in coursemanager/coursemanager/settings.py
sys.path.append(os.path.join(os.path.dirname(__file__), 'coursemanager'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coursemanager.settings')
django.setup()

# Now we can import our models
from courses.models import Department, Course, Student, Enrollment

def clear_data():
    """Delete existing data to start fresh."""
    Enrollment.objects.all().delete()
    Student.objects.all().delete()
    Course.objects.all().delete()
    Department.objects.all().delete()

def create_sample_data():
    """Create sample data: 2 Departments, 4 Courses, 5 Students."""
    print("Creating sample data...")

    # Create departments
    dept_cs = Department.objects.create(
        name="Computer Science",
        head_of_dept="Dr. Alice Smith",
        budget=150000.00
    )
    dept_math = Department.objects.create(
        name="Mathematics",
        head_of_dept="Dr. Bob Johnson",
        budget=100000.00
    )

    # Create courses
    course1 = Course.objects.create(
        name="Introduction to Programming",
        code="CS101",
        credits=3,
        department=dept_cs
    )
    course2 = Course.objects.create(
        name="Data Structures",
        code="CS102",
        credits=3,
        department=dept_cs
    )
    course3 = Course.objects.create(
        name="Calculus I",
        code="MATH101",
        credits=4,
        department=dept_math
    )
    course4 = Course.objects.create(
        name="Linear Algebra",
        code="MATH102",
        credits=3,
        department=dept_math
    )

    # Create students
    student1 = Student.objects.create(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        department=dept_cs,
        enrollment_year=2023
    )
    student2 = Student.objects.create(
        first_name="Jane",
        last_name="Smith",
        email="jane.smith@example.com",
        department=dept_cs,
        enrollment_year=2023
    )
    student3 = Student.objects.create(
        first_name="Bob",
        last_name="Johnson",
        email="bob.johnson@example.com",
        department=dept_math,
        enrollment_year=2022
    )
    student4 = Student.objects.create(
        first_name="Alice",
        last_name="Williams",
        email="alice.williams@example.com",
        department=dept_math,
        enrollment_year=2022
    )
    student5 = Student.objects.create(
        first_name="Charlie",
        last_name="Brown",
        email="charlie.brown@example.com",
        department=dept_cs,
        enrollment_year=2021
    )

    # Create some enrollments
    Enrollment.objects.create(
        student=student1,
        course=course1,
        enrollment_date="2023-09-01",
        grade="A"
    )
    Enrollment.objects.create(
        student=student1,
        course=course2,
        enrollment_date="2023-09-01",
        grade="B+"
    )
    Enrollment.objects.create(
        student=student3,
        course=course3,
        enrollment_date="2022-09-01",
        grade="A-"
    )
    Enrollment.objects.create(
        student=student4,
        course=course4,
        enrollment_date="2022-09-01",
        grade="B"
    )
    Enrollment.objects.create(
        student=student5,
        course=course1,
        enrollment_date="2021-09-01",
        grade="A"
    )

    print("Sample data created.\n")

def demonstrate_queries():
    """Demonstrate various ORM queries."""
    print("=== Demonstrating ORM Queries ===\n")

    # Clear connection queries log
    if hasattr(connection, 'reset_queries'):
        connection.reset_queries()

    # A. Filter courses by department
    print("A. Filter courses by department (Computer Science):")
    cs_courses = Course.objects.filter(department__name="Computer Science")
    for course in cs_courses:
        print(f"  - {course.code}: {course.name}")
    print(f"  Found {cs_courses.count()} courses.")
    print("  Explanation: The double underscore (__) is the lookup syntax that allows "
          "us to traverse relationships. Here, we filter Course by the name of its related Department.\n")

    # B. Aggregation example
    print("B. Annotation: Count courses per department:")
    dept_counts = Department.objects.annotate(course_count=Count('course'))
    for dept in dept_counts:
        print(f"  - {dept.name}: {dept.course_count} course(s)")
    print("  Explanation: annotate() adds extra fields to each object in the QuerySet, "
          "in this case counting related courses for each department.\n")

    # C. values() example
    print("C. values() example: Get only specific fields as dictionaries:")
    course_values = Course.objects.filter(department__name="Mathematics").values('code', 'name', 'credits')
    for course in course_values:
        print(f"  - {course}")
    print("  Explanation: values() returns a QuerySet that returns dictionaries instead of model instances, "
          "which can be more efficient when you only need specific fields.\n")

    # D. select_related example
    print("D. select_related example: Fetch students with their department in one query:")
    # Reset query count
    if hasattr(connection, 'reset_queries'):
        connection.reset_queries()

    students_with_dept = Student.objects.select_related('department').all()
    print(f"  Number of queries after select_related: {len(connection.queries)}")
    for student in students_with_dept[:3]:  # Show first 3
        print(f"  - {student.first_name} {student.last_name} -> {student.department.name}")
    print("  Explanation: select_related follows foreign-key relationships, fetching related objects "
          "in the same SQL query using a JOIN. This avoids the 'N+1 query problem' where each "
          "student would trigger a separate query to get their department.\n")

    # E. Query inspection using connection.queries
    print("E. Query inspection: Demonstrating that select_related reduces queries:")
    # First, without select_related (to show the difference)
    if hasattr(connection, 'reset_queries'):
        connection.reset_queries()
    students_without = Student.objects.all()[:3]
    # Now, to actually trigger the query, we need to iterate and access the related field
    for student in students_without:
        _ = student.department.name  # This will cause a query for each student if not prefetched
    count_without = len(connection.queries)
    print(f"  Number of queries for 3 students without select_related: {count_without}")

    # Now with select_related
    if hasattr(connection, 'reset_queries'):
        connection.reset_queries()
    students_with = Student.objects.select_related('department').all()[:3]
    for student in students_with:
        _ = student.department.name  # This should not cause additional queries
    count_with = len(connection.queries)
    print(f"  Number of queries for 3 students with select_related: {count_with}")
    print("  Explanation: By using select_related, we reduced the number of queries from 4 (1 for students + 3 for departments) to 1.\n")

    # F. Update example using F expressions
    print("F. Update example: Increase budget by 10% using F expressions:")
    # Show current budgets
    print("  Before update:")
    for dept in Department.objects.all():
        print(f"    - {dept.name}: ${dept.budget}")

    # Update using F expression
    Department.objects.update(budget=F('budget') * 1.1)

    print("  After update:")
    for dept in Department.objects.all():
        print(f"    - {dept.name}: ${dept.budget:.2f}")
    print("  Explanation: F() expressions allow us to refer to model field values directly in the database, "
          "without pulling them into Python. This means the update is done entirely in SQL, which is more efficient "
          "and avoids race conditions. The database multiplies the budget column by 1.1 directly.\n")

    print("=== End of demonstrations ===")

if __name__ == "__main__":
    # Clear any existing data and create sample data
    clear_data()
    create_sample_data()

    # Demonstrate the queries
    demonstrate_queries()

    print("\nScript completed successfully.")