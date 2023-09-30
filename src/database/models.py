from sqlalchemy import Column, Integer, String, func
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import Date
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.hybrid import hybrid_property


Base = declarative_base()

""" 
DROP TABLE IF EXISTS students; 
CREATE TABLE students (
     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     fullname STRING,
     group_id REFERENCES [groups] (id)
); 

DROP TABLE IF EXISTS [groups]; 
CREATE TABLE [groups] (
     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     name STRING UNIQUE
);

DROP TABLE IF EXISTS teachers; 
CREATE TABLE teachers (
     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     fullname STRING
);

DROP TABLE IF EXISTS disciplines; 
CREATE TABLE disciplines (
     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     name STRING UNIQUE,
     teachers_id REFERENCES teachers (id)
);

DROP TABLE IF EXISTS grade; 
CREATE TABLE grade (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    grade INTEGER, 
    disciplines_id REFERENCES disciplines (id),
    students_id REFERENCES students (id),
    date_of DATE
);

"""


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    students = relationship("Student",  back_populates="group")


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100))
    phone = Column(String(100))
    address = Column(String(150))
    group_id = Column(Integer, ForeignKey("groups.id" , ondelete="CASCADE"))
    # groups = relationship('Groups', backref="group")

    group = relationship("Group", back_populates="students")
    grade = relationship("Grade", back_populates="student")

    @hybrid_property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100))
    phone = Column(String(100))
    address = Column(String(150))

    disciplines = relationship("Discipline", back_populates="teacher",  cascade="all, delete-orphan")

    @hybrid_property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Discipline(Base):
    __tablename__ = "disciplines"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id", ondelete="CASCADE"))
    # teachers = relationship('Teachers')

    teacher = relationship("Teacher", back_populates="disciplines")
    grades = relationship("Grade", back_populates="discipline")


class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    date_of = Column(Date, nullable=False)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    discipline_id = Column(Integer, ForeignKey("disciplines.id", ondelete="CASCADE"))

    student = relationship("Student", back_populates="grade")
    discipline = relationship(
        "Discipline", back_populates="grades"
    )
