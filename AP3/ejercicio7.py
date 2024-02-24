"""Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, 
propietarios y balance. Los tres atributos se deben inicializar en el constructor con valores 
recibidos como parámetros."""

class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance


mi_cuenta = CuentaBancaria("9800234567", ["juan", "juliana"], 1580000.00)
print("Número de cuenta:", mi_cuenta.numero_cuenta)
print("Propietarios:", mi_cuenta.propietarios)
print("Balance:", mi_cuenta.balance)