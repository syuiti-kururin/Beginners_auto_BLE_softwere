# Technical Specification

ROBO-ONE Beginners Auto BLE PC Controller

---

# 1. Overview

This document describes the detailed technical specifications of the PC-side BLE controller used for ROBO-ONE beginner robots.

Unlike the README, which focuses on project introduction and basic usage, this document provides:

* communication architecture
* BLE configuration
* command protocol
* software structure
* operational flow

The goal of this document is to allow developers to understand how the system works internally and modify it if necessary.

---

# 2. System Architecture

The system consists of two major components.

1. PC Controller (Python)
2. Robot Controller (MicroPython / BLE)

The PC acts as the BLE **Central device**, while the robot acts as the **Peripheral device**.

System diagram:

```
+-----------------------+
|        PC             |
| Python BLE Controller |
| (Central Device)      |
+-----------+-----------+
            |
            | Bluetooth Low Energy
            |
+-----------v-----------+
|        Robot          |
| MicroPython BLE Node  |
| (Peripheral Device)   |
+-----------------------+
```

---

# 3. BLE Communication Model

BLE communication follows the standard GATT model.

Key elements used:

* Service
* Characteristic
* UUID

In most configurations, the robot firmware implements a UART-style BLE service.

Typical example:

Nordic UART Service (NUS)

Service UUID

```
6E400001-B5A3-F393-E0A9-E50E24DCCA9E
```

RX Characteristic (Write)

```
6E400002-B5A3-F393-E0A9-E50E24DCCA9E
```

TX Characteristic (Notify)

```
6E400003-B5A3-F393-E0A9-E50E24DCCA9E
```

Note that the actual UUID values may differ depending on the robot firmware implementation.

---

# 4. BLE Connection Flow

The connection process follows the typical BLE central workflow.

1. Robot starts BLE advertising
2. PC scans for BLE devices
3. Target robot is identified
4. PC establishes connection
5. PC discovers services
6. Characteristic is selected
7. Command transmission begins

---

# 5. Command Protocol

Communication between PC and robot is performed using simple ASCII commands.

Each command represents a robot action.

Example commands:

```
F
B
L
R
X
```

Command format:

```
[ASCII Command]
```

Example transmission:

```
send("F")
```

Robot receives the command and executes the corresponding motion.

Example robot behavior:

```
Receive: F
Action: Forward movement
```

---

# 6. Command Table

| Command | Action                |
| ------- | --------------------- |
| F       | Forward               |
| B       | Backward              |
| L       | Rotate Left           |
| R       | Rotate Right          |
| X       | Stop                  |
| A       | Autonomous Mode       |
| Op      | Manual Operation Mode |

Actual behavior depends on the robot firmware implementation.

---

# 7. Software Structure

Example project structure:

```
Beginners_auto_BLE_softwere

ble_robot.py
README.md
README_en.md
README_es-cl.md
README_na.md
specifics_md_jp.md
specifics_md_en.md
specifics_es-cl.md
specifics_na.md
LICENSE
```

Main roles:

ble_robot.py

Main file containing BLE communication and tkinter GUI

* BLE connection (direct connect to fixed address)
* Command transmission
* BLE receive notification (notify)
* GUI panel (directional buttons, auto/manual buttons, log box)
* asyncio event loop in separate thread

---

# 8. Python BLE Library

This project uses the Python BLE library:

bleak

Installation:

```
pip install bleak
```

Bleak provides cross-platform BLE functionality for:

* Windows
* Linux
* macOS

---

# 9. Example Command Transmission

Simplified example:

```python
await client.write_gatt_char(UART_RX, "F".encode())
```

This sends the command "F" to the robot.

---

# 10. Extension Possibilities

Possible future extensions include:

Sensor feedback

* IMU data
* distance sensors
* battery status

Autonomous navigation

* mapping
* path planning

Auto-scan and select BLE device

---

# 11. Safety Notes

Robots controlled by external software may move unexpectedly.

Always test in a safe environment.

Avoid operating robots near people or fragile equipment.

---

# 12. License

This project is distributed under the

ROBO-ONE Educational Non-Commercial Software License v1.0

See LICENSE file for details.
