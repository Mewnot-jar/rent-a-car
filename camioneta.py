from vehiculo import Vehiculo

class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, motor, precio_diario, capacidad_personas, tipo_traccion, terreno_ideal, rendimiento_kml, seguro_4x4_diario=5000):
        super().__init__(marca, modelo, motor, precio_diario, capacidad_personas, tipo_traccion, terreno_ideal, rendimiento_kml)
        self.seguro_4x4_diario = seguro_4x4_diario

    def calcular_cotizacion(self, dias):
        return (self.get_precio_diario() + self.seguro_4x4_diario) * dias
Camioneta.catalogo = {
    "1": Camioneta("Toyota", "Hilux", 2.4, 55000, 5, "4x4", "Nieve/Playa", 12.0),
    "2": Camioneta("Ford", "Ranger", 2.0, 58000, 5, "4x4", "Nieve/Playa", 11.5)
}