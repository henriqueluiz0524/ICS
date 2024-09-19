def verificar_palindromo(texto):
    # Remove espaços, pontuações e converte para minúsculas
    texto = texto.replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "")
    # Verifica se o texto é igual ao seu inverso
    return texto == texto[::-1]

# Solicita ao usuário que insira uma palavra ou frase
texto_usuario = input("Insira uma palavra ou frase: ")

# Verifica se é um palíndromo e exibe o resultado
if verificar_palindromo(texto_usuario):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")