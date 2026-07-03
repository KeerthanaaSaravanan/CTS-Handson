from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

DATABASE_URL = "mysql+pymysql://root:your_password@localhost/college_db"

engine = create_engine(DATABASE_URL)

Base = declarative_base()


class Department(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True)
    dept_name = Column(String(100))

    students = relationship("Student", back_populates="department")


class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    department_id = Column(Integer, ForeignKey("departments.department_id"))

    department = relationship("Department", back_populates="students")


Session = sessionmaker(bind=engine)
session = Session()

departments = session.query(Department).all()

for dept in departments:

    print(f"\nDepartment : {dept.dept_name}")

    for student in dept.students:
        print(f"{student.student_id} - {student.first_name} {student.last_name}")

session.close()