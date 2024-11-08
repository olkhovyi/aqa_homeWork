from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from faker import Faker
import random


Base = declarative_base()
fake = Faker()

# Enrollment table for many-to-many relationships between students and courses
enrollment_table = Table('enrollment', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

# Model Student
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    courses = relationship('Course', secondary=enrollment_table, back_populates='students')

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}')>"

# Model Course
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    students = relationship('Student', secondary=enrollment_table, back_populates='courses')

    def __repr__(self):
        return f"<Course(id={self.id}, title='{self.title}')>"

engine = create_engine('sqlite:///university.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding courses
def populate_database():
    courses = [Course(title=f"Course {i}") for i in range(1, 6)]
    session.add_all(courses)
    session.commit()

    # Adding students with unique names and enrolling them in courses
    students = [Student(name=fake.name()) for _ in range(20)]
    for student in students:
        student.courses = random.sample(courses, k=random.randint(1, 3))
        session.add(student)
    session.commit()
    print("Database populated with sample data.")

# Function for adding a new student with a random name and enrolling him in a course
def add_student(course_title):
    random_name = fake.name()
    new_student = Student(name=random_name)
    session.add(new_student)
    course = session.query(Course).filter_by(title=course_title).first()
    if course:
        new_student.courses.append(course)
    session.commit()
    print(f"Student {random_name} added and enrolled in {course_title}.")

# Functions for executing queries
def get_students_on_course(course_title):
    course = session.query(Course).filter_by(title=course_title).first()
    if course:
        return course.students
    return []

def get_courses_for_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()
    if student:
        return student.courses
    return []

# Function to update student name to random
def update_student_name(student_id):
    student = session.get(Student, student_id)
    if student:
        new_name = fake.name()
        student.name = new_name
        session.commit()
        print(f"Updated Student ID {student_id} to new name '{new_name}'.")

# Function to update student name to random
def delete_student(student_id):
    student = session.get(Student, student_id)
    if student:
        session.delete(student)
        session.commit()
        print(f"Deleted Student ID {student_id}.")


if __name__ == "__main__":
    populate_database()
    add_student("Course 1")
    students_on_course = get_students_on_course("Course 1")
    print("Students on Course 1:", students_on_course)


    courses_for_student = get_courses_for_student("Student 1")
    print("Courses for Student 1:", courses_for_student)

    update_student_name(1)

    delete_student(2)