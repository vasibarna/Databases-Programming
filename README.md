# PyMySQL

The purpose is to make a connection to a DB and write some CRUD statements

## Example1
Create a DB connection and return the DB version

## Example2 
Create a DB called "default" and make a connection to the new DB

## Example3
Create a a table called "example3" in the DB "default"
Ask the user for an integer and a varchar 
Insert those values in the table

## Example4
1.Create a a table called "bikesharing" in the DB "default"
having the following columns: tstamp, cnt, temperature, 
temperature_feels, humidity, wind_speed, weather_code, 
is_holiday, is_weekend, season

2.Insert in the DB the values from the CSV file "london-bikes.csv"
and commit the datas at every 100 rows.

## Example5
Make a simple select statement in from the bikesharing table

## Example6
Create a DB called todo_app and connect to that database
Create a table called tasks with the columns task - TEXT and done - BOOLEAN
Considering the folowings operations create a MENU 
0. Exit application
1. Show active tasks
2. Show tasks done
3. Mark task as done
4. Add new task
Based on the user option, write the functions that make the above operations