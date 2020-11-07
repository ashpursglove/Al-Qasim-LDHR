import csv
import time
from time import gmtime, strftime
from datetime import datetime, timedelta

cur_filename = 'xxx'

def datalog(logging,intmp, inhum, outtmp, outhum, othtmp, othhum, notkswt  ):
    
    
    if logging == False:
        cur_filename = str(datetime.now())
        
        with open(cur_filename+'.csv','+a',  newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ', 
                                    quotechar=' ', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['Time'] + ['In Temp']+ ['In Hum']+['Out Temp']+ ['Out Hum']+ ['Other Temp']+ ['Other Hum']+ ['No Tank Switch']+ ['column 5']+ ['column 6'])
        
        return True
    
        
    
    
    else:
        time.sleep(0.1)
        with open(cur_filename+'.csv','+a',  newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([str(datetime.now()),intmp,inhum,outtmp,outhum,othtmp,othhum,notkswt,'666','ergerg'])
            
