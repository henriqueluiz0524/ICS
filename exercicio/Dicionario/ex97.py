class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return self.idade

class Trabalhador(Pessoa):
    def __init__(self, nome, idade, empresa):
        super().__init__(nome, idade) 
        self.empresa = empresa
    
    def get_empresa(self):
        return self.empresa

if __name__ == "__main__":
    trabalhador1 = Trabalhador("João", 30, "Empresa XPTO")
    
    print("Nome:", trabalhador1.get_nome()) 
    print("Idade:", trabalhador1.get_idade()) 
    
    print("Empresa:", trabalhador1.get_empresa())