import psycopg2

def connect():
    conn = psycopg2.connect(
        database="elephant", user='postgres', password='postgres', host='localhost', port='5432'
    )
    return conn

