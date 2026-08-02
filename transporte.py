from vehiculo import Vehiculo

class Transporte(Vehiculo):
    def __init__(self, marca, modelo, precio_diario, capacidad_personas, tipo_traccion, terreno_ideal, rendimiento_kml):
        super().__init__(marca, modelo, precio_diario, capacidad_personas, tipo_traccion, terreno_ideal, rendimiento_kml)

        self.modelos = {
            "Sprinter": {
                "motor": "2.1L Diesel", 
                "capacidad_personas": 15,
                "traccion": "4x2",
                "rendimiento": 9.5,
                "precio_dia": 65000

            },
            "Crafter": {
                "motor": "2.0L Diesel", 
                "capacidad_personas": 20,
                "traccion": "4x2",
                "rendimiento": 10.0,
                "precio_dia": 75000
            
            },
        }

    def calcular_cotizacion(self, dias):
        return super().calcular_cotizacion(dias) + self.get_capacidad_personas()