import os, glob, time,csv
import time
import Adafruit_DHT
import RPi.GPIO as GPIO



DHT_SENSOR1 = Adafruit_DHT.DHT22
DHT_SENSOR2 = Adafruit_DHT.DHT22
DHT_SENSOR3 = Adafruit_DHT.DHT22
DHT_PIN1 = 4 #inside GH
DHT_PIN2 = 17 # outsude GH
DHT_PIN3 = 27 #othher normal greenhouse inside


arr=[]
arr = [0 for i in range(2)] 

GPIO.setmode(GPIO.BCM)


def get_out_data():
    
    values = [0]*3
    for i in range(1):
        values[i] = Adafruit_DHT.DHT22
        humidity, temperature_c = Adafruit_DHT.read_retry(DHT_SENSOR2, DHT_PIN2)
        temperature_f = temperature_c * ( 9 / 5 ) + 32
        
        values[0]=temperature_c
        values[1]=temperature_f
        values[2]=humidity
            
        outsidetemp = values[0]
        outsidehum = values[2]
        
        arr[0] = outsidetemp
        arr[1] = outsidehum

    
    return arr
