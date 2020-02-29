from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Address, Grades
from secrets import host, user, password


db = "default"

CONNECTION_STRING = f"mysql+pymysql://{user}:{password}@{host}/{db}"

eng = create_engine(CONNECTION_STRING)

Base.metadata.create_all(eng)


Session = sessionmaker(bind = eng)
s = Session()

s.add_all(
    [
Grades(student = 1, grade = 8, date_created = "2019-11-06"),
Grades(student = 2, grade = 9, date_created = "2019-12-06"),
Grades(student = 3, grade = 9, date_created = "2019-08-06"),
Grades(student = 4, grade = 10, date_created = "2019-10-06"),
Grades(student = 5, grade = 9, date_created = "2019-11-04"),
Grades(student = 6, grade = 8, date_created = "2019-06-02"),
Grades(student = 7, grade = 7, date_created = "2019-05-15")
    ]
)

s.commit()



rows = s.query(Student, Grades).join(Grades).filter(Student.id == 4)


for row in rows:
    student, grades = row
    print(f"|\t {student.first_name} |\t {grades.grade} |\t {grades.date_created}")



