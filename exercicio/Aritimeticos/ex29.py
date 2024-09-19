num1 = input("Digite o primeiro numero: ")
num2 = input("Digite o segundo numero: ")

operacao = input("Digite qual operacao vc deseja: (+ - * /) ")

if operacao == '+':
    soma = int(num1) + int(num2)
    print(soma)

elif operacao == '-':
    subtracao = int(num1) - int(num2)
    print(subtracao)

elif operacao == '*':
    multiplicacao = int(num1) * int(num2)
    print(multiplicacao)

else:
    operacao == '/'
    divisao = int(num1) / int(num2)
    print(divisao)



