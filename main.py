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

import threads_sensor_motor

# Write your program here
brick.display.clear()

_thread.start_new_thread(threads_sensor_motor.updateDist, ())
_thread.start_new_thread(threads_sensor_motor.runMotor, ())

wait(15000)