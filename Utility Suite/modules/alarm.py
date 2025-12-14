from plyer import notification as plyer_notification
import time

def notification():  
    plyer_notification.notify(
        title="Alarm",
        message="Time is up!",
        timeout=10
    )
    
def minutes(minutes_fetched):
    for i in range(minutes_fetched, 0, -1):
        time.sleep(60)
        if i == 1:
            notification()
    
def seconds(seconds_fetched):
    for i in range(seconds_fetched, 0, -1):
        time.sleep(1)
        if i == 1:
            notification()