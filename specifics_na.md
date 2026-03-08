# Dokumen Teknik (Technical Specification)

ROBO-ONE Beginners Auto BLE PC Controller

---

# 1. Ibwija (Resumen)

Eket dokumen e ibwija teknik imōn
**ROBO-ONE Beginners Auto BLE PC Controller**.

README.md e ibwija background ama ekamöak itsiwa,
iamörin eket dokumen e **ibwija itsi awöi** ōrōr:

* Sistem arquitectura
* BLE comunicación ikakōkō
* Especificación protocolo comando
* Estructura software
* Flujo conexión
* Diseño extensible

Eket dokumen e ñan **desarrollador ama usuario it eron mōrōñ sistema**.

---

# 2. Arquitectura Sistema

Eket sistema e ebar **2 elemento owieji**.

1. Controller PC (Python)
2. Controller robot (MicroPython / BLE)

PC e operar ñan **BLE Central (conectar)**,
robot e operar ñan **BLE Peripheral (conectado)**.

Diagrama:

```
+-----------------------+
|          PC           |
|  Python BLE Program   |
|   (Central Device)    |
+-----------+-----------+
            |
            | Bluetooth Low Energy
            |
+-----------v-----------+
|        Robot          |
|  MicroPython BLE Node |
|   (Peripheral Device) |
+-----------------------+
```

Software PC e enviar comando ñan robot,
program robot e recibir ama controlar motor ama servo.

---

# 3. Modelo BLE Comunicación

BLE comunicación e emen ñan **GATT (Generic Attribute Profile)**.

Elemento owieji:

* Service
* Characteristic
* UUID

BLE robot imōn,
ōrrōr e emen **UART service tipo**.

Ejemplo típico: **Nordic UART Service (NUS)**.

Ej.:

Service UUID

```
6E400001-B5A3-F393-E0A9-E50E24DCCA9E
```

RX Characteristic (PC → Robot)

```
6E400002-B5A3-F393-E0A9-E50E24DCCA9E
```

TX Characteristic (Robot → PC)

```
6E400003-B5A3-F393-E0A9-E50E24DCCA9E
```

Iamörin, UUID real e bai ñōr ñan program robot imōm.

---

# 4. Flujo Conexión BLE

Conexión BLE PC ama robot e emen pasos estándar BLE.

Flujo:

1. Robot iniow advertising BLE
2. Program PC scan device BLE
3. Detect device objetivo
4. Establecer conexión BLE
5. Obtener GATT service
6. Identify Characteristic
7. Iniow envío comando

---

# 5. Especificación Protocolo Comando

Comunicación PC ama robot e emen
**comando texto simple**.

Formato básico:

```
[ASCII string]
```

Ej.:

```
F
B
L
R
X
```

Software PC e enviar eket comando ñan BLE comunicación.

---

# 6. Tabla Comando

| Comando | Acción                |
| ------- | --------------------- |
| F       | Tōñ (Avanzar)         |
| B       | Ōrrōr (Retroceder)    |
| L       | Kiu (Girar izquierda) |
| R       | Ri (Girar derecha)    |
| X       | Detener               |
| A       | Modo autónomo         |
| Op      | Modo manual           |

※ Acción real e depender imōn program robot.

---

# 7. Estructura Software

Eket project e estructura simple.

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

Función owieji:

ble_robot.py

Archivo principal BLE comunicación ama GUI tkinter

* Conexión BLE (dirección fija)
* Envío comando
* Notificación BLE (notify)
* Panel GUI (botones dirección, botones auto/manual, log box)
* Event loop asyncio ñan hilo separado

---

# 8. Librería Python BLE

Eket project e emen librería Python BLE **bleak**.

Instalar:

```
pip install bleak
```

Bleak e operar imōn:

* Windows
* Linux
* macOS

---

# 9. Ejemplo Envío Comando

Escribir comando ñan BLE Characteristic.

Ej.:

```python
await client.write_gatt_char(UART_RX, "F".encode())
```

Eket code e enviar **comando avance** ñan robot.

---

# 10. Función Extensible

Eket sistema e bai mōrōñ ñan función ōrōr:

Sensor feedback

* IMU
* Sensor distancia
* Información batería

Control autónomo

* Mapeo
* Movimiento autónomo
* Búsqueda ruta

Scan ama select automático device BLE

---

# 11. Aviso Seguridad

Robot e controlar ñan software externo,
e bai mover inesperadamente.

Tesuto imōn lugar bwio,
ñan neine peligro ñan eit ama equipment.

---

# 12. Licencia

Eket project e distribuir ñan

ROBO-ONE Educational Non-Commercial Software License v1.0

Ver archivo `LICENSE`.
