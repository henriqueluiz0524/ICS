class Produto:
    preco = 0

def seta_preco(self, _preco):
    if _preco < 0:
        print('preço invalido, o preco nao pode ser nagativo')

    else:
        self.preco = _preco

class ProdutodEletronico(Produto)
    garantia = 