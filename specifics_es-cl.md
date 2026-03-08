# Especificación Técnica

ROBO-ONE Beginners Auto BLE PC Controller

---

# 1. Resumen

Este documento describe las especificaciones técnicas detalladas del
**ROBO-ONE Beginners Auto BLE PC Controller**.

En el README.md se explica el contexto del proyecto y el uso básico,
pero este documento cubre **con más detalle** lo siguiente:

* Arquitectura del sistema
* Funcionamiento de la comunicación BLE
* Especificación del protocolo de comandos
* Estructura del software
* Flujo de conexión
* Diseño extensible

Este documento está pensado principalmente **para desarrolladores y usuarios que quieran modificar el sistema**.

---

# 2. Arquitectura del sistema

Este sistema está compuesto por **2 elementos principales**.

1. Controlador del lado del PC (Python)
2. Controlador del lado del robot (MicroPython / BLE)

El PC opera como **BLE Central (el que conecta)**,
y el robot opera como **BLE Peripheral (el que se conecta)**.

Diagrama de comunicación:

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

El software del PC envía comandos al robot,
y el programa del robot los recibe y controla el movimiento de motores y servos.

---

# 3. Modelo de comunicación BLE

La comunicación BLE se realiza usando **GATT (Generic Attribute Profile)**.

Los elementos principales que se usan son los siguientes:

* Service
* Characteristic
* UUID

En la implementación BLE del robot,
en la mayoría de los casos se usa un **servicio de comunicación tipo UART**.

El ejemplo típico es el **Nordic UART Service (NUS)**.

Ejemplo:

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

Sin embargo, los UUID que se usan en la práctica
pueden variar dependiendo de la implementación del programa del robot.

---

# 4. Flujo de conexión BLE

La conexión BLE entre el PC y el robot sigue el procedimiento estándar de comunicación BLE.

Flujo de conexión:

1. El robot inicia el advertising BLE
2. El programa del PC escanea los dispositivos BLE
3. Se detecta el dispositivo objetivo
4. Se establece la conexión BLE
5. Se obtiene el servicio GATT
6. Se identifica la Characteristic de comunicación
7. Se da inicio al envío de comandos

---

# 5. Especificación del protocolo de comandos

La comunicación entre el PC y el robot
se realiza con **comandos de texto simple**.

Formato básico:

```
[Cadena ASCII]
```

Ejemplo:

```
F
B
L
R
X
```

El software del PC envía estos comandos a través de la comunicación BLE.

---

# 6. Tabla de comandos

| Comando | Acción                |
| ------- | --------------------- |
| F       | Avanzar               |
| B       | Retroceder            |
| L       | Girar a la izquierda  |
| R       | Girar a la derecha    |
| X       | Detener               |
| A       | Modo autónomo         |
| Op      | Modo operación manual |

※ El comportamiento real depende de la implementación del programa del robot.

---

# 7. Estructura del software

Este proyecto tiene una estructura simple.

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

Rol principal:

ble_robot.py

Archivo principal que contiene la comunicación BLE y la GUI tkinter

* Conexión BLE (conexión directa a dirección fija)
* Envío de comandos
* Notificación de recepción BLE (notify)
* Panel GUI (botones de dirección, botones auto/manual, caja de log)
* Event loop de asyncio en hilo separado

---

# 8. Librería Python BLE

Este proyecto usa la librería Python BLE **bleak**.

Instalación:

```
pip install bleak
```

Bleak opera en los siguientes entornos:

* Windows
* Linux
* macOS

---

# 9. Ejemplo de envío de comandos

Se escribe un comando en la Characteristic BLE.

Ejemplo:

```python
await client.write_gatt_char(UART_RX, "F".encode())
```

Este código envía el **comando de avance** al robot.

---

# 10. Funciones extensibles

Este sistema contempla las siguientes extensiones de funcionalidad:

Sensor feedback

* IMU
* Sensor de distancia
* Información de batería

Control autónomo

* Mapeo
* Movimiento autónomo
* Búsqueda de rutas

Escaneo y selección automática de dispositivos BLE

---

# 11. Aviso de seguridad

Cuando se controla un robot con software externo,
puede comportarse de formas inesperadas.

Haz las pruebas en un entorno seguro,
y asegúrate de que no haya peligro para personas ni equipos.

---

# 12. Licencia

Este proyecto se publica bajo la

ROBO-ONE Educational Non-Commercial Software License v1.0

Consulta el archivo `LICENSE` para más detalles.
