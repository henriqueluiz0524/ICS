# Solicita ao usuário que digite um número
numero = int(input("Digite um número: "))

# Mostra a tabuada do número de 1 a 10
print("Tabuada de", numero, ":")
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)