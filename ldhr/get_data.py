import os, glob, time,csv
import time
import Adafruit_DHT
import RPi.GPIO as GPIO
from datetime import datetime 

DHT_SENSOR1 = Adafruit_DHT.DHT22
DHT_SENSOR2 = Adafruit_DHT.DHT22
DHT_SENSOR3 = Adafruit_DHT.DHT22
DHT_PIN1 = 4
DHT_PIN2 = 17
DHT_PIN3 = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

# Print nice channel column headers.
print('-' * 87)
print('     Sensor#,    Date,      Time,     Tem.(C),    Temp.(F)     Hum.(%)')
print('-' * 87)

# Create csv file with headers
if not os.path.isfile('dataLog.csv'):
    with open('dataLog.csv', mode='w') as dataLog_file:
            dataLog_writer = csv.writer(dataLog_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            dataLog_writer.writerow(['Sensor#', 'Date-Time', 'Temp_C', 'Temp_F', 'Humidity', 'Pump_Status'])

# Main program loop.
while True:
    try:
        values = [0]*3
        for i in range(1):
            values[i] = Adafruit_DHT.DHT22
            humidity, temperature_c = Adafruit_DHT.read_retry(DHT_SENSOR1, DHT_PIN1)
    
            temperature_f = temperature_c * ( 9 / 5 ) + 32
            values[0]=temperature_c
            values[1]=temperature_f
            values[2]=humidity
            d=datetime.now()
            print('Sensor 1 | {:%Y-%m-%d  %H:%M:%S}    |   {:.1f} C    |   {:.1f} F   |    {:.1f} |'.format(d, values[0], values[1], values[2]))
        
        with open('dataLog.csv', mode='w') as dataLog_file:
            dataLog_writer = csv.writer(dataLog_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            dataLog_writer.writerow(['Sensor-1', '{:%Y-%m-%d  %H:%M:%S}'.format(d), '{:.1f} C'.format(values[0]), '{:.1f} F'.format(values[1]), '{:.1f}'.format(values[2]), 'Pump_Status'.format(values[2])])


    #time.sleep(5)

        values = [0]*3
        for i in range(1):
            values[i] = Adafruit_DHT.DHT22
            humidity, temperature_c = Adafruit_DHT.read_retry(DHT_SENSOR2, DHT_PIN2)
    
            temperature_f = temperature_c * ( 9 / 5 ) + 32
            values[0]=temperature_c
            values[1]=temperature_f
            values[2]=humidity
            d=datetime.now()
            print('Sensor 2 | {:%Y-%m-%d  %H:%M:%S}    |   {:.1f} C    |   {:.1f} F   |    {:.1f} |'.format(d, values[0], values[1], values[2]))
        with open('dataLog.csv', mode='w') as dataLog_file:
            dataLog_writer = csv.writer(dataLog_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            dataLog_writer.writerow(['Sensor-1', '{:%Y-%m-%d  %H:%M:%S}'.format(d), '{:.1f} C'.format(values[0]), '{:.1f} F'.format(values[1]), '{:.1f}'.format(values[2]), 'Pump_Status'.format(values[2])])
    #time.sleep(5)

        values = [0]*3
        for i in range(1):
            values[i] = Adafruit_DHT.DHT22
            humidity, temperature_c = Adafruit_DHT.read_retry(DHT_SENSOR3, DHT_PIN3)
    
            temperature_f = temperature_c * ( 9 / 5 ) + 32
            values[0]=temperature_c
            values[1]=temperature_f
            values[2]=humidity
            d=datetime.now()
            print('Sensor 3 | {:%Y-%m-%d  %H:%M:%S}    |   {:.1f} C    |   {:.1f} F   |    {:.1f} |'.format(d, values[0], values[1], values[2]))
        with open('dataLog.csv', mode='w') as dataLog_file:
            dataLog_writer = csv.writer(dataLog_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            dataLog_writer.writerow(['Sensor-1', '{:%Y-%m-%d  %H:%M:%S}'.format(d), '{:.1f} C'.format(values[0]), '{:.1f} F'.format(values[1]), '{:.1f}'.format(values[2]), 'Pump_Status'.format(values[2])])
    #time.sleep(5)



        if values[0] <27:
             GPIO.output(12, 0)
             print("PUMP is OFF")   #record the status of PUMP
             pump_status=0;
        else:
             GPIO.output(12, 1)
             print("PUMP is ON)")
             pump_status=1;         #record the status of PUMP

    except:

                GPIO.output(12, 0)
                print("Exception occured, pump is OFF")

    time.sleep(1)

