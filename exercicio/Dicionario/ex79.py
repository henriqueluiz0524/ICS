'''
 Escreva um programa que atualize a capital de um país no dicionário de países e capitais.

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

def atualizar_capital(pais, nova_capital):
    if pais in paises_capitais:
        paises_capitais[pais] = nova_capital
        print(f"A capital de {pais} foi atualizada para {nova_capital}.")
    else:
        print(f"O país {pais} não está presente no dicionário.")

pais = input("Digite o nome do país que você deseja atualizar a capital: ")
nova_capital = input(f"Digite a nova capital para {pais}: ")

atualizar_capital(pais, nova_capital)

print("Dicionário de países e capitais atualizado:")
print(paises_capitais)