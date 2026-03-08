# Technical Specification

ROBO-ONE Beginners Auto BLE PC Controller

## 1. Overview

Iti document explain technical structure enna system design
for **ROBO-ONE Beginners Auto BLE PC Controller**.

README describe project introduction.

This document describe:

* system architecture
* BLE communication model
* command protocol
* software structure
* connection flow

This document mainly for **developer and modification purpose**.

---

## 2. System Architecture

System have two main part:

1. PC Controller (Python)
2. Robot Controller (MicroPython BLE)

PC act as **BLE Central**.
Robot act as **BLE Peripheral**.

System structure:

```
PC (Python Controller)
      |
      | BLE Communication
      |
Robot (MicroPython BLE)
```

PC send command to robot.

Robot receive command and execute motor action.

---

## 3. BLE Communication

BLE communication use **GATT model**.

Main elements:

* Service
* Characteristic
* UUID

Often robot firmware use **Nordic UART Service**.

Example:

Service UUID

```
6E400001-B5A3-F393-E0A9-E50E24DCCA9E
```

RX Characteristic

```
6E400002-B5A3-F393-E0A9-E50E24DCCA9E
```

TX Characteristic

```
6E400003-B5A3-F393-E0A9-E50E24DCCA9E
```

Actual UUID depend robot firmware.

---

## 4. Connection Flow

BLE connection process:

1. Robot start BLE advertising
2. PC scan BLE devices
3. PC detect robot device
4. PC connect robot
5. PC discover services
6. PC select communication characteristic
7. command transmission start

---

## 5. Command Protocol

Communication use simple ASCII command.

Example:

```
F
B
L
R
X
```

Format:

```
[ASCII command]
```

Robot receive command and perform motion.

---

## 6. Command Table

| Command | Action          |
| ------- | --------------- |
| F       | Forward         |
| B       | Backward        |
| L       | Turn Left       |
| R       | Turn Right      |
| X       | Stop            |
| A       | Autonomous Mode |
| OP      | Manual Mode     |

Actual motion depend robot program.

---

## 7. Software Structure

Example repository structure:

```
ROBO-ONE_BLE_PC_Controller

ble_robot.py
main.py
README.md
Specifics.md
LICENSE
```

Roles:

ble_robot.py

* BLE scanning
* device connection
* command transmission

main.py

* user command input
* testing interface

---

## 8. Python Library

Project use Python BLE library **bleak**.

Install:

```
pip install bleak
```

Supported platforms:

* Windows
* Linux
* macOS

---

## 9. Command Transmission Example

Example Python code:

```
await client.write_gatt_char(uuid, b"F")
```

Robot receive command and execute action.

---

## 10. Future Extensions

Possible extensions:

* sensor feedback
* autonomous navigation
* mapping
* GUI controller

---

## 11. Safety Notes

Robot may move unexpectedly.

Test system in safe environment.

Avoid operation near people or fragile equipment.

---

## 12. License

ROBO-ONE Educational Non-Commercial License v1.0
