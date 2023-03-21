from dbconnect import connect
import psycopg2

def selectNewestByTaskId(id):
    conn = connect()
    cursor = conn.cursor()

    query = ("""SELECT * FROM task_instance WHERE task_id=%s ORDER BY datetime DESC""", [id])

    cursor.execute(query[0], query[1])

    result = cursor.fetchone()
    print(result)
    cursor.close()
    conn.close()
    return result

def selectAllTasks():
    conn = connect()

    cursor = conn.cursor()

    query = ("""SELECT * FROM tasks""")

    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

    cursor.close()
    conn.close()
    return result





