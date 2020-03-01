from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import _thread
import time

def printThread(num):
    while 1:
        print("Thread: ", num)
        time.sleep(num)

_thread.start_new_thread(printThread, (1,))
_thread.start_new_thread(printThread, (4,))

time.sleep(10)