#!/usr/bin/python3

from sqlite3 import connect, DatabaseError, OperationalError

class ExecuteQuery:
    """
    context manager that takes a query as input
    and executes it, managing both connection
    and the query execution
    """
    def __init__(self, query, *params):
        self.conn = None
        self.cursor = None
        self.query = query
        self.params = [*params] if params else []

    def __enter__(self):
        try:
            self.conn = connect('alx.sqlite')
            self.cursor = self.conn.cursor()
            self.cursor.execute(self.query, self.params)
            return self.cursor.fetchall()
        except (OperationalError, DatabaseError) as e:
            print(f'Query Failed: {e}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
        return False


def run_query(query, *params):
    with ExecuteQuery(query, *params) as results:
        return results

print(run_query('SELECT * FROM users WHERE age > ?', 25))
