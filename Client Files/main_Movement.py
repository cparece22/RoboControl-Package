import RoboPiLib as RPL
import setup
import motor_Direction
from time import sleep

def movement(data):
    char = data
    if usrin == '0':
        motor_Direction.stop()
    elif usrin == 'w':
        motor_Direction.front()
    elif usrin == 's':
        motor_Direction.back()
    elif usrin == 'a':
        motor_Direction.left()
    elif usrin == 'd':
        motor_Direction.right()
    elif usrin == 'esc':
        motor_Direction.quit()
    elif usrin == 'None':
        print("ping recieved")
    else:
        print("input not recognized")
