import RoboPiLib as RPL
import setup
import motor_Direction
from time import sleep


def movement(data):
    pinList = [0,1,2,3]
    char = data

    if char == 'r':
        motor_Direction.up(0)
    elif char == 'f':
        motor_Direction.down(0)

    elif char == 't':
        motor_Direction.up(1)
    elif char == 'g':
        motor_Direction.down(1)

    elif char == 'y':
        motor_Direction.up(2)
    elif char == 'h':
        motor_Direction.down(2)

    elif char == 'u':
        motor_Direction.up(3)
    elif char == 'j':
        motor_Direction.down(3)

    elif char == '0':
        for pin in pinList:
            motor_Direction.stop(pin)
    elif char == 'None':
        print("ping recieved")
    else:
        print("input not recognized")
