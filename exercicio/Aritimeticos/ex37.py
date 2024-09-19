ano = int(input("Digite um ano: "))

#or é um operador lógico utilizado para realizar operações de comparação entre expressões booleanas.

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(ano, "é um ano bissexto.")
else:
    print(ano, "não é um ano bissexto.")