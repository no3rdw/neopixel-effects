# LEDMatrix Effects!

This project was built for a Feather M4 Express, 32x32 LED Matrix, a NeoKey 1x4, and a PCF8523 real-time clock.

- When possible, all effects have been coded to work on other resolution screens (ex. 64x32), although I do not currently have the ability to test this.
- The real-time clock is optional and can be commented out in device.py. Any time the clock would be displayed, 00:00:00 will be displayed instead.
- The NeoKeys are also optional and can be commented out in device.py. Boot.py must also be removed if not using NeoKeys.  Obviously this means there is no way to interact with the effects, navigate menus, or enter/exit write mode. The first effect in the 'effects' list in main.py will be loaded on startup.
- If another microprocessor is used, the effect framerates may need to be adjusted (search for calls to limitStep within each effect's play loop)


**Credits**
- All included libraries courtesy Adafruit CircuitPython, available here: https://circuitpython.org/libraries
- Included font converted from OpenType font 04B03
- Easing functions in device.py courtesy Easings.net
- All other code by Paul Gallo (pgallo@gmail.com)
- Easing functions in device.py courtesy Easings.net
- All other code by Paul Gallo (pgallo@gmail.com)