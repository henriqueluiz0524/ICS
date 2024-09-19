'''
 Usando o dicionário criado no exercício anterior,
 escreva um programa que pergunte ao usuário o nome 
 de um país e exiba a capital correspondente.
'''

paises_capitais = {
    "Brasil": "Brasília",
    "Estados Unidos": "Washington D.C.",
    "França": "Paris",
    "Japão": "Tóquio",
    "Austrália": "Camberra"
}

pais = input("Qual o pais que você deseja saber a capital? ")

if pais in paises_capitais:
    capital = paises_capitais[pais]

    print(f"A capital de {pais} é {capital}.") 
else:

    print("Desculpe, não temos essa capital.")