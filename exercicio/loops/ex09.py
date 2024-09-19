# Lista de entrada
entrada = ["Olá", "mundo", "Python", "!"]

# Função para concatenar todos os elementos em uma única string
def concatenar_elementos(lista):
    # Inicializa uma string vazia para armazenar a concatenação
    resultado = ""
    
    # Itera sobre cada elemento na lista de entrada
    for elemento in lista:
        # Concatena o elemento atual à string resultado
        resultado += elemento
    
    # Retorna a string resultante
    return resultado

# Chama a função passando a lista de entrada como argumento e armazena o resultado em uma variável
saida = concatenar_elementos(entrada)

# Imprime a string resultante
print(saida)
