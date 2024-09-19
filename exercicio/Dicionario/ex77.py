'''
Escreva um programa que conte o número de itens (pares chave-valor) presentes no dicionário.
'''

paises_capitais = {
    "Brasil": "Brasília",
    "Estados Unidos": "Washington D.C.",
    "França": "Paris",
    "Japão": "Tóquio",
    "Austrália": "Camberra",
    "Alemanha": "Berlim",
    "Canadá": "Ottawa",
    "Índia": "Nova Deli"
}

numero_de_itens = len(paises_capitais.items())

print(f"O número de itens no dicionário é: {numero_de_itens}")