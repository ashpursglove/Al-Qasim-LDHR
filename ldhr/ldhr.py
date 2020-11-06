# from get_data import get_data
import RPi.GPIO as GPIO
import time
from DAQ.inside import get_in_data
from DAQ.outside import get_out_data
from DAQ.other import get_other_data

log_number = 0

tank_switch = False

temp_setpoint = 20
cooling = False

data_arr = [0]*6
run = 0




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
    GPIO.cleanup() # cleanup all GPIOs and close channels!!!
    
    print("\n"*100)
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

if run == 0:
    r = input("Press r and enter to run program ")
    if r == "r":
        print("Press Ctrl + C to halt Program")
        time.sleep(2)
        run = 1
        r = "x"
        
while run == 1:
    get_sensor_data()
    log_number += 1
    
    
    
    
    
  #if the inside is less than 5% different from outside    1 = inside hum, 3 = outside hum
    if data_arr[1] <= data_arr[3]+5:
        tank_switch = True
        
        
    if data_arr[0] >= temp_setpoint:
        cooling = True
        
        
        
    

        
        

    

