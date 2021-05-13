import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

TRIG = 7
ECHO = 12
LED = 13

GPIO.setup(TRIG, GPIO.OUT)
GPIO.output(TRIG, 0)

GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)



time.sleep(0.1)



distance = 0
def get_data():
    GPIO.output(TRIG,1)
    time.sleep(0.00001)
    GPIO.output(TRIG,0)
    while GPIO.input(ECHO) == 0:
        pass
    start = time.time()

    while GPIO.input(ECHO) == 1:
        pass
    stop = time.time()

    return (stop - start)*17000

print(distance)



Maximum = 50

p = GPIO.PWM(LED,50)
p.start(0)

def main():
    try:
        while True:
            distance = get_data() 
            print(distance)
            percentage = ((Maximum-distance)/Maximum)*100
            print(percentage)
            if(percentage>100):
                p.ChangeDutyCycle(100)
            elif(percentage<0):
                p.ChangeDutyCycle(0)
            else:
                p.ChangeDutyCycle(percentage)
            time.sleep(1)
    except KeyboardInterrupt: 
        return 

main()


