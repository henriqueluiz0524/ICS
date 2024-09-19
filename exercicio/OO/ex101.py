'''
Crie uma classe Pessoa com atributos nome e idade.
 Crie uma classe derivada Estudante que adiciona um atributo matricula
 e um método exibir_informacoes() que exibe todos os detalhes.
'''

class pessoa:
    def init(self,_nome,_idade):
        self.nome = _nome
        self.idade = _idade

class estudante(pessoa):
    escola = None
    serie = None
    frequencia = None

    def add_info_estudante(self, escola, serie, frequencia):
        self.escola = escola
        self.serie = serie
        self.frequencia = frequencia

    def retornar_informacoes(self):
        return self.nome + str(self.idade) + self.escola + self.serie + self.frequencia

Estudante = estudante("Luiz Moura ", 16)
Estudante.add_info_estudante(" escola silva de alencar ", "2 ano ", " 3")
exibir_informacoes = Estudante.retornar_informacoes()
print(exibir_informacoes)