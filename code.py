import time
import board
import analogio
import usb_hid
import neopixel
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

pixels = neopixel.NeoPixel(board.NEOPIXEL, 2, brightness=1.0, auto_write=False)
cc = ConsumerControl(usb_hid.devices)
pot_pin = analogio.AnalogIn(board.POTENTIOMETER) # Assuming the slider is on A0
pot_previous = pot_pin.value
sensitivity = 2800 # Adjust this value to set the volume step

while True:
    pot_current = pot_pin.value
    brightness = pot_current >> 8
    pixels.fill((5, brightness, 115,))
    pixels.show()
    if pot_current > pot_previous + sensitivity:
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        pot_previous = pot_current
    elif pot_current < pot_previous - sensitivity:
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
        pot_previous = pot_current
    time.sleep(0.01)
