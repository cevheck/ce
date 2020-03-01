from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import _thread
import time

lock = _thread.allocate_lock()

def printThread(num):
    while 1:
        with lock:
            
            for i in range(0,num):
                print("thread: ("+str(i+1)+"/"+str(num)+")")
                
        time.sleep(2)

_thread.start_new_thread(printThread, (2,))
_thread.start_new_thread(printThread, (5,))

time.sleep(10)
