import email 
import imaplib
import uuid
import datetime
from database_management.connectDb import connect

# return connection object
def loginAndSelect():
    imap_server = "imap.gmail.com" 
    email_address = "elephantclient1@gmail.com"
    password = "evatdawaocuiaief"
    # password = "elephantyikes"

    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(email_address, password)
    imap.select("Inbox")
    return imap

def imapifyDate(date):
    return date.strftime("%d-%b-%Y")

def strptimeEmail(message):
    try:
        messagedate = datetime.datetime.strptime(message.get('Date'), "%a, %d %b %Y %H:%M:%S %z")
    except: 
        messagedate = datetime.datetime.strptime(message.get('Date'), "%a, %d %b %Y %H:%M:%S %Z")
    finally:
        messagedate = messagedate.replace(tzinfo=None)
        return messagedate

def postgresifyDateTime(date):
    return date.replace(tzinfo=None).strftime("%Y-%m-%d %X")

def getMostRecentDate(): 
      # grab the most recent date with select 
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""SELECT datetime FROM task_instance ORDER BY datetime DESC;""")

    d = cursor.fetchone()
    date = d[0].replace(tzinfo=None)
    cursor.close()
    conn.close()

    return date


# return msgnums of new messages
def checkNew(imap):
    date = getMostRecentDate()

    imapDate = imapifyDate(date)

    # formattedRecentDate = recentDate.strftime("%d-%b-%G")
    isOk, msgnums = imap.search(None, f'(SINCE "{imapDate}")')
    newMessageNums = []
    if isOk == "OK": 

        conn = connect()
        cursor = conn.cursor()
        cursor.execute("""SELECT """)
        for m in msgnums[0].split():
            typ, data = imap.fetch(m, '(RFC822)')
            if typ == "OK":
                message = email.message_from_bytes(data[0][1])
                print(message.get('Date'))
                # produce a datetime object
                messagedate = strptimeEmail(message)
                dif = messagedate - date
                if int(dif.total_seconds()) > 0:
                    newMessageNums.append(m)
        
        return newMessageNums
       
    else:
        print(f'Error code: {isOk}')
        return False


# var: email ids, imap session
# retrieves emails with ids
# creates uuid for the occurrence
# creates object for each task, later used to create an insert query
# returns list of objects
def parseEmails(): 
    
    imap = loginAndSelect()
    msgnums= checkNew(imap)
    if msgnums:
        tasks = []
        for num in msgnums:
            typ, data = imap.fetch(num, '(RFC822)')
            if typ == "OK":
                message = email.message_from_bytes(data[0][1])
                u = uuid.uuid4()
                # turn the message date into a datetime object
                date = strptimeEmail(message)
                # construct the task item 
                item = {"uuid" : u,
                        "when" : date.replace(tzinfo=None).strftime("%Y-%m-%d %X"),
                        "task" : message.get('Subject')}

                tasks.append(item)
            else:
                print(f"Error: {typ}")
        return tasks
    else:
        return False

    



