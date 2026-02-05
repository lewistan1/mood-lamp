from machine import Pin
import neopixel
import time

# --- Configuration ---
num_leds = 24
led_pin = Pin(4, Pin.OUT)
ring = neopixel.NeoPixel(led_pin, num_leds)
brightness = 0.6  # adjust for power

# Touch sensor
touch = Pin(5, Pin.IN)

# --- Helper functions ---
def set_color(r, g, b):
    r = int(r * brightness)
    g = int(g * brightness)
    b = int(b * brightness)
    for i in range(num_leds):
        ring[i] = (r, g, b)
    ring.write()

# --- Modes and colors ---
colors = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (0, 255, 255),  # Cyan
    (255, 0, 255),  # Magenta
    (255, 255, 255),# White
    "RAINBOW"       # Special auto-cycle mode
]

prev_state = 0
tap_times = []
tap_interval = 0.1
color_index = -1
mode = None

# For rainbow cycle
rainbow_index = 0
last_change = time.ticks_ms()
cycle_delay = 1000  # ms between color changes

# --- Main loop ---
while True:
    state = touch.value()

    # Detect rising edge
    if state == 1 and prev_state == 0:
        now = time.time()
        tap_times.append(now)
        tap_times = [t for t in tap_times if now - t < tap_interval]

        if len(tap_times) == 3:
            # Triple tap -> off
            mode = None
            set_color(0, 0, 0)
            print("Triple tap: OFF")
            tap_times = []
        else:
            # Single tap -> next mode
            color_index = (color_index + 1) % len(colors)
            if colors[color_index] == "RAINBOW":
                mode = "RAINBOW"
                rainbow_index = 0
                last_change = time.ticks_ms()
                print("Rainbow cycle mode ON")
            else:
                mode = "STATIC"
                set_color(*colors[color_index])
                print(f"Single tap: {colors[color_index]}")

    prev_state = state

    # Handle rainbow cycle
    if mode == "RAINBOW":
        if time.ticks_diff(time.ticks_ms(), last_change) > cycle_delay:
            rainbow_index = (rainbow_index + 1) % (len(colors)-1)  # exclude "RAINBOW"
            set_color(*colors[rainbow_index])
            print(f"Rainbow cycle: {colors[rainbow_index]}")
            last_change = time.ticks_ms()

    time.sleep(0.05)  # polling speed

