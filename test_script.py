
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
        self.GPIO=GPIO.setmode(GPIO.BCM)
        
        
    def run():
        print("running")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
         
         

r=Rover()
r.run()    
   