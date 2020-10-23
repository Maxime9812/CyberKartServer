import RPi.GPIO as GPIO

class Motor:
    def __init__(self):
        self.pin = 11
        GPIO.setup(self.pin,GPIO.OUT)
    
    def forward(self):
        GPIO.output(self.pin,GPIO.HIGH)
    
    def stop(self):
        GPIO.output(self.pin,GPIO.LOW)
        