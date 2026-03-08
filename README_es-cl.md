# ROBO-ONE Beginners Auto BLE PC Controller

## Introducción
Este proyecto es un software controlador PC para experimentos de comunicación BLE,
pensado para los estudiantes que quieren meterse al mundo de los robots autónomos de ROBO-ONE.

---

## Sobre este proyecto

Yo estoy fabricando un robot para competencias de robots autónomos como **ROBO-ONE Beginners**.
Pero durante el desarrollo me topé con hartos problemas cuando tuve que lidiar con la comunicación **BLE (Bluetooth Low Energy)**.

En particular:

* Las apps BLE del celular son difíciles de operar con precisión
* Hacer pruebas y debug de la comunicación es una lata
* Integrar todo esto con el desarrollo del programa es complicado

Por eso mismo me armé un **controlador BLE simple en Python para manejar la comunicación BLE fácilmente desde el computador**.

---

## Para qué publiqué esto

En este repositorio publico ese **software controlador BLE para PC**.

Eso sí, hay que tener claro que esto está **en desarrollo todavía**,
y puede ser un poco distinto a la versión que manejo yo ahora.

Lo que publiqué acá lo dejé así de intencional:

* lo más simple posible
* fácil de entender
* listo para que le metas mano

O sea, esta es **la versión más básica del software**.

---

## La idea detrás del proyecto

Yo no me la sé toda todavía.
Sigo desarrollando mi robot mientras **voy investigando y aprendiendo de a poco**.

Por eso mismo este software no pretende ser una

"herramienta terminada"

sino más bien

**un punto de partida para que tú lo explores y lo modifiques a tu gusto.**

Si este software puede ser el **primer paso** para alguien que quiere:

* experimentar con comunicación BLE
* meterse al mundo de los robots autónomos con ROBO-ONE
* explorar sistemas de control de robots

pues me dejaría más que contento.

---

## Resumen

Este software es un **controlador para PC** hecho para manejar robots **ROBO-ONE para principiantes con BLE**.

Antes, la comunicación BLE se hacía con apps del celular como Bacon o Bluetooth Connect,
pero para controlar robots esas herramientas tienen hartas limitaciones:

* conexiones inestables
* interfaces bastante limitadas
* difícil hacer operaciones continuas o experimentos

Este proyecto entrega un **software que permite la comunicación BLE y el control del robot directo desde el computador**,
para experimentar y desarrollar de forma mucho más flexible.

---

## Proyecto relacionado

Este software está pensado para funcionar junto con el siguiente programa del lado del robot:

ROBO-ONE Beginners BLE Robot Program
Author: Terukazu Nishimura @AiRRC

Este repositorio **no modifica el programa del robot**.
Lo que hace es proveer un **nuevo software controlador BLE para el lado del PC**.

---

## Funciones principales

* Conexión BLE desde el computador
* Envío de comandos al robot (adelante, atrás, izquierda, derecha, detener)
* Cambio entre modo autónomo / modo manual
* Panel de control con interfaz GUI en tkinter
* Visualización en tiempo real del log de recepción BLE
* Entorno de operación y experimentación continua

---

## Requisitos del sistema

* Python 3
* Computador con soporte para comunicación BLE
* ROBO-ONE Beginner Robot (con BLE)

---

# Cómo usar

