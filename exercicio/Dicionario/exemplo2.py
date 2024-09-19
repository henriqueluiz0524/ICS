from typing import list

class itensPedido:
    codigoBarra = None
    presco = None
    qtd = 0

    def __init__(self, codigoBarra, presco, qtd):
        codigoBarra = codigoBarra
        presco = presco
        qtd = qtd


    class pedido:
        id = None
        itensPedido = list[itensPedido]
        imposto = 0
        desconto = 0
        total = 0

        def __init__(self, itensPedido: list[itensPedido], desconto: float): pass

item1 = itensPedido

novo_pedido = Pedido()