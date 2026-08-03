# Sistema de Cotización Rent-a-Car

Una aplicación de consola desarrollada en Python para la recomendación y cotización de arriendo de vehículos. El sistema evalúa las necesidades del cliente (cantidad de pasajeros, tipo de terreno y días de alquiler) para sugerir el vehículo óptimo y calcular el costo total.

## Características Principales

* **Cuestionario Interactivo:** Interfaz de línea de comandos (CLI) que guía al usuario para encontrar su vehículo ideal.
* **Validación de Inteligencia:** Verifica automáticamente si la capacidad del vehículo seleccionado es suficiente para el número de pasajeros indicado.
* **Catálogo Dinámico:** Los vehículos se generan y muestran dinámicamente a través de diccionarios a nivel de clase, evitando el *hardcoding*.
* **Cotización Precisa:** Cálculo del total a pagar que incluye tarifas base, descuentos por cantidad de días y recargos específicos según el tipo de vehículo (ej. seguros 4x4 o impuestos de carga pesada).

## Arquitectura y Conceptos POO Aplicados

Este proyecto fue diseñado aplicando los 4 pilares fundamentales de la Programación Orientada a Objetos:

1. **Abstracción y Herencia:**
   * Creación de una clase padre o superclase (`Vehiculo`) que centraliza los atributos y comportamientos comunes.
   * 4 clases hijas especializadas (`AutoSuv`, `Camioneta`, `Camion`, `Transporte`) que heredan de la clase base.

2. **Encapsulamiento:**
   * **Atributos Protegidos (`_marca`, `_modelo`, `_motor`):** Definen la identidad inmutable del vehículo y permiten fácil acceso a las clases hijas.
   * **Atributos Privados (`__precio_diario`, `__capacidad_personas`, etc.):** Protegen las variables críticas de negocio y lógica matemática, exigiendo el uso de métodos *Getters* y *Setters* para evitar estados corruptos (ej. precios negativos).

3. **Polimorfismo:**
   * Sobrescritura de métodos como `calcular_cotizacion()` y `mostrar_ficha_tecnica()`. Cada clase hija responde al mismo llamado desde el `main.py`, pero ejecuta su propia lógica interna (aplicando sus propios recargos o descuentos).

## Estructura del Proyecto

rent-a-car/
│
├── main.py            # Punto de entrada principal y lógica de menús
├── vehiculo.py        # Clase base (Superclase)
├── auto_suv.py        # Clase hija para vehículos de ciudad
├── camioneta.py       # Clase hija para todo terrenos (4x4)
├── camion.py          # Clase hija para vehículos de carga pesada
├── transporte.py      # Clase hija para traslado de grupos
└── README.md          # Documentación del proyecto

## Diagrama de flujo

<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/b4ef5349-8005-471a-920a-f668a134c64e" />

## Diagrama de clases

<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/9114da8b-fd7f-4c4d-a076-bab53b04fad5" />

