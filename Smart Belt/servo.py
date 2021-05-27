import RPi.GPIO as GPIO
import time
import threading

class servo:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11,GPIO.OUT)
        self.servo1 = GPIO.PWM(11,50)
        self.servo1.start(0)
    
    def to0(self):
        self.servo1.ChangeDutyCycle(1)
        time.sleep(2)
        
    def to45(self):
        self.servo1.ChangeDutyCycle(5)
        time.sleep(2)
    
    def stop(self):
        self.servo1.stop()
        GPIO.cleanup()