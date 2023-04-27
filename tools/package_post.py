import psycopg2
from retrieval import parseEmails
from database_management.dbconnect import connect
import uuid
import datetime
from database_management.dbconnect import connect

# get new emails and wrap them in queries for the database
def package():
    msgs = parseEmails()
    queries = []
    if msgs and len(msgs) > 0:
        print("There are new task occurrences! Uploading now.")

        conn = connect()
        cursor = conn.cursor()

        for m in msgs:
            taskIdQuery = f"SELECT id FROM tasks WHERE taskname = '{m['task']}';"
            cursor.execute(taskIdQuery)
            initialid = cursor.fetchall()
            if len(initialid) > 0:
                id = initialid[0][0]
                instance_uuid = str(uuid.uuid4())
                description_datetime = datetime.datetime.now().replace(tzinfo=None).strftime("%Y-%m-%d %X")
                
                # query = """"INSERT INTO task_instance VALUES (%(id)s, %(datetime)s, %(id)s, %(description)s, %(description_datetime)s);""", ({'id': instance_uuid, 'datetime': m['when'], 'task_id': id, 'description' : "", 'description_datetime': description_datetime})

                query = """INSERT INTO task_instance VALUES (%s, %s, %s, %s, %s);""", [instance_uuid, m['when'], id, "", description_datetime]

                queries.append(query) 

        cursor.close()
        conn.close()
        return queries
    else:
        print("There are no new messages at this time.")

def post():
    # execute multiple queries to post 
    # return True or False for worked or not 
    queries = package()
    if queries: 
        conn = connect()
        cursor = conn.cursor() 
        
        for query in queries: 
            cursor.execute(query[0], query[1])
            conn.commit()
        # data = cursor.fetchone()
        # print(data)
        cursor.close()
        conn.close()
        return True
    else:
        return False
