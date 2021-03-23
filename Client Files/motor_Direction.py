import RoboPiLib as RPL
import setup
from time import sleep
import sys, tty, termios, os
import NameJeff as HBridge #I know that this is weird but NameJeff is what the setup thing is called

speedleft = 0
speedright = 0
###EDIT THESE IF NEEDED



def stop():
    HBridge.setMotorLeft(0)
    HBridge.setMotorRight(0)

def front():
    speedleft = speedleft + 1       #the number here can be changed to increase or decrease the acceleration
    speedright = speedright + 1     #the number here can be changed to increase or decrease the acceleration

    if speedleft > 1:
        speedleft = 1
    if speedright > 1:
        speedright = 1

    HBridge.setMotorLeft(speedleft)
    HBridge.setMotorRight(speedright)

def left():
    speedleft = speedleft - 1       #the number here can be changed to increase or decrease the acceleration
    speedright = speedright + 1     #the number here can be changed to increase or decrease the acceleration
    if speedleft < -1:
        speedleft = -1      #make this value higher to make the turn less sharp
    if speedright > 1:
        speedright = 1
    HBridge.setMotorLeft(speedleft)
    HBridge.setMotorRight(speedright)

def right():
    speedleft = speedleft + 1       #the number here can be changed to increase or decrease the acceleration
    speedright = speedright - 1     #the number here can be changed to increase or decrease the acceleration
    if speedleft > 1:
        speedleft = 1
    if speedright < -1:
        speedright = -1     #make this value higher to make the turn less sharp
    HBridge.setMotorLeft(speedleft)
    HBridge.setMotorRight(speedright)

def back():
    speedleft = speedleft - 1       #the number here can be changed to increase or decrease the acceleration
    speedright = speedright - 1     #the number here can be changed to increase or decrease the acceleration
    if speedleft < -1:
        speedleft = -1
    if speedright < -1:
        speedright = -1
    HBridge.setMotorLeft(speedleft)
    HBridge.setMotorRight(speedright)

def exit():
    HBridge.setMotorLeft(0)
    HBridge.setMotorRight(0)
    HBridge.exit()
