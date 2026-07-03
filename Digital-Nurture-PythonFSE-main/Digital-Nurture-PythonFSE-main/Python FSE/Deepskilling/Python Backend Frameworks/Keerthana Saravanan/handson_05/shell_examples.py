# shell_examples.py
# This script demonstrates how to use the Flask shell to create sample data.
# To run these examples, launch the Flask shell with:
#   flask shell
# Then copy and paste the following lines into the shell prompt.

# Import the app and db to create an application context
from flask_coursemanager import create_app, db
from flask_coursemanager.courses.models import Department, Course, Student, Enrollment

# Create an application context
app = create_app()
app.app_context().push()

# Now we can use the db and models

# Create 2 Departments
dept1 = Department(name='Computer Science', head_of_dept='Dr. Smith', budget=100000.0)
dept2 = Department(name='Mathematics', head_of_dept='Dr. Johnson', budget=80000.0)

# Add departments to the session
db.session.add(dept1)
db.session.add(dept2)

# Commit the session to save departments to the database
db.session.commit()

# Create 3 Courses
course1 = Course(name='Introduction to Programming', code='CS101', credits=3, department_id=dept1.id)
course2 = Course(name='Data Structures', code='CS102', credits=3, department_id=dept1.id)
course3 = Course(name='Calculus I', code='MATH101', credits=4, department_id=dept2.id)

# Add courses to the session
db.session.add(course1)
db.session.add(course2)
db.session.add(course3)

# Commit the session to save courses to the database
db.session.commit()

# Optional: Create some students and enrollments to demonstrate relationships
student1 = Student(first_name='Alice', last_name='Smith', email='alice@example.com', department_id=dept1.id, enrollment_year=2023)
student2 = Student(first_name='Bob', last_name='Jones', email='bob@example.com', department_id=dept2.id, enrollment_year=2022)

db.session.add(student1)
db.session.add(student2)
db.session.commit()

# Enroll students in courses
enrollment1 = Enrollment(student_id=student1.id, course_id=course1.id, grade='A')
enrollment2 = Enrollment(student_id=student1.id, course_id=course2.id, grade='B+')
enrollment3 = Enrollment(student_id=student2.id, course_id=course3.id, grade='A-')

db.session.add(enrollment1)
db.session.add(enrollment2)
db.session.add(enrollment3)
db.session.commit()

# Now you can query the data
print("Departments:")
for dept in Department.query.all():
    print(f"  {dept}")

print("\nCourses:")
for course in Course.query.all():
    print(f"  {course}")

print("\nStudents:")
for student in Student.query.all():
    print(f"  {student}")

print("\nEnrollments:")
for enrollment in Enrollment.query.all():
    print(f"  {enrollment}")

# To exit the Flask shell, type exit() or press Ctrl+D