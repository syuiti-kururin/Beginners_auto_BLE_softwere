# ROBO-ONE Beginners Auto BLE PC Controller

Software de control BLE para PC diseñado para robots de la serie ROBO-ONE.

Este proyecto fue creado para resolver problemas de conexión y operación
que ocurren cuando se usan aplicaciones de smartphone como:

- Bacon
- Bluetooth Connect
- otras aplicaciones BLE genéricas

Estas aplicaciones pueden ser difíciles de usar cuando se intenta
controlar un robot durante pruebas o desarrollo.

Por esta razón, este proyecto proporciona un software simple para PC
escrito en Python que permite conectarse al robot mediante BLE y
enviar comandos fácilmente.

---

# Propósito del proyecto

Este proyecto fue creado como una herramienta inicial para estudiantes
que quieren participar en competiciones como:

- ROBO-ONE
- ROBO-ONE Light
- ROBO-ONE Auto
- ROBO-ONE Kendo
- ROBO-ONE Begginar

Muchos participantes son estudiantes jóvenes, incluso de escuela primaria.
Por eso este software se diseñó para ser:

- simple
- fácil de entender
- fácil de modificar

El objetivo **no es entregar un sistema completo**, sino proporcionar
un punto de partida desde el cual cada estudiante pueda investigar,
modificar y mejorar el código por sí mismo.

---

# Importante

El código publicado en este repositorio es **una versión simple**.

No es la versión más reciente ni la más avanzada.

Se publica intencionalmente en un estado simple para que sea más fácil
de entender y modificar.

---

# Requisitos

- Python 3
- Adaptador BLE en el PC
- Robot compatible con BLE

Bibliotecas Python:


bleak
asyncio


Instalar:


pip install bleak


---

# Uso básico

1. Iniciar el programa BLE en el robot (MicroPython)
2. Confirmar que el robot está en modo advertising BLE
3. Ejecutar el software de PC
4. Conectarse al robot
5. Enviar comandos BLE

---

# Documentación técnica

La especificación completa está disponible en:


Specifics_md.md


Versiones en otros idiomas:


Specifics_en.md
Specifics.na.md
Specifics.es-CL.md


---

# Licencia

Este proyecto está publicado bajo una licencia educativa personalizada.

Uso permitido:

- uso personal
- uso educativo
- modificación
- redistribución

No permitido:

- uso comercial

Ver archivo `LICENSE` para detalles.

---

# Autor

Proyecto desarrollado por un estudiante de KOSEN
durante el desarrollo de robots ROBO-ONE.
