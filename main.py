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
                print("Error: La cantidad de dias debe ser mayor a 0.")
        except ValueError:
            print("Error: Por favor ingresa un numero valido.")
    return pasajeros, terreno, dias
            
def evaluar_opcion(pasajeros, terreno, dias):
    vehiculo_elegido = None

    match terreno:
        case "1":
            print("Modelos Auto/Suv: ")
            print("1. Toyota Yaris ($35.000/dia - Traccion 4x2)")
            print("2. Toyota RAV4 ($45.000/dia - Traccion AWD)")
            while True:
                eleccion = input("Elige el modelo que prefieras: ")
                if eleccion == "1":
                    vehiculo_elegido = AutoSuv("Toyota", "Yaris", 35000, 5, "4x2", "Ciudad", 18.5)
                    break
                elif eleccion == "2":
                    vehiculo_elegido = AutoSuv("Toyota", "RAV4", 45000, 5, "AWD", "Ciudad", 14.0)
                    break
                print("Error: Opcion no valida.")
        case "2":
            print("Modelos todo terreno: ")
            print("1. Toyota Hilux ($55.000/día - 4x4)")
            print("2. Ford Ranger ($58.000/día - 4x4)")
            while True:
                eleccion = input("Elige el modelo que prefieras: ")
                if eleccion == "1":
                    vehiculo_elegido = Camioneta("Toyota", "Hilux", 55000, 5, "4x4", "Nieve/Playa", 12.0)
                    break
                elif eleccion == "2":
                    vehiculo_elegido = Camioneta("Ford", "Ranger", 58000, 5, "4x4", "Nieve/Playa", 11.5)
                    break
                print("Error: Opcion no valida.")       
        case "3":
            print("Modelos de carga pesada: ")
            print("1. Fuso Fighter ($90.000/día - 6x4)")
            print("2. Mercedes Accelo ($75.000/día - 4x2)")
            while True:
                eleccion = input("Elige el modelo que prefieras: ")
                if eleccion == "1":
                    vehiculo_elegido = Camion("Fuso", "Fighter", 90000, 3, "6x4", "Trabajo Pesado", 5.0)
                    break
                elif eleccion == "2":
                    vehiculo_elegido = Camion("Mercedes", "Accelo", 75000, 3, "4x2", "Trabajo Pesado", 7.0)
                    break
                print("Error: Opcion no valida.")
        case "4":
            print("Modelos de transporte de grupo: ")
            print("1. Mercedes Sprinter (Capacidad: 15 pasajeros)")
            print("2. Volkswagen Crafter (Capacidad: 20 pasajeros)")
            while True:
                eleccion = input("Elige el modelo que prefieras: ")
                if eleccion == "1":
                    vehiculo_elegido = Transporte("Mercedes", "Sprinter", 65000, 15, "4x2", "Grupo", 9.5)
                    break
                elif eleccion == "2":
                    vehiculo_elegido = Transporte("Volkswagen", "Crafter", 75000, 20, "4x2", "Grupo", 10.0)
                    break
                print("Error: Opcion no valida.")
    print(f"Has elegido un {vehiculo_elegido._marca} {vehiculo_elegido._modelo}")
    if pasajeros > vehiculo_elegido.get_capacidad_personas():
        print(f"ALERTA: El vehiculo que elegiste cuenta con capacidad para {vehiculo_elegido.get_capacidad_personas()} personas.")
        print(f"Pero indicaste que viajan {pasajeros} personas.")
        print("Sugerencia: Reinicia el programa y elige una opcion de Modelos de transporte de grupo.")
    else:
        print(f"Validacion completada: El vehiculo elegido cumple con las caracteristicas solicitadas.")
        return vehiculo_elegido
def generar_cotizacion(vehiculo, dias):
    vehiculo.mostrar_ficha_tecnica()
    total_a_pagar = vehiculo.calcular_cotizacion(dias)
    print(f"El total a pagar es: ${total_a_pagar}")

pasajeros, terreno, dias = mostrar_cuestionario()
vehiculo_listo = evaluar_opcion(pasajeros, terreno, dias)
if vehiculo_listo is not None:
    generar_cotizacion(vehiculo_listo, dias)