from fastapi import FastAPI, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud, models, schemas
from .database import engine, get_db

app = FastAPI(
    title="Course Management API",
    description="Course Management System built with FastAPI",
    version="1.0.0",
    contact={
        "name": "Digital Nurture Student",
        "email": "student@example.com"
    }
)

# Create tables
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

def send_confirmation_email(student_email: str):
    """
    Simulate sending a confirmation email.
    In a real application, this would connect to an email service.
    """
    print(f"Sending confirmation to {student_email}")

@app.get("/")
async def root():
    return {"message": "API running"}

@app.post("/api/courses/", response_model=schemas.CourseResponse, status_code=status.HTTP_201_CREATED, tags=["Courses"], summary="Create a new course", response_description="Successfully created course")
async def create_course(course: schemas.CourseCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_course(db=db, course=course)

@app.get("/api/courses/", response_model=list[schemas.CourseResponse], tags=["Courses"], summary="List all courses", response_description="List of courses")
async def read_courses(skip: int = 0, limit: int = 100, department_id: int = None, db: AsyncSession = Depends(get_db)):
    courses = await crud.get_courses(db=db, skip=skip, limit=limit, department_id=department_id)
    return courses

@app.get("/api/courses/{course_id}", response_model=schemas.CourseResponse, tags=["Courses"], summary="Get a course by ID", response_description="Course details")
async def read_course(course_id: int, db: AsyncSession = Depends(get_db)):
    db_course = await crud.get_course(db=db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course

@app.put("/api/courses/{course_id}", response_model=schemas.CourseResponse, tags=["Courses"], summary="Update a course", response_description="Updated course details")
async def update_course(course_id: int, course: schemas.CourseUpdate, db: AsyncSession = Depends(get_db)):
    db_course = await crud.update_course(db=db, course_id=course_id, course=course)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course

@app.delete("/api/courses/{course_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Courses"], summary="Delete a course", response_description="Course deleted successfully")
async def delete_course(course_id: int, db: AsyncSession = Depends(get_db)):
    db_course = await crud.delete_course(db=db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return None

# Student endpoints
@app.post("/api/students/", response_model=schemas.StudentResponse, status_code=status.HTTP_201_CREATED, tags=["Students"], summary="Create a new student", response_description="Successfully created student")
async def create_student(student: schemas.StudentCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_student(db=db, student=student)

@app.get("/api/students/", response_model=list[schemas.StudentResponse], tags=["Students"], summary="List all students", response_description="List of students")
async def read_students(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    students = await crud.get_students(db=db, skip=skip, limit=limit)
    return students

@app.get("/api/students/{student_id}", response_model=schemas.StudentResponse, tags=["Students"], summary="Get a student by ID", response_description="Student details")
async def read_student(student_id: int, db: AsyncSession = Depends(get_db)):
    db_student = await crud.get_student(db=db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.put("/api/students/{student_id}", response_model=schemas.StudentResponse, tags=["Students"], summary="Update a student", response_description="Updated student details")
async def update_student(student_id: int, student: schemas.StudentUpdate, db: AsyncSession = Depends(get_db)):
    db_student = await crud.update_student(db=db, student_id=student_id, student=student)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.delete("/api/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Students"], summary="Delete a student", response_description="Student deleted successfully")
async def delete_student(student_id: int, db: AsyncSession = Depends(get_db)):
    db_student = await crud.delete_student(db=db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return None

# Enrollment endpoints
@app.post("/api/enrollments/", response_model=schemas.EnrollmentResponse, status_code=status.HTTP_201_CREATED, tags=["Enrollments"], summary="Enroll a student in a course", response_description="Enrollment created successfully")
async def create_enrollment(enrollment: schemas.EnrollmentCreate, background_tasks: BackgroundTasks, db: AsyncSession = Depends(get_db)):
    # Verify student exists
    db_student = await crud.get_student(db=db, student_id=enrollment.student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    # Verify course exists
    db_course = await crud.get_course(db=db, course_id=enrollment.course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    # Create enrollment
    db_enrollment = await crud.create_enrollment(db=db, enrollment=enrollment)
    # Add background task to send confirmation email
    background_tasks.add_task(send_confirmation_email, db_student.email)
    return db_enrollment

@app.get("/api/enrollments/", response_model=list[schemas.EnrollmentResponse], tags=["Enrollments"], summary="List all enrollments", response_description="List of enrollments")
async def read_enrollments(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    enrollments = await crud.get_enrollments(db=db, skip=skip, limit=limit)
    return enrollments

@app.get("/api/enrollments/{enrollment_id}", response_model=schemas.EnrollmentResponse, tags=["Enrollments"], summary="Get an enrollment by ID", response_description="Enrollment details")
async def read_enrollment(enrollment_id: int, db: AsyncSession = Depends(get_db)):
    db_enrollment = await crud.get_enrollment(db=db, enrollment_id=enrollment_id)
    if db_enrollment is None:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return db_enrollment

@app.get("/api/courses/{course_id}/students/", response_model=list[schemas.StudentResponse], tags=["Courses"], summary="Get students enrolled in a course", response_description="List of students enrolled in the specified course")
async def read_course_students(course_id: int, db: AsyncSession = Depends(get_db)):
    # Verify course exists
    db_course = await crud.get_course(db=db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    # Get enrollments for the course
    enrollments = await crud.get_enrollments_by_course(db=db, course_id=course_id)
    # Get student details for each enrollment
    students = []
    for enrollment in enrollments:
        student = await crud.get_student(db=db, student_id=enrollment.student_id)
        if student:
            students.append(student)
    return students

@app.delete("/api/enrollments/{enrollment_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Enrollments"], summary="Delete an enrollment", response_description="Enrollment deleted successfully")
async def delete_enrollment(enrollment_id: int, db: AsyncSession = Depends(get_db)):
    db_enrollment = await crud.delete_enrollment(db=db, enrollment_id=enrollment_id)
    if db_enrollment is None:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return None