# from get_data import get_data
import RPi.GPIO as GPIO
from inside import get_in_data







outsidetemp = 0
outsidehum = 0

othertemp = 0
otherhum = 0


in_arr = get_in_data()

insidetemp = in_arr[0]
insidehum = in_arr[1]

print("inside temperature: %.1fC" %(insidetemp))
print("inside humidity: %.1f Percent" % (insidehum))


