import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
dac = dac[::-1]
# numbers = [255, 127, 64, 32, 5, 0, 256, 1, 4, 100, 15, 37, 62]
# for pin in dac:
#     GPIO.setup(pin ,GPIO.OUT)
# for number__ in numbers:
#     num = [0 for r in range(8)]
#     number = bin(number__)
#     number = list(number)
#     ind = number.index('b')
#     number = number[ind+1::]
#     if len(number)<8:
#         for i in range(8-len(number)):
#             number.append(0)
#     print(number)
#     for i in range(len(dac)):
#         GPIO.output(dac[i], int(number[i]))
#     time.sleep(1)
#     for i in range(len(dac)):
#         GPIO.output(dac[i], 0)
# GPIO.cleanup()
# number = [1, 1, 1, 1, 1, 1, 1, 0]
# for pin in dac:
#     GPIO.setup(pin ,GPIO.OUT)
# for i in range(8):
#     GPIO.output(dac[i], number[i])
leds = [24, 25, 8, 7, 12, 16, 20, 21]
aux = [2, 3, 14, 15, 18, 27, 23, 22]
for pin in leds:
    GPIO.setup(pin ,GPIO.OUT)
for pin in aux:
    GPIO.setup(pin, GPIO.IN)
while True:
    for i in range(len(aux)):
        GPIO.output(leds[i], GPIO.input(aux[i]))