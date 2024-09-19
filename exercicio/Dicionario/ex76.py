'''
 Escreva um programa que verifique se um determinado país está presente no dicionário.
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

pais = input("Qual o pais? ")

if pais in paises_capitais:
    capital = paises_capitais[pais]
    
    print(f"O {pais} esta presente na lista.")

else:
    print("Desculpe, não temos esse pais.")