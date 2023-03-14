import psycopg2
from datetime import timedelta

tasks = [(1, 'Meeting', '8 days', 2),
         (2, 'Attendance Submitted', '24 hours', 2),
         (3, 'Assignment Completed', '2 years', 1),
         (4, 'Collaboration', '8 days', 1),
         (5, 'Physical Therapy', '48 hours', 2),
         (6, 'Took Meds', '2 years', 2),
         (7, 'Ate', '5 hours', 2),
         (8, '24 oz water', '6 hours', 1),
         (9, 'Saw Doctor', '2 years', 2),
         (10, 'Medical Clerical', '2 years', 2),
         (11, 'Catbox', '2 days', 1),
         (12, 'Feed Finn', '2 years', 1),
         (13, 'Budget and Finances', '15 days', 2)]

def makeQueries():
    queries = []
    for task in tasks:
        query = f"INSERT INTO tasks VALUES {task};"
        queries.append(query)

    return queries

def postTasks():
    conn = psycopg2.connect(
        database="elephant", user='postgres', password='postgres', host='localhost', port='5432'
    )
    cursor = conn.cursor() 
    queries = makeQueries()
    for q in queries: 
        cursor.execute(q)
        conn.commit()
    
    cursor.execute('SELECT * FROM tasks;')
    data = cursor.fetchall()
    
    cursor.close()
    conn.close()

# postTasks()