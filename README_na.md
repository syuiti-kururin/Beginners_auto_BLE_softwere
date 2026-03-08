# ROBO-ONE Beginners Auto BLE PC Controller

## Ñurod
Eket software e PC controller ñan student it eron emen robot BLE eabwi ROBO-ONE.

---

## Ibwija eket software

Amo emenemen robot ñan ROBO-ONE Beginners ama eabwi robot eabwir.
Iamörin, emo emenemen, amo ibwanin **BLE (Bluetooth Low Energy)** e haro mabir.

Ipako:

* App BLE imōn tēlpon e käen operur bwio
* Tesuto ama debug e mabir
* Ñañanin emen program e mabir

Iamörin, amo emenemen **BLE controller eboa Python ñan ekamöak imōn kompiuta**.

---

## Ibwija ideburani eket

Eket repository, amo ideburan **BLE controller software ñan PC**.

Iamörin, eket software e **emen neine ñōrōr**, ama bai itsi e ñōr imōnen amo ikanak.

Eket ideburan:

* Simple awöi itsi
* Ekabwi ikakōkō
* Ñanan emen mōrōñōr

Ñan, eket e **versi simple awöi itsi**.

---

## Ikakōkō imōn eket

Amo inin neine ōrōr täkin.
Amo emenemen robot amen **iru ikakōkō iru**, de a poco.

Iamörin, eket software e neine

"tool owieji"

imwi e

**"eabwir ñan omo ikakōkō ama emen mōrōñōr imōm".**

Bwio itsi eket software e **ñurod imōn** ñan:

* Eit eron tesuto BLE
* Student eron eabwi robot autónomo ROBO-ONE
* Eit eron tesuto control robot

---

## Ibwija eket software

Eket software e **controller ñan PC** ñan robot **ROBO-ONE Beginners BLE**.

Ōrrōr, BLE communication e emen ñan app imōn tēlpon
(Bacon ama Bluetooth Connect ekamōar),
iamörin ñan control robot, eket tool e mabir:

* Conexión e mabir
* Interface e kimi
* Tesuto continuo e mabir

Iamörin eket software, **BLE communication ama control robot imōn kompiuta** e bwio itsi.

---

## Projekt ōrrōr

Eket software eabwir ñan program robot ōrrōr:

ROBO-ONE Beginners BLE Robot Program
Author: Terukazu Nishimura @AiRRC

Eket repository **e neine mōrōñ program robot**.
Imwi e **software controller BLE ñan PC**, eboa emen.

---

## Función owieji

* Conexión BLE imōn kompiuta
* Envío comando ñan robot (tōñ, ōrrōr, kiu, ri, detener)
* Cambio modo autónomo / modo manual
* Panel GUI ñan tkinter
* Log BLE real-time
* Tesuto continuo

---

## Eabwi sistema

* Python 3
* Kompiuta e BLE
* ROBO-ONE Beginner Robot (BLE)

---

# Ekamöak itsiwa

## 0. Iniow Python
Download Python 3 imōn [sitio oficial](https://www.python.org/downloads/).

## 1. Instalar librería

Instalar librería Python ñan BLE.

```bash
pip install bleak
```

---

## 2. Iniow program robot

Grab MicroPython BLE ñan microcontrolador robot ama iniow.

Asegúrate robot e **modo advertising BLE**.

---

### Ibwija: Ekamöak address BLE ama UUID

BLE communication e ebar **address imōn device (dirección MAC)**
ama **UUID** ñan data transmisión.

Scan tools:

* `sudo hcitool lescan` (terminal Linux)
* nRF Connect (app tēlpon)
* BLE Scanner
* Bluetooth Developer Tools (PC)

Pasos:

1. Iniow app scan BLE
2. Iniow robot
3. Select robot imōn lista
4. Ve lista **Service** ama **Characteristic**
5. Confirm **UUID**

Configure UUID ñan program PC.

※ BLE e mabir itsi iamörin, scan tools e bwio ñan ikakōkō.
※ Ōrrōr e emen **Nordic UART Service**.

---

## 3. Configure address BLE

Edit eket línea imōn `ble_robot.py` ñan address Bluetooth imōm robot
(ej. Raspberry Pi Pico W):

```python
ADDRESS = "2C:CF:67:CC:B5:B4"  # ← Cambiar ñan address imōm device
```

Ekamöak address Bluetooth (Linux):

```bash
sudo hcitool lescan
```

Ama bai nRF Connect (app tēlpon) e bwio ñan ekamöak address.

---

## 4. Iniow software PC

Ejecutar program controller imōn kompiuta.

```bash
python ble_robot.py
```

---

## 5. Conexión BLE

Iniow program, ventana GUI **"ROBO BLE Controller"** e iriow.
Press botón **Connect** ñan conectar robot.
Conexión bwio, status e cambiar a **"Connected"**, ama bai enviar comando robot.

---

## Estructura directorio

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

# Especificación comunicación BLE

Eket software e emen **BLE (Bluetooth Low Energy)** ñan comunicación comando PC ama robot.

Función:

* PC: BLE Central (conectar)
* Robot: BLE Peripheral (conectado)

PC e enviar comando ñan robot,
program MicroPython robot e recibir ama ejecutar.

Comunicación e emen **comando texto simple**.

Ej.:

```
F
B
L
R
X
```

---

# Arquitectura conexión

```
+--------------------+
|        PC          |
|  BLE Controller    |
|  (Python Program)  |
+---------+----------+
          |
          | BLE
          |
+---------v----------+
|      Robot         |
|  MicroPython BLE   |
|  Servo Controller  |
+--------------------+
```

Flujo:

1. Robot iniow advertising BLE
2. Software PC scan device
3. PC conectar BLE
4. Enviar comando
5. Robot ejecutar

---

# Lista comando

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

# Ejemplo comunicación

Enviar comando PC ñan robot:

```
send("F")
```

Robot:

```
Recibir: F
→ Avanzar
```

---

# Función futuro

* Sensor feedback ñan PC
* Función mapeo
* Algoritmo navegación autónoma
* Scan ama select automático device BLE

---

## Aviso seguridad

Eket software e ñan **tesuto ama educación control robot**.

Robot e bai mover inesperadamente.
Siempre operar robot imōn lugar bwio ñan evitar accidente.

---

## Licencia

Eket project e distribuir ñan **ROBO-ONE Educational Non-Commercial License v1.0**.

Permitido:
- Uso
- Modificación
- Fork
- Redistribución
- Uso educativo

Prohibido:
- Uso comercial
- Venta

Ver archivo `LICENSE`.
