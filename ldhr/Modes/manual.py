import RPi.GPIO as GPIO
import time


GPIO.cleanup() # cleanup all GPIOs and close channels!!!
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



def manual_mode():
    manual_or = (GPIO.input(26))
    manual_cool = (GPIO.input(23))
    manual_inletout = (GPIO.input(24))
    manual_outletout = (GPIO.input(25))
    manual_stout = (GPIO.input(12))
    
    if manual_cool:
        GPIO.output(5, GPIO.LOW)
    else:
        GPIO.output(5, GPIO.HIGH)
            
            
    if manual_inletout:
        GPIO.output(6, GPIO.LOW)
    else:
         GPIO.output(6, GPIO.HIGH)
            
            
    if manual_outletout:
        GPIO.output(13, GPIO.LOW)
    else:
        GPIO.output(13, GPIO.HIGH)
            
            
    if manual_stout:
        GPIO.output(19, GPIO.LOW)
    else:
        GPIO.output(19, GPIO.HIGH)
    
    

