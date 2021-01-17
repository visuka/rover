
import RPi.GPIO as GPIO          
from time import sleep


class Rover():
    def __init__(self):
        self.in1 = 24
        self.in2 = 23
        self.en = 25
        self.l1=17
        self.r2=27
        self.en2=22
        self.temp1=1
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.in1,GPIO.OUT)
        GPIO.setup(self.in2,GPIO.OUT)
        GPIO.setup(self.en,GPIO.OUT)
        GPIO.setup(self.l1,GPIO.OUT)
        GPIO.setup(self.r2,GPIO.OUT)
        GPIO.setup(self.en2,GPIO.OUT)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)
        GPIO.output(self.l1,GPIO.LOW)
        GPIO.output(self.r2,GPIO.LOW)
        p=GPIO.PWM(self.en,1000)
        p2=GPIO.PWM(self.en2,1000)
        
        
    def run():
        print("running")
        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2,GPIO.LOW)
         
         

r=Rover()
r.run()    
   