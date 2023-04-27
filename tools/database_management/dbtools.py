from dbconnect import connect
import psycopg2

def selectNewestByTaskId(id):
    conn = connect()
    cursor = conn.cursor()

    query = ("""SELECT * FROM task_instance WHERE task_id=%s ORDER BY datetime DESC""", [id])

    cursor.execute(query[0], query[1])

    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def selectByTaskId(taskId): 
    conn = connect() 
    cursor = conn.cursor()
    query = ("""SELECT taskname FROM tasks WHERE id=%s""", [taskId])

    cursor.execute(query[0], query[1])
    result = cursor.fetchall()
    # print(taskId, result[0][0])
    cursor.close()
    conn.close()

    return result[0][0]

def selectAllTasks():
    conn = connect()

    cursor = conn.cursor()

    query = ("""SELECT * FROM tasks""")

    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    conn.close()
    return result

def showTaskInstanceTable(): 
    conn = connect() 
    cursor = conn.cursor() 

    query = """SELECT * FROM task_instance"""

    cursor.execute(query)
    task_instances = cursor.fetchall()
    cursor.close()
    conn.close()

    instances = []
    for task in task_instances: 
        
        taskname = selectByTaskId(task[2])
        instances.append([task[0], task[2], taskname, task[1]])
    for instance in instances: 
        print(f"{instance[2]}, {instance[3]}")
    return instances

