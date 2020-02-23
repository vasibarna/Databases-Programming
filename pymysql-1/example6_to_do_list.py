import pymysql
from secrets import host, user, password

def show_tasks(c):
    #print all open tasks and their ids in order of ids
    select_stmt = '''SELECT id, task FROM tasks WHERE done !=1 ORDER BY id;'''
    c.execute(select_stmt)
    lista = c.fetchall()
    print(f"\nTask List\n{'-' * 30}")
    lista = [print(elem) for elem in lista]
    print("-" * 30)

def show_tasks_done(c):
    #print all done tasks and their ids in order of ids
    select_stmt = '''
    SELECT id, task 
    FROM tasks 
    WHERE done !=0 
    ORDER BY id;
    '''
    c.execute(select_stmt)
    lista = c.fetchall()
    print(f"\nTask List\n{'-' * 30}")
    lista = [print(elem) for elem in lista]
    print("-" * 30)


def mark_as_done(c, task_id):
    #update the <done> field to 1 in the table for given ID
    update_stmt = '''
    UPDATE tasks
    SET done = 1
    WHERE id = %s 
    '''
    c.execute(update_stmt, (task_id))
    print(c.fetchall())

def add_new_task(c, task_name):
    #add a new task in the database
    insert_stmt = '''
    INSERT INTO tasks (task, done)
    VALUES (%s, 0)
    '''
    c.execute(insert_stmt, task_name)


# 1. Conectare la o baza de date generica
db = pymysql.connect(host, user, password, "")

with db.cursor() as c:
    c._defer_warnings = True
    c.execute("CREATE SCHEMA IF NOT EXISTS `todo_app` DEFAULT CHARACTER SET utf8;")
db.close()

# 2. Conectare la o baza de date "todo_app"
db = pymysql.connect(host, user, password, "todo_app")

# 3. Conectare table "tasks"
create_stmt = """CREATE TABLE IF NOT EXISTS `tasks` (
        id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, 
        task TEXT NOT NULL,
        done BOOLEAN);"""

with db.cursor() as c:
    c._defer_warnings = True
    c.execute(create_stmt)
    '''
    In a loop:
        ○ ask user what to do using input()
        ○ show task list
        ○ mark task as done
        ○ add new task
        ○ exit application'''
    while True:
        print('''
Menu
0. Exit application
1. Show active tasks
2. Show tasks done
3. Mark task as done
4. Add new task''')
        option = int(input("Please insert you option (0, 1, 2, 3 or 4): "))
        if option not in [0,1,2,3,4]:
            continue
        if option == 0:
            print("Bye")
            break
        elif option == 1:
            show_tasks(c)
        elif option == 2:
            show_tasks_done(c)
        elif option == 3:
            task_id = input("Please type the task ID: ")
            mark_as_done(c, task_id)
            db.commit()
        elif option == 4:
            task_name = input("Please type the task: ")
            add_new_task(c, task_name)
            db.commit()
db.close()

    
