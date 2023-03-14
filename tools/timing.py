import schedule 
from retrieval import checkNew, loginAndSelect
from db_manipulation import package_post

tasksForDailyReport = []

def getPostNewMail():
    mail = checkNew(loginAndSelect())
    if mail: 
        queries = package_post.package(mail)
        didPost = package_post.post(queries)
        if didPost:
            print("Successfully posted tasks to the database.")
        else:
            print("Failed to post the new emails found.")
    else:
        print("No new mail to post at this time.)")

# this will run nightly at a different minute than above func
def checkIntervalTasks():
    # compares each recent date of task with an interval
    # if alert level 1
        # add to list that gets returned at the end 
    # if alert level 2
        # send email that triggers iphone shortcut, interactive notification
    # if alert level 3
        # send trigger email, trigger accountability contact 

    
    pass

schedule.every().hour.at(":20").do(getPostNewMail)