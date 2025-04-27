import time
import machine
# IMPORT THE ENCODER TO CHANGE THE POSITION
from encoder.py import *

# MOVE THE STEPPER MOTOR BY A SPECIFIC AMOUNT OF STEPS
def moveStepper():

# GET THE POSITION OF THE STEPPER MOTOR
def getPosition():
    # CALL FUNCTION IN ENCODER
    pass

# MOVE THE STEPPER MOTOR TO A SPECIFIC POSITION, BASED ON A LOOP
def fixPosition(desiredPosition):
    while (hand.getFingerPosition() is not desiredPosition):
        if (position < desiredPosition):
            moveStepper(1)
        elif (position > desiredPosition):
            moveStepper(-1)
        time.sleep(0.1)
