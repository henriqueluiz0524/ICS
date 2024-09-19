'''
 Dado um dicionário de produtos e seus preços, escreva um programa que filtre
   e exiba apenas os produtos que custam mais de um determinado valor.
'''

produtos_precos = {
    "Notebook": 3500.00,
    "Smartphone": 2000.00,
    "Tablet": 1200.00,
    "Fone de Ouvido": 300.00,
    "Mouse": 150.00,
    "Teclado": 200.00
}

valor_minimo = 1000.00

print(f"Produtos com preço maior que R${valor_minimo:.2f}:")
for produto, preco in produtos_precos.items():
    if preco > valor_minimo:
        print(f"{produto}: R${preco:.2f}")
