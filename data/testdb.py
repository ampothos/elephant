import psycopg2

conn = psycopg2.connect(database="postgres", user="poster", password="", host='localhost', port='5432')

conn.autocommit = True

cursor = conn.cursor()

sql = '''CREATE database mydb''';

cursor.execute(sql)
print("Db created successfully")

conn.close()