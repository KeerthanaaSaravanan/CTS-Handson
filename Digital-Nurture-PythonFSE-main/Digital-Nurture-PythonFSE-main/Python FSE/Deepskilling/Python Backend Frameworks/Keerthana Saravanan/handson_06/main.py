from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud, models, schemas
from .database import engine, get_db

app = FastAPI(
    title="Course Management API",
    description="A RESTful API for managing courses and departments with async SQLAlchemy",
    version="1.0.0"
)

# Create tables
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

# Dependency
# get_db is imported from database

@app.get("/")
async def root():
    return {"message": "API running"}

@app.post("/api/courses/", response_model=schemas.CourseResponse, status_code=status.HTTP_201_CREATED)
async def create_course(course: schemas.CourseCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_course(db=db, course=course)

@app.get("/api/courses/", response_model=list[schemas.CourseResponse])
async def read_courses(skip: int = 0, limit: int = 100, department_id: int = None, db: AsyncSession = Depends(get_db)):
    courses = await crud.get_courses(db=db, skip=skip, limit=limit, department_id=department_id)
    return courses

@app.get("/api/courses/{course_id}", response_model=schemas.CourseResponse)
async def read_course(course_id: int, db: AsyncSession = Depends(get_db)):
    db_course = await crud.get_course(db=db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course

@app.put("/api/courses/{course_id}", response_model=schemas.CourseResponse)
async def update_course(course_id: int, course: schemas.CourseUpdate, db: AsyncSession = Depends(get_db)):
    db_course = await crud.update_course(db=db, course_id=course_id, course=course)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course

@app.delete("/api/courses/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_id: int, db: AsyncSession = Depends(get_db)):
    db_course = await crud.delete_course(db=db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return None

# Department endpoints (optional, but we can keep them for completeness)
# We'll skip department endpoints for brevity, but if required, we can add similar CRUD for departments.
# However, the task only requires course endpoints with department_id filter.