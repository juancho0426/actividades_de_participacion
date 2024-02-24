#Cree una clase Punto que represente un punto en el plano cartesiano

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def _str_(self):
        return f"({self.x}, {self.y})"

# Ejemplo de uso de la clase Punto
punto1 = Punto(10,20)
print("Coordenadas del punto:", punto1)