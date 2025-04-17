from machine import Pin
import time

# Elenco dei pin disponibili sulla RP2040 (GPIO 0–28)
gpio_pins = list(range(29))


# set pints to 0
for pin_num in gpio_pins:
    try:
        pin = Pin(pin_num, Pin.OUT)
        pin.value(0)  # Set the pin to LOW
    except Exception as e:
        print(f"GPIO{pin_num} non disponibile: {e}")


# Crea un dizionario di pin configurati come input con PULL_DOWN (evita pin fluttuanti)
inputs = {}
for pin_num in gpio_pins:
    try:
        inputs[pin_num] = Pin(pin_num, Pin.IN, Pin.PULL_DOWN)
    except Exception as e:
        print(f"GPIO{pin_num} non disponibile: {e}")

print("awaiting for GPIO input...")
while True:
    states = {}
    for pin_num, pin in inputs.items():
        if pin.value() == 1:  # Check if the pin value is 1
            states[pin_num] = pin.value()
    
    if states:  # Print only if there are active pins
        print("Stati dei GPIO attivi:", dict(sorted(states.items())) )
    


    time.sleep(1)