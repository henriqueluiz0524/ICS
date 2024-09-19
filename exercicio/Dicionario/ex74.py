'''
Remova um dos países do dicionário criado e exiba o dicionário atualizado.
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

paises_capitais.pop("França")

print(paises_capitais)