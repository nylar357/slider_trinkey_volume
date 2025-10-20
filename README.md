🎚️ Slider Trinkey Volume Controller

This repository contains the CircuitPython script for turning the Adafruit Slider Trinkey into a dedicated USB Human Interface Device (HID) volume controller.

Simply plug the Trinkey into your computer, and moving the slider will adjust your system's volume (Volume Up / Volume Down). The onboard NeoPixels also provide visual feedback.

🎥 Demo Video

See the Slider Trinkey in action!

🛠️ Setup and Dependencies

This script is written in CircuitPython.

Hardware: Adafruit Slider Trinkey (with an ATSAMD21 microcontroller).

Firmware: Ensure you are running the latest version of CircuitPython on your Trinkey.

Libraries: You must have the necessary libraries installed in the lib folder of your Trinkey's CIRCUITPY drive. The required library is:

adafruit_hid

⚙️ How the Script Works (code.py)

The code.py script continuously reads the analog value from the linear potentiometer and maps that movement to USB Consumer Control commands.

Key Logic:

Initialization:

The ConsumerControl class is initialized to send keyboard/media commands over USB.

The potentiometer input is set up on the board.POTENTIOMETER pin.

sensitivity = 2800 is defined. This value controls how far the slider needs to move before a volume change command is sent. You can adjust this for finer or coarser control.

Volume Control:

The script checks if the pot_current value has increased by more than sensitivity from the pot_previous value.

If it has moved up, it sends a ConsumerControlCode.VOLUME_INCREMENT.

If it has moved down, it sends a ConsumerControlCode.VOLUME_DECREMENT.

The pot_previous value is updated only after a volume command is sent, preventing commands from being sent continuously for a single movement.

NeoPixel Feedback:

The pot_current value (a 16-bit number, 0 to 65535) is shifted right by 8 bits (brightness = pot_current >> 8) to scale it down to an 8-bit number (0-255).

This scaled value is used as the Green component in the NeoPixel color (5, brightness, 115), causing the brightness of the blue-purple light to increase and decrease as the slider is moved.

Code Snippet:

# Part of code.py
```
sensitivity = 2800 # Adjust this value to set the volume step

while True:
    pot_current = pot_pin.value
    # Set NeoPixel brightness based on slider position
    brightness = pot_current >> 8 
    pixels.fill((5, brightness, 115,)) # Blue-purple color, brightness tied to pot value
    pixels.show()
    
    # Check for movement exceeding sensitivity threshold
    if pot_current > pot_previous + sensitivity:
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        pot_previous = pot_current
    elif pot_current < pot_previous - sensitivity:
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
        pot_previous = pot_current
    
    time.sleep(0.01)

```
