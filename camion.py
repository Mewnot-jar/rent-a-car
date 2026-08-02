from vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, marca, modelo, precio_diario, capacidad_personas, tipo_traccion, terreno_ideal, rendimiento_kml, impuesto_carga_pesada=15000):
        super().__init__(marca, modelo, precio_diario, capacidad_personas, tipo_traccion, terreno_ideal, rendimiento_kml)
        self.impuesto_carga_pesada = impuesto_carga_pesada

        self.modelos = {
            "Fighter": {
                "motor": "7.5L Diesel", 
                "capacidad_personas": 3,
                "traccion": "6x4",
                "rendimiento": 5.0,
                "precio_dia": 90000

            },
            "Accelo": {
                "motor": "4.8L Diesel", 
                "capacidad_personas": 3,
                "traccion": "4x2",
                "rendimiento": 7.0,
                "precio_dia": 75000
            
            },
        }

    def calcular_cotizacion(self, dias):
        return super().calcular_cotizacion(dias) + self.impuesto_carga_pesada