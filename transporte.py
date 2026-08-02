from vehiculo import Vehiculo

class Transporte(Vehiculo):
    def __init__(self, marca, modelo, motor, precio_diario, capacidad_personas, tipo_traccion, terreno_ideal, rendimiento_kml):
        super().__init__(marca, modelo, motor, precio_diario, capacidad_personas, tipo_traccion, terreno_ideal, rendimiento_kml)
        
    def calcular_cotizacion(self, dias):
        return super().calcular_cotizacion(dias) + self.get_capacidad_personas()

Transporte.catalogo = {
    "1": Transporte("Mercedes-Benz", "Sprinter", "2.1L Turbodiesel", 65000, 15, "4x2", "Grupo", 9.5),
    "2": Transporte("Volkswagen", "Crafter", "2.0L TDI", 75000, 20, "4x2", "Grupo", 10.0)
}