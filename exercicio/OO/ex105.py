'''
Crie uma classe ContaBancaria 
com métodos para depositar() e sacar().
Crie uma classe derivada ContaPoupanca que adicione um método calcular_rendimento().
'''
class ContaBancaria:
    def __init__(self, deposito, saque) -> None:
        self.deposito = deposito
        self.saque = saque
    
    def depositar(self):
        self.deposito = None
        self.saque = None

    def sacar(self):