import pymysql
from secrets import host, user, password
import datetime

db = pymysql.connect(host, user, password, "default")

with db.cursor() as c:
    c._defer_warnings = True
    c.execute("""CREATE TABLE IF NOT EXISTS `bikesharing` (
        tstamp TIMESTAMP, 
        cnt INTEGER, 
        temperature DECIMAL(5, 2),
        temperature_feels DECIMAL(5, 2), 
        humidity DECIMAL(4, 1), 
        wind_speed DECIMAL(5, 2), 
        weather_code INTEGER, 
        is_holiday BOOLEAN, 
        is_weekend BOOLEAN, 
        season INTEGER);""")
    # c.execute("DELETE FROM `bikesharing`")



insert_stmt = '''INSERT INTO `bikesharing` (tstamp, cnt, temperature, 
                temperature_feels, humidity, wind_speed, weather_code, is_holiday, is_weekend, 
                season) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''

def convert_line_to_values(line):
    value = line.split(",")
    value[0] = datetime.datetime.strptime(value[0],"%Y-%m-%d %H:%M:%S")
    return value

with open("/home/vasile/Desktop/DB Programming/pymysql-1/london-bikes.csv", "r") as f:
    date = f.readlines()

i = 0

with db.cursor() as c:
    c._defer_warnings = True
    for i, line in enumerate(date):
        if i == 0:
            continue
        d = convert_line_to_values(line)
        c.execute(insert_stmt, d)
        if i % 100 == 0:
            db.commit()
    db.commit()
db.close()


