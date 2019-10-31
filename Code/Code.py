import RPi.GPIO as GPIO

GPIO.setwarnings(False)

seq = []
for i in range(4):
    digit = None
    while digit == None:
        digit = kp.getkey()
    seq.append(digit)

    print(seq)

    if seq == [1, 2, 3, '#']:
        print ('Code accepted') # hier moeten die lampjes verschillende kleuren worden


print ('Typ je code in')
