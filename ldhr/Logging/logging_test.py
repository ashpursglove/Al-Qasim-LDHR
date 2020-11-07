import csv
import time
from time import gmtime, strftime
from datetime import datetime, timedelta


    #'+a',
with open(str(datetime.now())+'.csv','+a',  newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', 
                                quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Time'] + ['In Temp']+ ['In Hum']+['Out Temp']+ ['Out Hum']+ ['Other Temp']+ ['Other Hum']+ ['No Tank Switch']+ ['column 5']+ ['column 6'])
    
    while True:
        time.sleep(0.1)
            
        
        spamwriter.writerow([str(datetime.now()),'Lovely Spam','Wonderful Spam','Wonderful Spam','cjkhvt','666','Wonderful Spam','cvjgv,'666','ergerg'])
        