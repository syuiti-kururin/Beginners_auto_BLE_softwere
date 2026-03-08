# Especificación Técnica

ROBO-ONE Beginners Auto BLE PC Controller

## 1. Descripción general

Este documento describe la estructura técnica del sistema
**ROBO-ONE Beginners Auto BLE PC Controller**.

Mientras que el README presenta la introducción del proyecto,
este documento explica:

* arquitectura del sistema
* modelo de comunicación BLE
* protocolo de comandos
* estructura del software
* flujo de conexión

Este documento está dirigido principalmente a **desarrolladores**.

---

## 2. Arquitectura del sistema

El sistema tiene dos componentes principales:

1. Controlador en PC (Python)
2. Controlador del robot (MicroPython BLE)

El PC actúa como **BLE Central**.
El robot actúa como **BLE Peripheral**.

```
PC (Controlador Python)
        |
        | Comunicación BLE
        |
Robot (MicroPython BLE)
```

El PC envía comandos al robot,
y el robot ejecuta las acciones correspondientes.

---

## 3. Comunicación BLE

La comunicación BLE utiliza el modelo **GATT**.

Elementos principales:

* Service
* Characteristic
* UUID

Muchos robots usan **Nordic UART Service**.

Ejemplo:

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

Los UUID reales pueden variar dependiendo del firmware del robot.

---

## 4. Flujo de conexión

Proceso típico de conexión BLE:

1. El robot inicia advertising
2. El PC escanea dispositivos
3. Se detecta el robot
4. Se establece la conexión
5. Se descubren los servicios
6. Se selecciona el characteristic
7. Se envían comandos

---

## 5. Protocolo de comandos

La comunicación utiliza **comandos ASCII simples**.

Ejemplo:

```
F
B
L
R
X
```

Formato:

```
[comando ASCII]
```

---

## 6. Tabla de comandos

| Comando | Acción          |
| ------- | --------------- |
| F       | Avanzar         |
| B       | Retroceder      |
| L       | Girar izquierda |
| R       | Girar derecha   |
| X       | Detener         |
| A       | Modo autónomo   |
| OP      | Modo manual     |

---

## 7. Estructura del software

Ejemplo:

```
ROBO-ONE_BLE_PC_Controller

ble_robot.py
main.py
README.md
Specifics.md
LICENSE
```

ble_robot.py

* escaneo BLE
* conexión
* transmisión de comandos

main.py

* interfaz de usuario
* pruebas de control

---

## 8. Biblioteca Python

El proyecto usa **bleak** para BLE.

Instalación:

```
pip install bleak
```

Compatible con:

* Windows
* Linux
* macOS

---

## 9. Ejemplo de transmisión

Ejemplo Python:

```
await client.write_gatt_char(uuid, b"F")
```

---

## 10. Extensiones futuras

Posibles extensiones:

* feedback de sensores
* navegación autónoma
* mapeo
* controlador GUI

---

## 11. Seguridad

Los robots pueden moverse inesperadamente.

Realizar pruebas en un entorno seguro.

---

## 12. Licencia

ROBO-ONE Educational Non-Commercial License v1.0
