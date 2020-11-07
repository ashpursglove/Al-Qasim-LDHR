import time
from time import gmtime, strftime
from datetime import datetime, timedelta








while True:
    time_now = datetime.now()
    
    x = datetime.now()
    
    
    print("\n"*100)
    
    print(x.hour)
    print(x.minute)
    print(x.strftime("%A"))
    print (time_now)
    
    time.sleep(0.1)
