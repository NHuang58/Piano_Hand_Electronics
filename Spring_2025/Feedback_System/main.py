import machine
import time

finger_distances = [0, 0, 0, 0, 0] #FIX TO FIND THE DISTANCE BETWEEN FINGERS (NOT CONSTANT)

def main():
    while True:
        # Get the position of the stepper motor
        position = getPosition()
        # Fix the position of the stepper motor
        fixPosition()
        # Sleep for 1 second
        time.sleep(1)

if __name__ == "__main__":
    main()