import RoboPiLib as RPL
import setup
from time import sleep

def down(pin):
    RPL.servoWrite(pin,1600)

def up(pin):
    RPL.servoWrite(pin,1400)

def stop(pin):
    RPL.servoWrite(pin,0)
