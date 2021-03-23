import RoboPiLib as RPL
import setup
from time import sleep

def front():
    RPL.servoWrite(0,1600)
    RPL.servoWrite(1,1400)

def back():
    RPL.servoWrite(0,1400)
    RPL.servoWrite(1,1600)

def left():
    RPL.servoWrite(0,1550)
    RPL.servoWrite(1,1400)

def right():
    RPL.servoWrite(0,1600)
    RPL.servoWrite(1,1450)

def stop():
    RPL.servoWrite(0,0)
    RPL.servoWrite(1,0)
