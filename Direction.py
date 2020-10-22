import RPi.GPIO as GPIO

class Direction:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD) # Use board numerotation mode
        GPIO.setWarning(False) # Disable warning
    
        GPIO.setup(pwm_gpio,GPIO.OUT)
        
        self.pin = 12
        self.frequence = 50
        self.pwm = GPIO.PWM(self.pin,self.frequence)
        
        self.resetPosition()
        
    def resetPosition(self):
        self.changeRotation(angle_to_percent(80))
    
    def changeRotation(angle):
        self.rotation = angle_to_percent(angle)
        pwm.start(self.rotation)
 
 
def angle_to_percent(angle):
    if angle > 180 or angle < 0:
        print("Error Angle not in range", angle)
        return False
        
    start = 4
    end = 12.5
    ratio = (end - start) / 180
    
    angle_as_percent = angle * ratio
    return start + angle_as_percent

    
