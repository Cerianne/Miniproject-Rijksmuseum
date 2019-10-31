import RPi.GPIO as GPIO
import sys

rood = 17
groen = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(groen, GPIO.OUT)
GPIO.setup(rood, GPIO.OUT)

GPIO.output(groen, 0)
GPIO.output(rood, 0)

if len(sys.argv) > 1:
    cmd = sys.argv[1]

    if cmd == 'rood':
        GPIO.output(rood, 1)

    if cmd == 'groen':
        GPIO.output(groen, 1)



