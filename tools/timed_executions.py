import schedule 
from package_post import post
from database_management.dbtools import selectNewestByTaskId, selectAllTasks
import datetime
from smtplib import SMTP_SSL, SMTP_SSL_PORT
from email.message import EmailMessage
from make_email import makeSendEmail

tasksForDailyReport = []

def getPostNewMail():
    didPost = post()
    if didPost: 
        print("Successfully posted tasks to the database.")
    else:
        print("No new mail to post at this time.)")

# this will run hourly at a different minute than above func
#  ensures intervals are obeyed and none have exceeded
def checkIntervalLapsesAndNotify():
    #compile the task db into a dict of taskname : {task id: id, task interval : interval}
    tasksFromDb = selectAllTasks()
    
    taskInfo = {}
    for tasks in tasksFromDb:
        taskInfo[tasks[1]] = {"id" : tasks[0],
                             "interval": tasks[2],
                             "criticality" : tasks[3]}
    for task, item in taskInfo.items():
        # print(task, item)

        # get newest for each taskname ad store the id in this var
        newest = selectNewestByTaskId(item['id'])
        
        if newest is not None:
            howLongSinceLast = datetime.datetime.now() - newest[1]
            print(task, item)
            print(howLongSinceLast - item["interval"])
            print()
            if howLongSinceLast - item["interval"] > datetime.timedelta(seconds=0):
                # blanket add task to daily report of tasks overdue 
                tasksForDailyReport.append({"item" : task,
                                            "interval" : item["interval"],
                                            "timeSince" : howLongSinceLast }) 
                # for attendance, make sure it is not the weekend
                if item["criticality"] == 2:
                    # if it's been double time interval, move to criticality 3
                    # establish an edit db task criticality func to import here 
                    
                    body = f'Time since last occurrence: {howLongSinceLast}\n Maximum time expected: {item["interval"]}'
                    from_email = "elephantclient1@gmail.com"
                    to_email = "thewateringholesender@gmail.com"

                    maildict = {'from_email' : from_email,
                                'to_email': to_email, 
                                'subject' : task,
                                'body' : body,
                                'from_pass' : 'evatdawaocuiaief'}
                    # create an email with the task as the subject for interval breach alert 
                    makeSendEmail(maildict)

                elif (item["criticality"] == 3):
                    # send trigger email to accountability contact 
                    pass



    print(tasksForDailyReport)

        # trueInterval = datetime.datetime.now() - newest

        # compares each recent date of task with an interval
        # if alert level 1
            # add to list that gets returned at the end 
        # if alert level 2
            # send email that triggers iphone shortcut, interactive notification
        # if alert level 3
            # send trigger email, trigger accountability contact 

# schedule.every().hour.at(":20").do(getPostNewMail)
# schedule.every().hour.at(":30").do(checkIntervalLapsesAndNotify)
getPostNewMail()