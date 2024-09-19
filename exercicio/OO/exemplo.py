# classes
# Objetos

class Pessoa:
    nome = ''
    sobrenome = ""
    idade = None
    profissao = "estagiario"

    # metodo construtor
    def __init__(self, nome_passado, sobrenome_passado, idade_passada):
        self.nome = nome_passado
        self.sobrenome = sobrenome_passado
        self.idade = idade_passada

    def retorna_nome_completo(self):
        return self.nome + self.sobrenome
    
    def imprime_dados_completo(self):
        return self.nome + ' ' + self.sobrenome + ' ' + str(self.idade)
    
# instanciar um objeto
pessoa = Pessoa('luiz', 'moura', 17)
print(pessoa.imprime_dados_completo())  



