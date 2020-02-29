from sqlalchemy import create_engine
from models import Base, Student
from secrets import host, user, password


db = "default"

CONNECTION_STRING = f"mysql+pymysql://{user}:{password}@{host}/{db}"

eng = create_engine(CONNECTION_STRING)

Base.metadata.create_all(eng)

