from .connectDb import connect
import psycopg2

# return newest task from instance table 
def selectNewestByTaskId(id):
    conn = connect()
    cursor = conn.cursor()

    query = ("""SELECT * FROM task_instance WHERE task_id=%s ORDER BY datetime DESC""", [id])

    cursor.execute(query[0], query[1])

    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

# return 1 task blueprint row by task id
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

# returns all task blueprints from task table 
def selectAllTasks():
    conn = connect()

    cursor = conn.cursor()

    query = ("""SELECT * FROM tasks""")

    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    conn.close()
    return result

# returns all instances from task_instance table in a list
# [id, taskId, name, datetime]
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

def deleteTaskInstance(id): 
    conn = connect() 
    cursor = conn.cursor() 

    query = """DELETE FROM task_instance WHERE task_id=%s RETURNING *"""
    cursor.execute(query, id)
    deleted = cursor.fetchall()

    cursor.close()
    conn.close()
    return deleted

