from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student
from secrets import host, user, password
from sqlalchemy import func


db = "default"

CONNECTION_STRING = f"mysql+pymysql://{user}:{password}@{host}/{db}"

eng = create_engine(CONNECTION_STRING)

Base.metadata.create_all(eng)


Session = sessionmaker(bind = eng)
s = Session()


all_the_values_from_db = s.query(Student).all()
all_the_values_from_db = [print(i) for i in all_the_values_from_db]


filtered_values_from_db = s.query(Student).filter(Student.first_name == "Vasile")
filtered_values_from_db = [print(i) for i in filtered_values_from_db]


print("-"*30)
filtered_values_from_db_2 = s.query(Student).filter(Student.id == 2)
filtered_values_from_db_2 = [print(i) for i in filtered_values_from_db_2]

print("-"*30)
filtered_values_from_db_3 = s.query(Student).filter(Student.id == 2, Student.first_name.like("Ne%"))
filtered_values_from_db_3 = [print(i) for i in filtered_values_from_db_3]

print("-"*30)
filtered_values_from_db_4 = s.query(Student).count()
print(filtered_values_from_db_4)


print("-"*50)
filtered_values_from_db_5 = s.query(func.max(Student.id))
filtered_values_from_db_5 = [f"Id maxim{print(i)}" for i in filtered_values_from_db_5]

print("-"*30)
vasile = filtered_values_from_db_6 = s.query(Student).filter(Student.first_name == "Vasile").first()
print(vasile)

vasile.last_name = "Popescu"
s.commit()

vasiles = filtered_values_from_db_6 = s.query(Student).filter(Student.first_name == "Vasile")
for vasile in vasiles:
    vasile.last_name = "Barna"
s.commit()

records = s.query(func.min((Student.last_name)))
for record in records:
    print(record)