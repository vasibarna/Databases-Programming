from sqlalchemy import create_engine, desc, update
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Address
from secrets import host, user, password


db = "default"

CONNECTION_STRING = f"mysql+pymysql://{user}:{password}@{host}/{db}"

eng = create_engine(CONNECTION_STRING)

Base.metadata.create_all(eng)


Session = sessionmaker(bind = eng)
s = Session()

# s.add_all(
#     [
# Address(student = 1, street_name = "Dunarii", number = 144, city = "Cluj-Napoca"),
# Address(student = 2, street_name = "ABC", number = 100, city = "Cluj-Napoca"),
# Address(student = 5, street_name = "Strada3", number = 101, city = "Cluj")
#     ]
# )

# s.commit()



rows = s.query(Student, Address).join(Address).filter(Student.id > 4)

# rows = s.query(Student, Address).join(Address).all()



for row in rows:
    student, address = row
    print(f"|\t {student.first_name} |\t {address.street_name} |")


name_ordered_asc = s.query(Student).order_by(Student.first_name)
name_ordered_asc = [print(i) for i in name_ordered_asc]

print("-"*50)

name_ordered_desc = s.query(Student).order_by(desc(Student.first_name))
name_ordered_desc = [print(i) for i in name_ordered_desc]

print("-"*50)

name_limit_3 = s.query(Student).limit(3).all()
name_limit_3 = [print(i) for i in name_limit_3]

print("*"*50)


student_update = s.query(Student).filter(Student.first_name == "Brena").update({"first_name" : "Brennnna"})
s.commit()


