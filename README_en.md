# ROBO-ONE Beginners Auto BLE PC Controller

## Introduction

This project is a **PC controller software for BLE communication experiments** designed for students who want to challenge **ROBO-ONE autonomous robots**.

---

## About This Project

I am currently building a robot to participate in autonomous robot competitions such as **ROBO-ONE Beginners**.
During development, I encountered many difficulties when working with **BLE (Bluetooth Low Energy) communication**.

In particular:

* Smartphone BLE apps are difficult to operate precisely
* Communication testing and debugging are inconvenient
* Integration with program development is difficult

Because of these issues, I created a **simple BLE controller software in Python that allows BLE communication to be handled easily from a PC**.

---

## Purpose of This Repository

This repository publishes the **PC-side BLE controller software** that I created.

However, please note that this software is **still under development**, and it may differ slightly from the version I currently use.

The version published here is intentionally kept:

* as simple as possible
* easy to understand
* suitable as a starting point for modification

In other words, this is the **most basic version of the software**.

---

## Philosophy of This Project

I do not claim to fully understand everything yet.
I am still developing my robot while **learning and researching step by step**.

Therefore, this software is not intended to be a

"complete tool"

but rather

**a starting point for people who want to explore and modify the system themselves.**

If this software can become the **first step** for people who want to:

* experiment with BLE communication
* challenge ROBO-ONE autonomous robots
* explore robot control systems

then I would be very happy.

---

## Overview

This software is a **PC-based controller** designed to operate **BLE-enabled ROBO-ONE beginner robots**.

Traditionally, BLE communication can be performed using smartphone applications such as:

* Bacon
* Bluetooth Connect

However, for robot control purposes these tools often have limitations such as:

* unstable connections
* restricted user interfaces
* difficulty performing continuous operations or experiments

This project provides a **software solution that allows BLE communication and robot control directly from a PC**, enabling more flexible experimentation and development.

---

## Related Project

This software is intended to work together with the following robot-side program:

ROBO-ONE Beginners BLE Robot Program
Author: Terukazu Nishimura @AiRRC

This repository **does not modify the robot-side program**.
Instead, it provides a **newly developed PC-side BLE controller software**.

---

## Main Features

* BLE connection from a PC
* Command transmission to the robot
* Continuous operation and experimentation environment
* Support for autonomous control program development

---

## System Requirements

* Python 3
* A PC that supports BLE communication
* ROBO-ONE Beginner Robot (BLE-enabled)

---

# Usage

## 0. Download Python

Download the latest version of Python 3 from the official website:

https://www.python.org/downloads/

---

## 1. Install Required Libraries

Install the Python library required for BLE communication.

```bash
pip install bleak
```

Install additional dependencies if necessary.

---

## 2. Start the Robot Program

Write the **BLE-enabled MicroPython program** to the robot’s microcontroller and start it.

Make sure the robot is in **BLE advertising mode**.

---

### Note: How to Find the BLE UUID

BLE communication uses **UUIDs** to identify services and characteristics.

To communicate with the robot, you may need to identify the correct UUID.

You can find the UUID using BLE scanning tools such as:

* nRF Connect (smartphone app)
* BLE Scanner
* Bluetooth Developer Tools (PC)

Basic steps:

1. Start a BLE scanning application
2. Turn on the robot
3. Select the robot device from the list
4. View the **Service** or **Characteristic** list
5. Identify the displayed **UUID**

After obtaining the UUID, configure it in the PC-side program.

BLE may seem complicated at first, but inspecting the services using these tools helps understanding the communication structure.

In many cases, the **Nordic UART Service** is used.

---

## 3. Run the PC Software

Run the controller program on the PC.

```bash
python ble_robot.py
```

or

```bash
python main.py
```

(depending on the actual file name)

---

## 4. Connect via BLE

After launching the program, search for the robot BLE device and connect to it.

Once connected successfully, the PC will be able to send commands to the robot.

---

## Directory Structure

```
ROBO-ONE_BLE_PC_Controller/

├ ble_robot.py
├ main.py
├ README.md
└ LICENSE
```

---

# Communication Specification (BLE Commands)

This software uses **BLE (Bluetooth Low Energy)** to perform command communication between the PC and the robot.

Communication roles:

* PC: BLE Central (connecting device)
* Robot: BLE Peripheral (device being connected)

The PC sends commands to the robot, and the robot-side MicroPython program receives them and executes the corresponding actions.

Communication is mainly performed using **simple text commands**.

Example:

```
F
B
L
R
X
```

---

# Connection Architecture

```
+--------------------+
|        PC          |
|  BLE Controller    |
|  (Python Program)  |
+---------+----------+
          |
          | BLE communication
          |
+---------v----------+
|      Robot         |
|  MicroPython BLE   |
|  Servo Controller  |
+--------------------+
```

Communication flow:

1. Robot starts BLE advertising
2. PC software scans for devices
3. PC connects via BLE
4. Commands are transmitted
5. Robot executes the command

---

# Command List

| Command | Action                |
| ------- | --------------------- |
| F       | Move Forward          |
| B       | Move Backward         |
| L       | Rotate Left           |
| R       | Rotate Right          |
| X       | Stop                  |
| A       | Autonomous Mode       |
| OP      | Manual Operation Mode |

Actual commands may depend on the robot firmware implementation.

---

# Communication Example

Example of sending a command from the PC to the robot:

```
send("F")
```

Robot-side processing example:

```
Received command: F
→ Execute forward movement
```

---

# Planned Future Extensions

The following features are planned for future development:

* Sensor feedback to the PC
* Mapping functionality
* Autonomous navigation algorithms
* GUI controller

---

## Safety Notice

This software is intended for **robot control experiments and development**.

Robots may move unexpectedly depending on the commands sent.
Always operate the robot in a safe environment to avoid accidents or damage.

---

## License

This project is released under the **ROBO-ONE Educational Non-Commercial License v1.0**.

Permitted:

* Use
* Modification
* Fork
* Redistribution
* Educational and research use

Prohibited:

* Commercial use
* Selling for profit

See the `LICENSE` file for details.
