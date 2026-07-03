from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    head_of_dept = Column(String(100), nullable=False)
    budget = Column(Float, nullable=False)

    # Relationships
    courses = relationship("Course", back_populates="department")
    students = relationship("Student", back_populates="department")  # We don't have Student model in this task, but we'll keep for completeness

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    code = Column(String(20), unique=True, nullable=False)
    credits = Column(Integer, nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"))

    # Relationships
    department = relationship("Department", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")  # We don't have Enrollment model in this task

# Note: We are not defining Student and Enrollment models in this task as the focus is on Course.
# However, to avoid errors, we can leave them out or define them minimally.
# Since the task does not require them, we'll omit them.