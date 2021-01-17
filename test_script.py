
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
        self.GPIO.setmode(GPIO.BCM)
        self.GPIO.setup(in1,GPIO.OUT)
        self.GPIO.setup(in2,GPIO.OUT)
        self.GPIO.setup(en,GPIO.OUT)
        self.GPIO.setup(l1,GPIO.OUT)
        self.GPIO.setup(r2,GPIO.OUT)
        self.GPIO.setup(en2,GPIO.OUT)
        self.GPIO.output(in1,GPIO.LOW)
        self.GPIO.output(in2,GPIO.LOW)
        self.GPIO.output(l1,GPIO.LOW)
        self.GPIO.output(r2,GPIO.LOW)
        self.p=GPIO.PWM(en,1000)
        self.p2=GPIO.PWM(en2,1000)
        self.p.start(25)
        self.p2.start(100)
        
    def run():
        print(
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
         
    
    def high():
    def medium():
    def low():
    def forward():
    def backward():
    def left():
    def right():
    def stop():
    def exit():
    