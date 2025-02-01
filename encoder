from machine import Pin 
from time import sleep_ms
from rotary_irq import *

r = RotaryIRQ(pin_num_clk=32, 
              pin_num_dt=33, 
              min_val=0, 
              max_val=19, 
              reverse=True, 
              range_mode=RotaryIRQ.RANGE_WRAP)
sw = Pin(34, Pin.IN)
val_old = r.value()
isRotaryEncoder = True
print("hello")
while True:
    val_new = r.value()
    print(val_new)
    if val_old != val_new:
        val_old = val_new
        print(val_new)
        #print('result = {0}'.format(val_new))
    sleep_ms(200)

