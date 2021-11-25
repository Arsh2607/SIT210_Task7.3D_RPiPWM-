import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

trig = 23 ## trigger pin for HC SR04
echo = 24 ## echo pin for GC SR04
led = 18  ## settig the pin for PWM led

GPIO.setwarnings(False)
GPIO.setup(trig, GPIO.OUT) ## sets as an output pin
GPIO.setup(echo, GPIO.IN)## sets as an input pin
GPIO.setup(led, GPIO.OUT)
led = GPIO.PWM(led, 100)

GPIO.output(trig, False)
time.sleep(2)


def Distance_Calculator(): ## function to calculate the distace using HCSR)4 sensor
    GPIO.output(trig, 1)
    time.sleep(0.00001)
    GPIO.output(trig, 0)
    start = time.time()
    end = time.time()

    while (GPIO.input(echo) == 0):
        start = time.time()

    while (GPIO.input(echo) == 1):
        end = time.time()
        
    time = end-start
    val = (time*34300)/2
    return val



val_i = Distance_Calculator()

try:
    while 1:
        distance = Distance_Calculator()
        if (distance > 200):
            print("Out of range")
            
        elif (distance > 60):
            led.ChangeDutyCycle(0)
            print("Distance ==> ", distance)
        else:
            led.ChangeDutyCycle(100 - (3*val_i))
            print("Distance ==> ", distance)
            val_1 = distance
        time.sleep(0.5)

except:
    print("Error in setup.")

finally:
    GPIO.cleanup()
