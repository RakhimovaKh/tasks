import sqlite3

'''Create table students in teatchers.db'''

# connection = sqlite3.connect('teatchers.db')
# cursor = connection.cursor()
# query = """CREATE TABLE Students
# (
# Student_Id INTEGER NOT NULL PRIMARY KEY,
# Student_Name TEXT NOT NULL,
# School_ID INTEGER NOT NULL
# );
# """
# cursor.execute(query)
# connection.commit()
# connection.close()

'''Fill table students'''

# connection = sqlite3.connect('teatchers.db')
# cursor = connection.cursor()
# query = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
# VALUES
# (201, 'Иван', 1),
# (202, 'Петр', 2),
# (203, 'Анастасия', 3),
# (204, 'Игорь', 4);
# """
# cursor.execute(query)
# connection.commit()
# connection.close()

def get_connection():
    connection = sqlite3.connect('teatchers.db')
    return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_school_name(school_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT * FROM School WHERE School_Id = ?"""
    cursor.execute(select_query, (school_id,))
    record = cursor.fetchone()
    close_connection(connection)
    return record[1] # Наименование школы
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных по школе ", error)

def get_students_detail(school_id):
    try:
      school_name = get_school_name(school_id)
      connection = get_connection()
      cursor = connection.cursor()
      select_query = """SELECT * FROM Students WHERE School_Id = ?"""
      cursor.execute(select_query, (school_id,))
      records = cursor.fetchall()
      print ("Данные по студентам")
      for row in records:
        print ("ID студента", row[0])
        print ("Имя студента", row[1])
        print ("ID школы", row[2])
        print ("Название школы", school_name)
      close_connection(connection)
    except (Exception, sqlite3.Error) as error:
      print ("Ошибка в получении данных ", error)

print ("Задача данные по студентам")
get_students_detail(1)