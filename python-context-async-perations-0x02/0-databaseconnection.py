#!/usr/bin/python3

from sqlite3 import connect, DatabaseError

class DatabaseConnection():
    def __init__(self):
        self.conn =  connect('alx.sqlite')
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, type, value, traceback):
        self.conn.close()
        return False


with DatabaseConnection() as cursor:
    try:
        query = 'SELECT * FROM users'
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except DatabaseError as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
