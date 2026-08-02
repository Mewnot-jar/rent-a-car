from vehiculo import Vehiculo

class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, precio_diario, capacidad_personas, tipo_traccion, terreno_ideal, rendimiento_kml, seguro_4x4_diario=5000):
        super().__init__(marca, modelo, precio_diario, capacidad_personas, tipo_traccion, terreno_ideal, rendimiento_kml)
        self.seguro_4x4_diario = seguro_4x4_diario

        self.modelos = {
            "Hilux": {
                "motor": "2.4L Diesel", 
                "capacidad_personas": 5,
                "traccion": "4x4",
                "rendimiento": 12.0,
                "precio_dia": 55000

            },
            "Ranger": {
                "motor": "2.0L Diesel", 
                "capacidad_personas": 5,
                "traccion": "AWD",
                "rendimiento": 11.5,
                "precio_dia": 58000
            
            },
        }

    def calcular_cotizacion(self, dias):
        return (self.get_precio_diario() + self.seguro_4x4_diario) * dias