class Vehiculo:
    def __init__(self, marca, modelo, precio_diario, capacidad_personas, tipo_traccion, terreno_ideal, rendimiento_kml):
        #atributos protegidos
        self._marca = marca
        self._modelo = modelo

        #atributos privados
        self.set_precio_diario(precio_diario)
        self.__capacidad_personas = capacidad_personas
        self.__tipo_traccion = tipo_traccion
        self.__terreno_ideal = terreno_ideal
        self.__rendimiento_kml = rendimiento_kml

    def get_precio_diario(self):
        return self.__precio_diario

    def set_precio_diario(self, nuevo_precio):
        if nuevo_precio <= 0:
            print(f"Alerta: el precio ${nuevo_precio} no es valido. Se asignara la tarifa Base $10000")
            self.__precio_diario = 10000
        else:
            self.__precio_diario = nuevo_precio

    def get_capacidad_personas(self):
        return self.__capacidad_personas

    def get_tipo_traccion(self):
        return self.__tipo_traccion

    def get_terreno_ideal(self):
        return self.__terreno_ideal

    def get_rendimiento_kml(self):
        return self.__rendimiento_kml

    def calcular_cotizacion(self, dias):
        return self.get_precio_diario() * dias

    def mostrar_ficha_tecnica(self):
        print("------- FICHA TECNICA -------")
        print(f"Marca:            {self.marca}")
        print(f"Modelo:           {self.modelo}")
        print(f"Capacidad:        {self.get_capacidad_personas()}")
        print(f"Traccion:         {self.get_tipo_traccion()}")
        print(f"Rendimiento:      {self.get_rendimiento_kml()}")
        print(f"Precio por dia:   ${self.get_precio_diario()}")
        print("-----------------------------")

auto = Vehiculo("Toyota", "Corolla", -20000, 5, "Delantero", 14)
auto.mostrar_ficha_tecnica()