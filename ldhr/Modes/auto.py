import RPi.GPIO as GPIO
import time


GPIO.cleanup() # cleanup all GPIOs and close channels!!!

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


manual_or = (GPIO.input(26))
inlet_empty = (GPIO.input(16))
outlet_empty = (GPIO.input(20))
stage_empty = (GPIO.input(21))
    
    

    
def auto_mode(in_temp,set_point,in_hum,out_hum,hum_diff):
    
    tank_switch = False
    cooling = False
    
    

        
        
#     if the inside is less than 5% different from outside    1 = inside hum, 3 = outside hum
    if in_hum <= out_hum +hum_diff: 
        tank_switch = True
            
      # if temperature is above setpoint turn on cooling
    if in_temp >= set_point:
        GPIO.output(22, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        cooling = True
    else:
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)

    return tank_switch, cooling