## 0. Descarga Python
Descarga la última versión de Python 3 desde el [sitio oficial](https://www.python.org/downloads/).

## 1. Instala las librerías necesarias

Instala la librería Python necesaria para la comunicación BLE.

```bash
pip install bleak
```

Instala dependencias adicionales si es necesario.

---

## 2. Inicia el programa del robot

Graba el **programa MicroPython con BLE** en el microcontrolador del robot y enciéndelo.

Asegúrate de que el robot esté en **modo advertising BLE**.

---

### Nota: Cómo encontrar la dirección del dispositivo BLE y el UUID

La comunicación BLE necesita tanto la **dirección del dispositivo (dirección MAC)**
como el **UUID** que se usa para transmitir datos.

Puedes identificarlos con herramientas de escaneo BLE:

* `sudo hcitool lescan` (terminal Linux)
* nRF Connect (app del celular)
* BLE Scanner
* Bluetooth Developer Tools (PC)

Pasos básicos:

1. Abre una app de escaneo BLE
2. Enciende el robot
3. Selecciona el robot de la lista de dispositivos
4. Ve la lista de **Service** o **Characteristic**
5. Identifica el **UUID** que aparece

Después de obtener el UUID, configúralo en el programa del PC.

※ El BLE puede parecer complicado al principio, pero si lo revisas con estas herramientas se entiende mucho mejor la estructura de comunicación.
※ En la mayoría de los casos se usa el **Nordic UART Service**.

---

## 3. Configura la dirección del dispositivo BLE

Edita la siguiente línea en `ble_robot.py` para que coincida con la dirección Bluetooth de tu robot
(ej. Raspberry Pi Pico W):

```python
ADDRESS = "2C:CF:67:CC:B5:B4"  # ← Cambia esto por la dirección de tu dispositivo
```

Cómo encontrar tu dirección Bluetooth (Linux):

```bash
sudo hcitool lescan
```

También puedes usar **nRF Connect** (app del celular) para encontrar la dirección del dispositivo.

---

## 4. Inicia el software del PC

Ejecuta el programa controlador en el computador.

```bash
python ble_robot.py
```

---

## 5. Conecta vía BLE

Después de iniciar el programa, aparecerá una ventana GUI llamada **"ROBO BLE Controller"**.
Presiona el botón **Connect** para conectarte al robot.
Una vez conectado exitosamente, el estado cambia a **"Connected"** y ya puedes enviarle comandos al robot.

---

## Estructura de directorios

```
Beginners_auto_BLE_softwere/

├ ble_robot.py
├ README.md
├ README_en.md
├ README_es-cl.md
├ README_na.md
├ specifics_md_jp.md
├ specifics_md_en.md
├ specifics_es-cl.md
├ specifics_na.md
└ LICENSE
```

---

# Especificación de comunicación (comandos BLE)

Este software usa **BLE (Bluetooth Low Energy)** para la comunicación de comandos entre el PC y el robot.

Roles de comunicación:

* PC: BLE Central (dispositivo que conecta)
* Robot: BLE Peripheral (dispositivo que se conecta)

El PC envía comandos al robot, y el programa MicroPython del robot los recibe y ejecuta las acciones correspondientes.

La comunicación se hace principalmente con **comandos de texto simple**.

Ejemplo:

```
F
B
L
R
X
```

---

# Arquitectura de conexión

```
+--------------------+
|        PC          |
|  BLE Controller    |
|  (Python Program)  |
+---------+----------+
          |
          | Comunicación BLE
          |
+---------v----------+
|      Robot         |
|  MicroPython BLE   |
|  Servo Controller  |
+--------------------+
```

Flujo de comunicación:

1. El robot inicia el advertising BLE
2. El software PC escanea dispositivos
3. El PC conecta vía BLE
4. Se transmiten comandos
5. El robot ejecuta el comando

---

# Lista de comandos

| Comando | Acción                |
| ------- | --------------------- |
| F       | Avanzar               |
| B       | Retroceder            |
| L       | Girar a la izquierda  |
| R       | Girar a la derecha    |
| X       | Detener               |
| A       | Modo autónomo         |
| Op      | Modo operación manual |

※ El comportamiento real depende de la implementación del firmware del robot.

---

# Ejemplo de comunicación

Ejemplo de envío de comando desde el PC al robot:

```
send("F")
```

Del lado del robot:

```
Comando recibido: F
→ Ejecutar movimiento hacia adelante
```

---

# Funciones futuras planeadas

Las siguientes funciones están planeadas para más adelante:

* Feedback de sensores al PC
* Función de mapeo
* Algoritmos de navegación autónoma
* Escaneo y selección automática de dispositivos BLE

---

## Aviso de seguridad

Este software es para **experimentos y desarrollo en control de robots**.

Los robots pueden moverse de forma inesperada dependiendo de los comandos enviados.
Siempre opera el robot en un entorno seguro para evitar accidentes o daños.

---

## Licencia

Este proyecto se publica bajo la **ROBO-ONE Educational Non-Commercial License v1.0**.

Permitido:
- Uso
- Modificación
- Fork
- Redistribución
- Uso educativo y de investigación

Prohibido:
- Uso comercial
- Venta con fines de lucro

Consulta el archivo `LICENSE` para más detalles.
