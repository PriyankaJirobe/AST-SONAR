# AST-SONAR

## Adaptive Sonar Transmission System

AST-SONAR is an ESP32-based proof-of-concept prototype exploring
software-controlled and reconfigurable sonar transmission.

The project demonstrates hardware control, user-defined parameters,
operating modes, physical output and real-time monitoring through
a Python dashboard.

---

## 🚀 Features

- ESP32-based embedded controller
- Potentiometer-based frequency parameter input
- Adjustable transmission power
- Normal, Adaptive and Low Power operating modes
- Buzzer-based physical transmission output
- Python-based real-time dashboard
- Serial communication between ESP32 and PC
- Live display of frequency, power and operating mode

---

## 🔧 Hardware

- ESP32 development board
- Potentiometer
- Push buttons
- Buzzer
- Breadboard
- Jumper wires
- USB cable

---

## 💻 Software

- Arduino IDE
- ESP32 Arduino framework
- Python
- Tkinter
- PySerial

---

## ⚙️ Working Principle

The prototype follows the basic flow:

Input
↓
ESP32
↓
Control Logic
↓
Transmission Output
↓
Serial Communication
↓
Python Dashboard

The potentiometer provides an input that is mapped to a frequency
parameter. Push buttons are used to modify transmission power and
operating mode.

The ESP32 sends the current system parameters to the Python dashboard
through a serial connection.

---

## 🖥️ Dashboard

The Python dashboard provides real-time monitoring of:

- Frequency
- Power
- Operating Mode
- Transmission Status

The dashboard communicates with the ESP32 through a live serial link.

---

## 📁 Project Structure

AST-SONAR/
│
├── README.md
├── ast_sonar.ino
│
└── dashboard/
    └── ast_sonar_dashboard.py

---

## ⚠️ Current Prototype Scope

This project is an early proof-of-concept.

The current prototype focuses on demonstrating:

- Embedded control
- Hardware interaction
- Parameter adjustment
- Operating modes
- Physical output
- Real-time software monitoring

The current buzzer output is a proof-of-concept transmission indicator.
The prototype does not yet implement a dedicated underwater sonar
transducer or true acoustic waveform generation.

---

## 🚀 Future Development

Future versions may explore:

- Actual waveform generation
- DAC-based signal output
- Signal conditioning
- Sensor-based environmental inputs
- Adaptive waveform selection
- Hardware timers and DMA
- Oscilloscope and FFT-based validation
- Dedicated acoustic transducer integration

---

## 👩‍💻 Project

Built as a hands-on embedded systems project to explore the integration
of electronics, ESP32 programming, Python software and hardware-software
communication.
