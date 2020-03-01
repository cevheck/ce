#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick  
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

import _thread
import time


motorA = Motor(Port.A)
USS = UltrasonicSensor(Port.S1)

distance = 0 
threshold = 50      #milimeters; ultrasone sensor measures between 100 and 2500 mm
lock = _thread.allocate_lock()

def runMotor():

    while True:
        
        global threshold
        with lock:
            dist = getDist()
        if (dist > threshold):
            motorA.run(360)
        else:
            motorA.stop(Stop.BRAKE)
        wait(200)        #miliseconds

def updateDist():

    f = open('USSdata','w')      #open file to log

    while True:
        
        global distance
        with lock:
            distance = USS.distance()
        brick.display.text(distance)

        f.write(str(distance)+'\n')

        wait(200)
    
def getDist():
    return distance
