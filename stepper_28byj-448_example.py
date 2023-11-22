# https://microcontrollerslab.com/28byj-48-stepper-motor-esp32-micropython/
# https://www.thingiverse.com/thing:2797132
from machine import Pin
from time import sleep

IN1 = Pin(4,Pin.OUT)
IN2 = Pin(16,Pin.OUT)
IN3 = Pin(17,Pin.OUT)
IN4 = Pin(5,Pin.OUT)

pins = [IN1, IN2, IN3, IN4]

suck = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
inject = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]

def pump(sequence, amount):
    rounds = 0
    while True:
        print(rounds)
        for step in sequence:
            for i in range(len(pins)):
                pins[i].value(step[i])
                rounds += 1               
                sleep(0.001)
        if rounds > amount:
            rounds = 0
            break
pump(suck, 1500)
for i in range(4):
    pump(inject, 1500)
