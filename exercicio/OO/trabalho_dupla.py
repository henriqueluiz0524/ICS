class Veiculo:
    marca = None
    modelo = None
    ano = None

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class Carro(Veiculo):
    numero_de_portas = None

    def add_info_carro(self, numero_de_portas):
        self.numero_portas = numero_de_portas

    def Descrever_carro(self):
        return "Este é um " + self.marca + self.modelo + " do ano " + str(self.ano) + " com " + str(self.numero_portas) + " Portas. "

class Motocicleta(Veiculo):
    cilindrada = None

    def add_info_motocicleta(self, cilindrada):
        self.cilindrada = cilindrada

    def Descrever_motocicleta(self):
        return "Esta é uma motocicleta " + self.marca + self.modelo + " do ano " + str(self.ano) + " com " + str(self.cilindrada) + "cc"
    
carro = Carro("Toyota ", "Corolla ", 2018)
carro.add_info_carro(4)
exibir_dados_carro = carro.Descrever_carro()
print(exibir_dados_carro)

carro2 = Carro("Ford ", "Fusion ", 2017)
carro2.add_info_carro(4)
exibir_dados_carro2 = carro2.Descrever_carro()
print(exibir_dados_carro2)

motocicleta = Motocicleta("Honda ", "CBR500R ", 2020 )
motocicleta.add_info_motocicleta(500)
exibir_dados_motocicleta = motocicleta.Descrever_motocicleta()
print(exibir_dados_motocicleta)

motocicleta2 = Motocicleta("Yamaha ", "MT-07 ", 2019 )
motocicleta2.add_info_motocicleta(689)
exibir_dados_motocicleta2 = motocicleta2.Descrever_motocicleta()
print(exibir_dados_motocicleta2)