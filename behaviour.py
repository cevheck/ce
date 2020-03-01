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

from subsumption import Behavior
from subsumption import Controller

USS = UltrasonicSensor(Port.S1)

distLock = _thread.allocate_lock()

#this function will be used to request the distance from the ultrasonic sensor
#it uses a lock so only one request can be handled at the same time

#if the takeControl method and action request information from the same sensor, one request could partially
#overwrite the data and then block after which the other request could read partially written data
#since they both run in parallel
def getDist():

    dist = 0
    
    with distLock:
        dist = USS.distance()
    
    return dist


class behaviorOne(Behavior):

    def __init__(self):
        self.keepRunning = True

    def takeControl(self):
        return True

    def action(self):
        
        self.keepRunning = True

        while self.keepRunning:
            print("not running motor")
            time.sleep(1)

    def suppress(self):
        
        self.keepRunning = False

class behaviorTwo(Behavior):

    motorA = Motor(Port.A)

    def __init__(self):
        pass

    def takeControl(self):

        if (getDist() > 100):
            return True
        else:
            return False
    
    def action(self):

        while (getDist() > 100):
            
            self.motorA.run(360)

        self.motorA.stop(Stop.BRAKE)
    
    def suppress(self):
        pass

#An object of the controller class is created, it has one optional argument
#whether the controller should keep running when no behavior can take control, this is false by default

cont = Controller()

#an object of each behavior class is created and add to the controller

bh2 = behaviorTwo()
bh1 = behaviorOne()

#the behavior that is added first has the highes priority, in this case bh2 has the higher priority

cont.add(bh2)
cont.add(bh1)

#this function will start the controller

cont.start()