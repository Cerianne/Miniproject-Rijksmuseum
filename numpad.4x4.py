import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

matrix = [ [1, 2, 3, 'A']
           [4, 5, 6, 'B']
           [7, 8, 9, 'C']
           ['*', 0, '#', 'D'] ]

row = [7, 11, 13, 15]
colom = [12, 16, 18, 22]

for j in range(4):
    GPIO.setup(colom[j], GPIO.OUT)
    GPIO.output(colom[j], 1)

for i in range(4):
    GPIO.setup(row[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    while (True):
        for j in range(4):
            GPIO.output(colom[j], 0)

            for i in range(4):
                if GPIO.input(row[i]) == 0:
                    print matrix[i][j]
                    while (GPIO.input(row[i]) == 0):
                        pass

            GPIO.output(colom[j], 1)

except KeyboardInterrupt:
    GPIO.cleanup()