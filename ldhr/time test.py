import time
from time import gmtime, strftime
from datetime import datetime, timedelta








switch_delay = 0.5 # in minutes
time_now = datetime.now()
set_time = datetime.now()+ timedelta(minutes = minutes_to_add)

can_switch = True
print (time_now)

print(set_time)

while True:
    time_now = datetime.now()
    print("\n"*100)
    print (time_now)
    print(set_time)
    
    if time_now>set_time:
        good = True
    print(good)
    time.sleep(0.1)
    