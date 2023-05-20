# elephant

This is a task-tracking and lifestyle sustainability solution, created for my personal use. It is currently still in development, though it is functional on a basic level. 

**Automatic Operations**
    timed_execution.py 
    - getPostNewMail() -> runs on the hour at :20
        - check for new tasks completed
        - posts them to the database if they exist
    - checkIntervalLapsesAndNotify() -> runs on the hour at :30
        - check for tasks that have not been done within the required amount of time. 
        - If there are tasks that need to be done, email is sent to the designated notification reciever. Contains: 
            - Name of task
            - Time elapsed since last completed 
            - Maximum amount of time allowed to elapse before notification is sent

