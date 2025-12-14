from dotenv import load_dotenv, find_dotenv
import time
from datetime import datetime

def startup():
    print("\nLoading application...")
    load_dotenv(find_dotenv(), override=True)
    time.sleep(.5)

def getTime():
    now: datetime = datetime.now()
    print(f"{now:%c}")
    load_dotenv(find_dotenv(), override=True)
    time.sleep(1)