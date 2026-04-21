class CuentaBancaria:
    def _init_(self, numero_cuenta, titular, saldo, tipo_cuenta, activa):
        self.__numero_cuenta = numero_cuenta
        self.__titular = titular
        self.__saldo = saldo
        self.__tipo_cuenta = tipo_cuenta
        self.__activa = activa

    # GETTERS
    def get_numero_cuenta(self):
        return self.__numero_cuenta

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_tipo_cuenta(self):
        return self.__tipo_cuenta

    def get_activa(self):
        return self.__activa

    # SETTERS
    def set_titular(self, titular):
        self.__titular = titular

    def set_tipo_cuenta(self, tipo_cuenta):
        self.__tipo_cuenta = tipo_cuenta

    def set_activa(self, activa):
        self.__activa = activa

    # MÉTODO 1: depositar dinero
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print("Depósito realizado")
        else:
            print("Cantidad inválida")

    # MÉTODO 2: retirar dinero
    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print("Retiro realizado")
        else:
            print("Fondos insuficientes")



