import RPi.GPIO as GPIO
import time
i = 0
jump_time = 0.1




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

# On relay board, relays coils are on when pin is low!

while True:
    GPIO.setmode(GPIO.BCM)
    
    GPIO.output(5, GPIO.LOW)
    time.sleep(jump_time)
    GPIO.output(5, GPIO.HIGH)
    time.sleep(jump_time)

    GPIO.output(6, GPIO.LOW)
    time.sleep(jump_time)
    GPIO.output(6, GPIO.HIGH)
    time.sleep(jump_time)
    
    GPIO.output(13, GPIO.LOW)
    time.sleep(jump_time)
    GPIO.output(13, GPIO.HIGH)
    time.sleep(jump_time)
    
    GPIO.output(19, GPIO.LOW)
    time.sleep(jump_time)
    GPIO.output(19, GPIO.HIGH)
    time.sleep(jump_time)
    

   
    print(i)
    print("Inlet Float: %r" %(GPIO.input(23)))
    print("Outlet Float: %r" %(GPIO.input(24)))
    print("Staging Float: %r" %(GPIO.input(21)))
    i += 1
    