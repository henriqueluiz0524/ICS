'''
Crie uma classe Carro com atributos marca e modelo.
 Crie uma classe derivada CarroEletrico
   que adicione um atributo autonomia e um método detalhes()
 para exibir as informações do carro.

'''

class carro:
    marca = ''
    modelo = ''
    autonomia = ''

    def __init__(self, marca, modelo,):
        self.marca = marca
        self.modelo = modelo
    
class CarroEletrico(carro):
    autonomia = None

    def add_info_CarroEletrico(self, autonomia_passada):
      self.autonomia = autonomia_passada

    def detalhes(self):
      return self.marca + self.modelo + str(self.autonomia)
    
carro_eletrico = CarroEletrico('BMW' 'x1')
carro_eletrico.add_info_CarroEletrico(300)
Detalhes = carro_eletrico.detalhes()
print(Detalhes)