'''

'''

lista_palavras = [
    "gato", "cachorro", "gato", "elefante", "cachorro", 
    "gato", "cachorro", "pássaro", "gato", "gato"
]

contagem_palavras = {}

for palavra in lista_palavras:
    if palavra in contagem_palavras:

        contagem_palavras[palavra] += 1
    else:

        contagem_palavras[palavra] = 1

print("Contagem de palavras:")
print(contagem_palavras)
