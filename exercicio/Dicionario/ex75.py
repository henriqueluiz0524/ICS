'''
 Itere sobre o dicionário de países e capitais e exiba cada 
 par chave-valor no formato "A capital de [país] é [capital]".
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

for pais, capital in paises_capitais.items():
    print(f"A capital de {pais} é {capital}.")