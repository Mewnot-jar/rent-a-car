from auto_suv import AutoSuv
from camioneta import Camioneta
from camion import Camion
from transporte import Transporte

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
                print("Error: La cnatidad de dias debe ser mayor a 0.")
        except ValueError:
            print("Error: Por favor ingresa un numero valido.")
    return pasajeros, terreno, dias

mostrar_cuestionario()