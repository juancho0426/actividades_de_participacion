"""Cree una clase Carta que contenga dos propiedades valor y pinta, las cuales son asignadas 
solo al momento de la construcción del objeto (se pasan como parámetros en el constructor). 
Defina 4 constantes que representan los nombres de las 4 pintas que puede tener una carta."""

class Carta:
    def _init_(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

# Definición de las constantes para las pintas
CORAZON = "Corazón"
DIAMANTE = "Diamante"
TREBOL = "Trébol"
PICAS = "picas"

# Ejemplo de creación de una carta
mi_carta = Carta(7, PICAS)
print("Valor:", mi_carta.valor)
print("Pinta:", mi_carta.pinta)