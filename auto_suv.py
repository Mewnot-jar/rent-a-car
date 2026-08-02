from vehiculo import Vehiculo

class AutoSuv(Vehiculo):
    def __init__(self, marca, modelo, precio_diario, capacidad_personas, tipo_traccion, terreno_ideal, rendimiento_kml):
        super().__init__(marca, modelo, precio_diario, capacidad_personas, tipo_traccion, terreno_ideal, rendimiento_kml)

        self.modelos = {
            "Yaris": {
                "motor": 1.5, 
                "capacidad_personas": 5,
                "traccion": "4x2",
                "rendimiento": 18.5,
                "precio_dia": 35000

            },
            "RAV4": {
                "motor": 2.5, 
                "capacidad_personas": 5,
                "traccion": "AWD",
                "rendimiento": 14.0,
                "precio_dia": 45000
            
            },
        }

    def calcular_cotizacion(self, dias):
        total = super().calcular_cotizacion(dias)
        if dias > 7:
            total = total * 0.90
        return total