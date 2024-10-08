import pyodbc
import base


def connect():
    try:
        connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + base.SERVER + ';DATABASE=' + base.DATABASE + ';Trusted_Connection=yes;'
        conn = pyodbc.connect(connection_string)
        return conn
    except Exception as e:
        print(e)


def fetch(query):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(e)


def insert(query):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(query)
        cursor.commit()
        return 'category added successfully'
    except Exception as e:
        print(e)
