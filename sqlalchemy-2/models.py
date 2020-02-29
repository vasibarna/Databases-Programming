from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

Base = declarative_base()

#Class 1 user for example 1, example 2 and example 3
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key = True, autoincrement = True)
    first_name = Column(String(255))
    last_name = Column(String(255))

    def __str__(self):
        return f"<Student #{self.id} {self.first_name} {self.last_name}>"


#Class 2 user for example 4
class Locker(Base):
    __tablename__ = "lockers"
    number = Column(Integer, primary_key = True)
    student = Column(Integer, ForeignKey(Student.id), primary_key = True)

    def __str__(self):
        return f"<Locker {self.number}: {self.student}>"


#Class 3 user for example 5
class Address(Base):
    __tablename__ = "address"
    student = Column(Integer, ForeignKey(Student.id), primary_key = True)
    street_name = Column(String(100))
    number = Column(Integer)
    city = Column(String(100))

    def __str__(self):
        return f"<Street {self.street_name} number {self.number} city {self.city}>"

#Class 4 user for example 6
class Grades(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key = True, autoincrement = True)
    student = Column(Integer, ForeignKey(Student.id))
    grade = Column(Integer)
    date_created = Column(DateTime)

    def __str__(self):
        return f"Name:{self.student} grade:{self.grade} date:{self.date_created}>"