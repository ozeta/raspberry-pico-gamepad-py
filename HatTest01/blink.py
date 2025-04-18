from machine import Pin
import time
import neopixel
"""
This library uses the plain firmware by https://www.waveshare.com/wiki/RP2350-Zero

This script reads the input the Pico to the aliexpress hat board
Each time a key is pressed, an output is printed in the REPL console and the integrated WS2812 led is turned on 

"""

# ----- Configuration -----

# Button polling frequency (in Hertz)
polling_frequency_hz = 16
polling_interval_sec = 1 / polling_frequency_hz

# WS2812 LED setup (connected to GP16)
NUM_LEDS = 1
led_pin = Pin(16, Pin.OUT)
led_strip = neopixel.NeoPixel(led_pin, NUM_LEDS)

# Button pins mapped by label
buttons = {
    "Middle": Pin(14, Pin.IN, Pin.PULL_UP),
    "Right":  Pin(15, Pin.IN, Pin.PULL_UP),
    "Left":   Pin(26, Pin.IN, Pin.PULL_UP),
    "Back":   Pin(27, Pin.IN, Pin.PULL_UP),
    "Front":  Pin(28, Pin.IN, Pin.PULL_UP)
}

# ----- LED Control Functions -----

def turn_on_led(color):  # RGB: dim white
    led_strip[0] = color
    led_strip.write()

def turn_off_led():
    led_strip[0] = (0, 0, 0)
    led_strip.write()

# ----- Main Loop -----

while True:
    pressed_buttons = []

    for name, pin in buttons.items():
        if pin.value() == 0:  # Active LOW: pressed = 0
            pressed_buttons.append(name)

    if pressed_buttons:
        print("Pressed buttons:", ", ".join(pressed_buttons))
        turn_on_led((5, 5, 5))  # Turn on LED with reduced brightness
    else:
        turn_off_led()  # Turn off LED

    time.sleep(polling_interval_sec)
