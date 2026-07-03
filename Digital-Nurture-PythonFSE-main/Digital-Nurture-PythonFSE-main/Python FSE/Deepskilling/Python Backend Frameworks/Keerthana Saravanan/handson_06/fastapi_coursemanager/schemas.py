from pydantic import BaseModel
from typing import List, Optional

# Pydantic schemas for Course
class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    credits: int

class CourseCreate(CourseBase):
    pass

class CourseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    credits: Optional[int] = None

class CourseResponse(CourseBase):
    id: int

    class Config:
        orm_mode = True

# Pydantic schemas for Department
class DepartmentBase(BaseModel):
    name: str
    description: Optional[str] = None

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentResponse(DepartmentBase):
    id: int
    courses: List[CourseResponse] = []

    class Config:
        orm_mode = True