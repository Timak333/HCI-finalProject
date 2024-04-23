import sqlite3

connection = sqlite3.connect('database.db')

def execute_sql_file(file_path):
    with open(file_path, 'r') as f:
        connection.executescript(f.read())

try:
    execute_sql_file('schema.sql')
    execute_sql_file('mentor_info.sql')
    connection.commit()
except sqlite3.Error as e:
    print("Error occurred:", e.args[0])
finally:
    connection.close()
