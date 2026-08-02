from auto_suv import AutoSuv
from camioneta import Camioneta
from camion import Camion
from transporte import Transporte

flota = {
    "1": AutoSuv.catalogo,
    "2": Camioneta.catalogo,
    "3": Camion.catalogo,
    "4": Transporte.catalogo
}

def mostrar_cuestionario():
    print("------- CUESTIONARIO PA' SABER QUE AUTO TE CONVIENE Y NO PAGUI' DE MAS -------")


    while True:
        try:
            pasajeros = int(input("I. Cantidad de pajeros que llevaras: "))
            if pasajeros > 0 and pasajeros <= 20:
                break
            else:
                print("Error: El numero de pasajeros no es valido (1 - 20)")
        except ValueError:
            print("Error: Por favor ingresa un numero valido (1 - 20)")

    print("II. Que tipo de terreno transitaras:")
    print("1. Ciudad / Paseo Familiar")
    print("2. Nieve / Playa / Todo terreno")
    print("3. Trabajo pesado / Trabajo de carga")
    print("4. Traslado de varios pasajeros")

    while True:
        terreno = input("Elige una opcion (1-4): ")
        if terreno in ["1", "2", "3", "4"]:
            break
        else:
            print("Error: Opcion no valida. Debes ingresar una de las opciones mostradas (1 - 4).")
    while True:
        try:
            dias = int(input("III. Dias que durara el alquiler: "))
            if dias > 0:
                break
            else:
                print("Error: La cantidad de dias debe ser mayor a 0.")
        except ValueError:
            print("Error: Por favor ingresa un numero valido.")
    return pasajeros, terreno, dias
            
def evaluar_opcion(pasajeros, terreno):
    modelos_disponibles = flota[terreno]
    print("------- Modelos disponibles para el terreno elegido -------")
    for clave, vehiculo in modelos_disponibles.items():
        print(f"{clave}.{vehiculo._marca} {vehiculo._modelo}")
        print(f"  Motor: {vehiculo._motor}")
        print(f"  Precio: ${vehiculo.get_precio_diario()} / dia")
    while True:
        eleccion = input("Elige el modelo que prefieras: ")
        if eleccion in modelos_disponibles:
            vehiculo_elegido = modelos_disponibles[eleccion]
            break
        else:
            print("Error: Opcion no valida.")
    print(f"Has elegido un {vehiculo_elegido._marca} {vehiculo_elegido._modelo}")
    if pasajeros > vehiculo_elegido.get_capacidad_personas():
        print(f"ALERTA: El vehiculo que elegiste cuenta con capacidad para {vehiculo_elegido.get_capacidad_personas()} personas. Pero indicaste que viajan {pasajeros} personas.")
        print("Sugerencia: Reinicia el programa y elige una opcion de Modelos de transporte de grupo.")
        return None
    else:
        print(f"Validacion completada: El vehiculo elegido cumple con las caracteristicas solicitadas.")
        return vehiculo_elegido
    
def generar_cotizacion(vehiculo, dias):
    vehiculo.mostrar_ficha_tecnica()
    total_a_pagar = vehiculo.calcular_cotizacion(dias)
    print(f"El total a pagar es: ${total_a_pagar}")

pasajeros, terreno, dias = mostrar_cuestionario()
vehiculo_listo = evaluar_opcion(pasajeros, terreno)
if vehiculo_listo is not None:
    generar_cotizacion(vehiculo_listo, dias)