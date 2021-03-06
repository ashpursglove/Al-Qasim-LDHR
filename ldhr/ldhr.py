
import RPi.GPIO as GPIO
import time
import csv
from time import gmtime, strftime
from datetime import datetime, timedelta
from DAQ.inside import get_in_data
from DAQ.outside import get_out_data
from DAQ.other import get_other_data
from Modes.auto import auto_mode
from Modes.manual import manual_mode
from Logging.auto_log_send import autolog
from Logging.auto_log_send import autosend
from Error.error_occ import email_error

#email list 

e1= "ashley.pursglove@redseafarms.com"
e2= "ryan.lefers@redseafarms.com"
e3= "oscar.tovar@redseafarms.com"
e4= "ahmed.almashharawi@redseafarms.com"
e5= "alba.luna@redseafarms.com"








cur_filename = "nil"





no_tank_changes = 0
GPIO.cleanup() # cleanup all GPIOs and close channels!!!
log_number = 0
prog = 0 # tank switch progress tracker





hum_diff = 1 #difference in hum that causes a tank switch
switch_delay = 60 # tank switch buffer time in minutes
can_switch = True # are the tanks allowed to perform a switch
tank_switch = False

temp_setpoint = 20 # tempetature setpoint for cooling
cooling = False

data_arr = [0]*6
run = 1


''' Set up data logging'''
data_is_logging = False
dlt = datetime.now() #last datalogging time
ndl = datetime.now() # next data logging time

day_number = 0

dli = 2 # datalogging interval time in minutes
session_length = 540 #time between each data dump in minutes (1 day is 1440 minutes)
session_start = datetime.now()
following_session = datetime.now()+ timedelta(minutes = session_length)



set_time= datetime.now() #first occurance
time_now = datetime.now()


# GPIO:
# 4  - Inside greenhouse DHT22
# 17 - Outside greenhouse DHT22
# 27 - Other greenhouse DHT22
# 
# 22 - Pump 1 inlet cooling
# 5  - Pump 2 outlet cooling
# 6  - Pump 3 inlet tank out
# 13 - Pump 4 outlet tank out
# 19 - Pump 5 staging tank out
# 
# 26 - Manual Control Over-Ride
# 18 - Manual inlet cooling pump 1
# 23 - Manual outlet cooling pump 2
# 24 - Manual inlet tank out (Pump 3)
# 25 - Manual Outlet Tank out (Pump 4)
# 12 - Manual Staging Tank out (Pump 5)
# 16 - inlet float switch 
# 20 - outlet float switch
# 21 - Staging float switch

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

