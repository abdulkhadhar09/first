import RPi.GPIO as GPIO
from time import sleep

pul = 17
dire = 27
ena = 22


GPIO.setmode(GPIO.BCM)
GPIO.setup(pul, GPIO.OUT)
GPIO.setup(dire, GPIO.OUT)
GPIO.setup(ena, GPIO.OUT)

GPIO.output(ena, GPIO.LOW)
GPIO.output(dire, GPIO.LOW)

def steppulse():
    GPIO.output(pul, GPIO.HIGH)
    sleep(0.0001)
    GPIO.output(pul, GPIO.LOW)
    sleep(0.0001)

def rotmotor(steps, direction):
    GPIO.output(dire, direction)
    for i in range(steps):
        steppulse()
        
rotmotor(200, GPIO.LOW)
GPIO.output(ena, GPIO.HIGH)
GPIO.cleanup()