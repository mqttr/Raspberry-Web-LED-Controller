import RPi.GPIO as GPIO
import time
from signal import pause

class controller:
    def __init__(self):
        self.light = 12
        self.button = 18
    
    def setup(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.light, GPIO.OUT)
        GPIO.setup(self.button, GPIO.IN)
    
    def set_on(self):
        GPIO.output(self.light, GPIO.HIGH)
    
    def set_off(self):
        GPIO.output(self.light, GPIO.LOW)
    
    def clean_up(self):
        GPIO.output(light, GPIO.LOW)
        GPIO.cleanup()
    