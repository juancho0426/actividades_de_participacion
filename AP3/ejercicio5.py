"""Cree una clase Circulo que tenga las propiedades centro y radio, las cuales 
se inicializan con parámetros en el constructor. Defina métodos en la clase para 
calcular el área, el perímetro e indicar si un punto pertenece al círculo o no."""

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio ** 2

    def perimetro(self):
        return 2 * 3.1416 * self.radio

    def pertenece(self, punto):
        distancia = ((punto[0] - self.centro[0]) * 2 + (punto[1] - self.centro[1]) * 2) ** 0.5
        return distancia <= self.radio


circulo = Circulo((0, 0), 5)

print("Área:", circulo.area())
print("Perímetro:", circulo.perimetro())
print("¿Pertenece el punto (10, 20) al círculo?", circulo.pertenece((10, 20)))
print("¿Pertenece el punto (15, 30) al círculo?", circulo.pertenece((15, 30)))