GPIO.setup(26, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(20, GPIO.IN)
GPIO.setup(21, GPIO.IN)


#set all outputs to off (coil high)
GPIO.output(22, GPIO.HIGH)
GPIO.output(5, GPIO.HIGH)
GPIO.output(6, GPIO.HIGH)
GPIO.output(13, GPIO.HIGH)
GPIO.output(19, GPIO.HIGH)

inlet_empty = (GPIO.input(16))
outlet_empty = (GPIO.input(20))
stage_empty = (GPIO.input(21))




print("\n"*100)
print("Finding and warming up sensors")
print("I'll be about 10 seconds!!")
print("\n"*7)





'''...............................................................................................'''



#function to get all T&H data
def get_sensor_data():
    #get data from inside sensor
    in_arr = get_in_data()
    
    
    
    data_arr[0] = in_arr[0] #inside temp
    data_arr[1] = in_arr[1] #inside hum

    #get data from outside sensor
    out_arr = get_out_data()

    data_arr[2] = out_arr[0] #outside hum
    data_arr[3] = out_arr[1]  #outside hum

    #get data from other greenhouse sensor
    other_arr = get_other_data()

    data_arr[4] = other_arr[0] #other temp
    data_arr[5] = other_arr[1]  #other hum
    #GPIO.cleanup() # cleanup all GPIOs and close channels!!!
    

    time_now = datetime.now()
    
    
    
    
    print("\n"*50)
    time.sleep(0.01)
    print("%d-%d-%d  %d:%d:%d" % (time_now.day, time_now.month,time_now.year , time_now.hour, time_now.minute, time_now.second))
    print("*******************Auto Program Running*******************")
   # print("")
    print("Number of Tank Changes: %d" %(no_tank_changes))
    print("Tank Change Threshold: %.1f%%" %(hum_diff))
    print("Switch Threshold Time:%.1f Minutes" % (switch_delay))
    print("Time of Next Data Log: %d:%d:%d" % (ndl.hour, ndl.minute, ndl.second))
    print("-----------------------------------------------------------")
    print("Inside Temperature: %.1fC" %(data_arr[0]))
    print("Inside Humidity: %.1f%%" % (data_arr[1]))
    #print("")
    print("Outside Temperature: %.1fC" %(data_arr[2]))
    print("Outside Humidity: %.1f%%" % (data_arr[3]))
    #print("")
    print("Other Greenhouse Temperature: %.1fC" %(data_arr[4]))
    print("Other Greenhouse Humidity: %.1f%%" % (data_arr[5]))
    print("-----------------------------------------------------------")
    print("Tank Switch Condition Met: %r " %(tank_switch))
    #print("")
    print("Passed Switch Time Allowance: %r" % (can_switch))
   # print("")
    print("Cooling On: %r " %(cooling))
   # print("")
    print("Press Control + C to Exit Program")
   # print("")
    print("*******************Auto Program Running*******************")
    print("")
    
    return data_arr



try:
    #main program

    while True:
  
        if datetime.now() >= set_time:
            can_switch = True
              
              
              #AUTO MODE....................................................................
              
        while run == 1:
            
            
    #         data_is_logging = datalog(data_is_logging,data_arr[0],data_arr[1],data_arr[2],data_arr[3],data_arr[4],data_arr[5],99)
            
            if datetime.now() >= set_time:
                can_switch = True
            
            get_sensor_data()
            
            auto_return = auto_mode(data_arr[0],temp_setpoint,data_arr[1],data_arr[3],hum_diff) # runs the auto program here and returns paramaters
            
            
            tank_switch = auto_return[0]
            cooling = auto_return[1]
            


               # see if manual switch has been flipped
            if GPIO.input(26):
                run = 2
            
            if tank_switch and can_switch:
                run = 3
                
                
                
    #DATA LOGGING.........................................'''
                


            if data_is_logging == False:
                
                new_time = datetime.now()
                cur_filename = "/home/pi/code/ldhr/ldhr/Logging/" + "%d-%d-%d  %d:%d" % (new_time.day, new_time.month,new_time.year ,new_time.hour, new_time.minute)
        
            
            autolog_return = autolog(data_is_logging,ndl, cur_filename, dli, data_arr, no_tank_changes, cooling)
            
            ndl = autolog_return[0]
            data_is_logging = autolog_return[1]
            

    #END OF DATA LOGGING........................................  
            
    #DATA SENDING.........................................'''

            
            autosend_return = autosend(session_length, session_start, following_session, data_is_logging,cur_filename)
            
            data_is_logging = autosend_return[0]
            session_start = autosend_return[1]
            following_session = autosend_return[2]
            
            
           
            print(session_start)
            print(following_session)

            
          
            
            
            
            
            #...................................................................................
            
            
                
            
            
            
            
            
            
            
            
            #Manual mode................................................................
            
            
        while run == 2:
            manual_or = (GPIO.input(26))
            
            if manual_or == 0:
                run = 1
            
            manual_mode()
            
            print("\n"*100)
            print("*******************Manual Mode*******************")
            print("\n"*5)
            print("             Manual Mode Engaged")
            print("\n")
            print("         Use Switches to control Outputs")
            print("\n"*5)
            print("*******************Manual Mode*******************")
            print("\n"*2)
            time.sleep(0.1)
            



         #...........................................................................................


    # Tank Switch.............................................................................
                

        while run ==3:
            time.sleep(0.2)
            inlet_empty = (GPIO.input(16))
            outlet_empty = (GPIO.input(20))
            stage_empty = (GPIO.input(21))
            time.sleep(0.2)
            print("\n"*50)
            print("*******************Tank Switch in Progress*******************")
            print("")
            print("Tank Switch")
            print("")
            print("Next Tank Switch allowed in %.1f Minutes" % (switch_delay))
            print("")
            print("program Step: %s" % (prog))
            print("")
            
            #print("inlet empty: %r" % (inlet_empty))
            if prog == 0:
                GPIO.output(6, GPIO.LOW)
                print("Moving Inlet Tank to Staging Tank")
                if inlet_empty == 0:
                    prog = 1
            
            if prog ==1:
                GPIO.output(6, GPIO.HIGH)
                GPIO.output(13, GPIO.LOW)
                print("Moving Outlet Tank to Inlet Tank")
                if outlet_empty == 0:
                    prog = 2
                    
            if prog == 2:
                GPIO.output(13, GPIO.HIGH)
                GPIO.output(19, GPIO.LOW)
                print("Moving Staging Tank to Outlet Tank")
                if stage_empty == 0:
                    GPIO.output(19, GPIO.HIGH)
                    print("Tank Switch Complete, Moving Back to Main Program")
                    
                    set_time = datetime.now()+ timedelta(minutes = switch_delay) #sets time limit until next switch
                    can_switch = False
                    prog = 0
                    run = 1
                    no_tank_changes = no_tank_changes +1
            print("\n"*2)
            print("*******************Tank Switch in Progress*******************")
            print("\n"*4)
    #................................................................
            
            
except Exception as error:
    
    print("there has been an error")
    print("\n")
    print(error)
    
    email_error(e1, str(error))
    email_error(e2, str(error))
    email_error(e3, str(error))
    email_error(e4, str(error))
    email_error(e5, str(error))
            
            

    

