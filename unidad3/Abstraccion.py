from abc import ABC, abstractmethod

# Clase abstracta
class Vehiculo(ABC):
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def __str__(self):
        return f"Vehículo genérico: {self.marca} {self.modelo} ({self.año}) - Color: {self.color}"


# Subclases que heredan solo los atributos
class Auto(Vehiculo):
    pass


class Moto(Vehiculo):
    pass


class Camion(Vehiculo):
    pass


class helicoptero(Vehiculo):
    pass


# Crear objetos de las clases hijas
auto1 = Auto("Toyota", "Corolla", 2022, "Rojo")
auto2 = Auto("Nissan", "Altima", 2007, "Azul")
moto1 = Moto("Yamaha", "FZ", 2021, "Negra")
moto2 = Moto("Kawasaki", "ninja", 2021, "Negra")
camion1 = Camion("Volvo", "FH", 2020, "Blanco")
camion2 = Camion("mercedes", "AMG", 2023, "Blanco")
helicoptero1 = helicoptero("Boeing", "apache", 2021, "gris")
helicoptero2 = helicoptero("Boeing", "747", 2022, "verde")

# Visualización
print(auto1)
print(auto2)
print(moto1)
print(moto2)
print(camion1)
print(camion2)
print(helicoptero1)
print(helicoptero2)