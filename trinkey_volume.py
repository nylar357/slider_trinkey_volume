import time
import board
import analogio
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

cc = ConsumerControl(usb_hid.devices)
pot_pin = analogio.AnalogIn(board.POTENTIOMETER) # Assuming the slider is on A0
pot_previous = pot_pin.value
sensitivity = 1000 # Adjust this value to set the volume step

while True:
    pot_current = pot_pin.value
    if pot_current > pot_previous + sensitivity:
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        pot_previous = pot_current
    elif pot_current < pot_previous - sensitivity:
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
        pot_previous = pot_current
    time.sleep(0.01)

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-


import time
import board
import analogio
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

cc = ConsumerControl(usb_hid.devices)
pot_pin = analogio.AnalogIn(board.POTENTIOMETER) # Assuming the slider is on A0
pot_previous = pot_pin.value
increment_divisor = 500 # A lower number gives bigger steps, higher for smaller steps

while True:
    pot_current = pot_pin.value
    delta = (pot_current - pot_previous) // increment_divisor
    
    if delta > 0:
        for _ in range(delta):
            cc.send(ConsumerControlCode.VOLUME_INCREMENT)
    elif delta < 0:
        for _ in range(abs(delta)):
            cc.send(ConsumerControlCode.VOLUME_DECREMENT)
            
    pot_previous = pot_current
    time.sleep(0.01)
