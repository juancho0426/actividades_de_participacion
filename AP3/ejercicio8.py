""" Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito
 en la cuenta."""

class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance
        self.balance = balance

    def depositar(self, cantidad):
        self.balance += cantidad
        print("Se depositaron", cantidad, "en la cuenta.")
        print("Nuevo balance:", self.balance)

mi_cuenta = CuentaBancaria("9800234567", ["juan", "juliana"], 1580000.00)
mi_cuenta.depositar(420000.00)