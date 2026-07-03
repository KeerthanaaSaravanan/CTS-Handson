from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mysql+pymysql://root:your_password@localhost/college_db"

engine = create_engine(DATABASE_URL)

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100))
    enrollment_year = Column(Integer)


Session = sessionmaker(bind=engine)
session = Session()

# Insert a student

student = Student(
    first_name="John",
    last_name="David",
    email="john.david@college.edu",
    enrollment_year=2025
)

session.add(student)
session.commit()

print("Student Added Successfully!")

# Display all students

students = session.query(Student).all()

for s in students:
    print(s.student_id, s.first_name, s.last_name)

# Update student

student = session.query(Student).filter_by(student_id=1).first()

if student:
    student.first_name = "Arjun Updated"
    session.commit()

print("Student Updated!")

# Delete student

student = session.query(Student).filter_by(email="john.david@college.edu").first()

if student:
    session.delete(student)
    session.commit()

print("Student Deleted!")

session.close()