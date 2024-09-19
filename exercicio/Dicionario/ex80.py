'''
Crie dois dicionários e combine-os em um único dicionário. Exiba o dicionário resultante
'''
dicionario1 = {
    "a": 1,
    "b": 2,
    "c": 3
}

dicionario2 = {
    "d": 4,
    "e": 5,
    "f": 6
}

dicionario_combinado = {**dicionario1, **dicionario2}

print("Dicionário combinado:")
print(dicionario_combinado)
