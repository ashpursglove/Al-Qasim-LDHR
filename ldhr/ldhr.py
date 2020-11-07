
import RPi.GPIO as GPIO
import time
from DAQ.inside import get_in_data
from DAQ.outside import get_out_data
from DAQ.other import get_other_data
from Modes.auto import auto_mode
from Modes.manual import manual_mode


GPIO.cleanup() # cleanup all GPIOs and close channels!!!
log_number = 0

tank_switch = False

temp_setpoint = 24
cooling = False

data_arr = [0]*6
run = 1





# GPIO:
# 4  - Inside greenhouse DHT22
# 17 - Outside greenhouse DHT22
# 27 - Other greenhouse DHT22
# 
# 
# 5  - Pump 1 inlet cooling, Pump 2 outlet cooling, fans
# 6  - Pump 3 inlet tank out
# 13 - Pump 4 outlet tank out
# 19 - Pump 5 staging tank out
# 
# 26 - Manual Control Over-Ride
# 18 - Manual Fan
# 23 - Manual Cooling pumps (1&2)
# 24 - Manual inlet tank out (Pump 3)
# 25 - Manual Outlet Tank out (Pump 4)
# 12 - Manual Staging Tank out (Pump 5)
# 16 - inlet float switch 
# 20 - outlet float switch
# 21 - Staging float switch

GPIO.setmode(GPIO.BCM)

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
GPIO.output(5, GPIO.HIGH)
GPIO.output(6, GPIO.HIGH)
GPIO.output(13, GPIO.HIGH)
GPIO.output(19, GPIO.HIGH)



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
    
    print("\n"*100)
    print("Auto Program Running")
    print("")
    print("Log Number: %d" %(log_number))
    print("")
    print("Inside Temperature: %.1fC" %(data_arr[0]))
    print("Inside Humidity: %.1f Percent" % (data_arr[1]))
    print("")
    print("Outside Temperature: %.1fC" %(data_arr[2]))
    print("Outside Humidity: %.1f Percent" % (data_arr[3]))
    print("")
    print("Other Greenhouse Temperature: %.1fC" %(data_arr[4]))
    print("Other Greenhouse Humidity: %.1f Percent" % (data_arr[5]))
    print("")
    print("Tank Switch: %r " %(tank_switch))
    print("Cooling On: %r " %(cooling))
    print("")
    
    return data_arr




#main program

while True:      
          
          
          #AUTO MODE....................................................................
          
    while run == 1:
        
        get_sensor_data()
        
        auto_return = auto_mode(data_arr[0],temp_setpoint,data_arr[1],data_arr[3])
        
        tank_switch = auto_return[0]
        cooling = auto_return[1]

           # see if manual switch has been flipped
        if GPIO.input(26):
            run = 2
        
        
        log_number += 1
        
        #...................................................................................
        
        
            
        
        
        
        
        
        
        
        
        #Manual mode................................................................
        
        
    while run == 2:
        manual_or = (GPIO.input(26))
        
        if manual_or == 0:
            run = 1
        
        manual_mode()
        
        print("\n"*100)
        print("manual mode")



     #...........................................................................................

            
            
        

            
            

    
