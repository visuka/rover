
import RPi.GPIO as GPIO          
from time import sleep


class Rover():
    in1 = 24
    in2 = 23
    en = 25
    l1=17
    r2=27
    en2=22
    temp1=1
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(en,GPIO.OUT)
    GPIO.setup(l1,GPIO.OUT)
    GPIO.setup(r2,GPIO.OUT)
    GPIO.setup(en2,GPIO.OUT)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(l1,GPIO.LOW)
    GPIO.output(r2,GPIO.LOW)
    p=GPIO.PWM(self.en,1000)
    p2=GPIO.PWM(self.en2,1000)
        
           
    def run(self):
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
    
        
         

r=Rover()
r.run()    
   