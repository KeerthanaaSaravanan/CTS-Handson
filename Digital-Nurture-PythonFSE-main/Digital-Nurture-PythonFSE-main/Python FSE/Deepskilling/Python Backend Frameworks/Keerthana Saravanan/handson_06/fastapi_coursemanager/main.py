from fastapi import FastAPI, HTTPException, status
from fastapi_coursemanager.schemas import (
    CourseCreate, CourseUpdate, CourseResponse,
    DepartmentCreate, DepartmentResponse
)
from typing import List

app = FastAPI(
    title="Course Management API",
    description="A RESTful API for managing courses and departments",
    version="1.0.0"
)

# In-memory storage for demonstration
courses_db = []
departments_db = []
course_id_counter = 1
department_id_counter = 1

@app.get("/")
async def root():
    return {"message": "API running"}

@app.post("/api/courses/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
async def create_course(course: CourseCreate):
    global course_id_counter
    course_data = course.dict()
    course_data["id"] = course_id_counter
    course_id_counter += 1
    courses_db.append(course_data)
    return course_data

@app.get("/api/courses/", response_model=List[CourseResponse])
async def get_courses():
    return courses_db

@app.get("/api/courses/{course_id}", response_model=CourseResponse)
async def get_course(course_id: int):
    for course in courses_db:
        if course["id"] == course_id:
            return course
    raise HTTPException(status_code=404, detail="Course not found")

@app.put("/api/courses/{course_id}", response_model=CourseResponse)
async def update_course(course_id: int, course_update: CourseUpdate):
    for course in courses_db:
        if course["id"] == course_id:
            if course_update.title is not None:
                course["title"] = course_update.title
            if course_update.description is not None:
                course["description"] = course_update.description
            if course_update.credits is not None:
                course["credits"] = course_update.credits
            return course
    raise HTTPException(status_code=404, detail="Course not found")

@app.delete("/api/courses/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_id: int):
    for i, course in enumerate(courses_db):
        if course["id"] == course_id:
            del courses_db[i]
            return
    raise HTTPException(status_code=404, detail="Course not found")

# Department endpoints
@app.post("/api/departments/", response_model=DepartmentResponse, status_code=status.HTTP_201_CREATED)
async def create_department(department: DepartmentCreate):
    global department_id_counter
    department_data = department.dict()
    department_data["id"] = department_id_counter
    department_id_counter += 1
    departments_db.append(department_data)
    return department_data

@app.get("/api/departments/", response_model=List[DepartmentResponse])
async def get_departments():
    return departments_db

@app.get("/api/departments/{department_id}", response_model=DepartmentResponse)
async def get_department(department_id: int):
    for department in departments_db:
        if department["id"] == department_id:
            # Load courses for this department
            dept_courses = [course for course in courses_db if course.get("department_id") == department_id]
            department["courses"] = dept_courses
            return department
    raise HTTPException(status_code=404, detail="Department not found")