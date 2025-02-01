from machine import Pin
import time

# Pin definitions
CLK_PIN = 25  # GPIO25 connected to the rotary encoder's CLK pin
DT_PIN = 26   # GPIO26 connected to the rotary encoder's DT pin

# Constants
DIRECTION_CW = 0   # Clockwise direction
DIRECTION_CCW = 1  # Counter-clockwise direction
STEPS_PER_REVOLUTION = 600  # Number of steps for one full rotation (360°)

# Variables
counter = 0
direction = DIRECTION_CW
prev_CLK_state = 0

# Initialize pins
clk = Pin(CLK_PIN, Pin.IN, Pin.PULL_UP)
dt = Pin(DT_PIN, Pin.IN, Pin.PULL_UP)


duration = 0
# Main loop
while True:
    # Read the current state of the CLK pin
    CLK_state = clk.value()

    # Check if the CLK pin state has changed
    if CLK_state != prev_CLK_state:
        # If the state of CLK is HIGH, a pulse occurred
        if CLK_state == 1:
            # Read the DT pin to determine the direction
            if dt.value() == 1:
                counter -= 1
                direction = DIRECTION_CCW
            else:
                counter += 1
                direction = DIRECTION_CW

            # Calculate degrees
            degrees = (counter % STEPS_PER_REVOLUTION) * (360 / STEPS_PER_REVOLUTION)
            print("Rotary Encoder:: direction:", "CLOCKWISE" if direction == DIRECTION_CW else "ANTICLOCKWISE", "- count:", counter, "- degrees:", degrees)

        # Save the current CLK state for the next iteration
        prev_CLK_state = CLK_state

    # Small delay to reduce CPU usage
    duration += 1
    time.sleep_ms(1000)
    if (duration == 15):
        print("Program ended")
        break