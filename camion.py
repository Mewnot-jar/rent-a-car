from vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, marca, modelo, motor, precio_diario, capacidad_personas, tipo_traccion, terreno_ideal, rendimiento_kml, impuesto_carga_pesada=15000):
        super().__init__(marca, modelo, motor, precio_diario, capacidad_personas, tipo_traccion, terreno_ideal, rendimiento_kml)
        self.impuesto_carga_pesada = impuesto_carga_pesada

    def calcular_cotizacion(self, dias):
        return super().calcular_cotizacion(dias) + self.impuesto_carga_pesada
Camion.catalogo = {
    "1": Camion("Fuso", "Fighter", "7.5L Diesel", 90000, 3, "6x4", "Trabajo Pesado", 5.0),
    "2": Camion("Mercedes-Benz", "Accelo", "4.8L Diesel", 75000, 3, "4x2", "Trabajo Pesado", 7.0)
}