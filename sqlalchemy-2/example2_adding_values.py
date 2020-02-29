from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student
from secrets import host, user, password


db = "default"

CONNECTION_STRING = f"mysql+pymysql://{user}:{password}@{host}/{db}"

eng = create_engine(CONNECTION_STRING)

Base.metadata.create_all(eng)


Session = sessionmaker(bind = eng)
s = Session()

s.add_all(
    [
Student(first_name = "Mike", last_name = "Wazowski"),
Student(first_name = "Netti", last_name = "Nashe"),
Student(first_name = "Jessamine", last_name = "Addison"),
Student(first_name = "Brena", last_name = "Bugdale"),
Student(first_name = "Theobald", last_name = "Oram"),
    ]
)

s.commit()

s.add(Student(first_name = "Vasile", last_name = "Barna"))
s.commit()

s.add(Student(first_name = "Vasile", last_name = "Popa"))
s.commit()

