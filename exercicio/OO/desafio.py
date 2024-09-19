class calculadora_impostos:
    def calcular_impostos(self, valor):
        return (valor * 12) / 100

calculadora = calculadora_impostos()
print(calculadora.calcular_impostos(100))

class calculadoraiof(calculadora_impostos):
    def calculariof(self, valor):
        return (valor * 1) / 100
    
calculadora = calculadoraiof()
print(calculadora.calculariof(500))

class CalculadoraSimples(calculadora_impostos):
    def calcular_simples(self, valor):
        return (valor * 2) / 100
    
    def calcula_total_impostos(self, valor):
        impostos1 = calculadora.calcular_impostos(100)
        impostos2 = calculadora.calcular_simples(100)
        print
    
calculadora = CalculadoraSimples()
impostos1 = calculadora.calcular_impostos(100)
impostos2 = calculadora.calcular_simple(100)
print(str(impostos1 + impostos2))
    
    
