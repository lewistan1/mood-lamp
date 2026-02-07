# 💡 The Flower
<img width="483" height="364" alt="image" src="https://github.com/user-attachments/assets/12155fca-3349-4dbc-94d3-013b393c2106" />


This project implements a **touch-controlled NeoPixel LED ring** using an ESP32 supermini.  
Users can cycle through colours, activate a rainbow auto-cycle mode, or turn off the LEDs using **tap gestures** on a touch input.

The design prioritises **simplicity**, **low power usage**, and **standalone interaction** without Wi-Fi or external controllers.

This project also serves as my first hands-on microcontroller project, where I explored the fundamentals of ESP32 programming.

---

## ✨ Features

- Controls a **24-LED NeoPixel ring**
- Adjustable **global brightness scaling**
- Touch-based interaction:
  - **Single tap** → next colour / mode
  - **Triple tap** → turn OFF
- Built-in **RAINBOW auto-cycle mode**
- Simple polling-based touch detection
- Lightweight and beginner-friendly MicroPython code

---

## 🔌 Hardware Components

| Component | Quantity |
|---------|---------|
| ESP32 supermini (MicroPython) | 1 |
| NeoPixel LED Ring (24 LEDs) | 1 |
| Touch Input / Touch Pad | 1 |
| Power Supply | 1 |

---

## 📍 Pin Configuration

| Function | ESP32 Pin |
|-------|---------|
| NeoPixel Data | GPIO 4 |
| Touch Input | GPIO 5 |
<img width="1196" height="694" alt="image" src="https://github.com/user-attachments/assets/f340e8df-c3bd-4045-bd87-fc96cb086fac" />

---

## 🎨 Colour & Mode Behaviour

### Available Colours
The system cycles through the following colours:

- Red
- Green
- Blue
- Yellow
- Cyan
- Magenta
- White
- **RAINBOW** (auto-cycle mode)

---

## 🖐 Touch Gesture Controls

| Gesture | Action |
|-------|--------|
| Single tap | Cycle to next colour / mode |
| Triple tap | Turn OFF all LEDs |

### Notes
- Triple tap must occur within a short time window (`tap_interval`)
- Touch input is edge-detected to avoid repeated triggers
- Brightness is applied globally to reduce power draw

---

## 🌈 Rainbow Mode

When **RAINBOW mode** is active:
- The LED ring automatically cycles through preset colours
- Colour changes occur at a fixed interval (`cycle_delay`)
- Mode continues until another tap is detected

---

## 🛠 Software Stack

- **MicroPython**
- **NeoPixel library**
- Polling-based touch input handling

---

## 🚀 Setup Instructions

1. Flash **MicroPython** onto your ESP32
2. Upload the Python script to the board
3. Connect:
   - NeoPixel data line to GPIO 4
   - Touch input to GPIO 5
4. Power on the board
5. Use touch gestures to control the LED ring

---

## ⚡ Configuration Options

You can easily adjust behaviour by modifying:

```python
brightness = 0.6       # LED brightness (0.0 – 1.0)
tap_interval = 0.1     # Time window for multi-tap detection
cycle_delay = 1000     # Rainbow cycle delay (ms)
