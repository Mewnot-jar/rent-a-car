from vehiculo import Vehiculo

class AutoSuv(Vehiculo):
    def __init__(self, marca, modelo, motor, precio_diario, capacidad_personas, tipo_traccion, terreno_ideal, rendimiento_kml):
        super().__init__(marca, modelo, motor, precio_diario, capacidad_personas, tipo_traccion, terreno_ideal, rendimiento_kml)
    def calcular_cotizacion(self, dias):
        total = super().calcular_cotizacion(dias)
        if dias > 7:
            total = total * 0.90
        return total
AutoSuv.catalogo = {
    "1": AutoSuv("Toyota", "Yaris", "1.5L Gasolina", 35000, 5, "4x2", "Ciudad", 18.5),
    "2": AutoSuv("Nissan", "Qashqai", "2.0L Gasolina", 45000, 5, "AWD", "Ciudad", 14.0)
}