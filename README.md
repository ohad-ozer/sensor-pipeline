# Sensor Pipeline

A two-part project simulating an industrial sensor data pipeline.
The C++ part simulates a sensor and writes readings to a CSV file.
The Python part reads and analyzes that data.

---

## Project Structure
```
sensor-pipeline/
├── sensor-simulator/         # C++ project
│   ├── Sensor.h
│   ├── Sensor.cpp
│   └── sensor-simulator.cpp
├── python-analyzer/          # Python project
│   └── analyzer.py
├── requirements.txt
└── README.md
```
---

## Requirements

### C++
- Visual Studio 2022 or later
- C++17 or later

### Python
- Python 3.10 or later
- No external dependencies required (see requirements.txt)

---

## How to Run

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/sensor-pipeline.git
cd sensor-pipeline
```

### 2. Run the C++ Simulator
- Open `sensor-simulator/sensor-simulator.slnx` in Visual Studio
- Build and run the project
- This generates `sensor_data.csv` inside the `sensor-simulator` folder

### 3. Run the Python Analyzer
```bash
cd python-analyzer
python analyzer.py
```

---

## Example Output
```
=== Sensor Report ===
Sensor: sensor_1
Readings: 20
Temperature:
Average : 26.52
Min     : 15.57
Max     : 39.77
Humidity:
Average : 61.83
Min     : 31.11
Max     : 89.51
Alerts:
⚠ Reading 8: temperature 39.77 exceeds threshold!
⚠ Reading 13: temperature 38.15 exceeds threshold!
⚠ Reading 16: temperature 37.61 exceeds threshold!

```