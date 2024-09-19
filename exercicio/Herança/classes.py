class Pessoa:
    def __init__(self, nome, sobrenome, idade) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def calcula_ano_nascimento(self):
        return 2024 - self.idade

    def busca_dados_completos(self):
        return{
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'idade': self.idade

        }    
    
class Funcionario(Pessoa):
    cargo = None
    departamento = None

    def add_info_funcionario(self, cargo, departamento) -> None:
        self.cargo = cargo
        self.departamento = departamento

    def busca_dados_completos(self):
        return {
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'idade': self.idade,
            'cargo': self.cargo,
            'departamento': self.departamento
        }
    
class Gerente(Funcionario):
    def busca_departamento(self):
        return self.departamento