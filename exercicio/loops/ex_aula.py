elementos_que_terminam_com_H = ['Pirapora', 'Montes Claros', 'BH']

def seleciona_elemento_com_a_letra_H(elemento_com_H):
    lista_auxiliar = []
    for palavra in elemento_com_H:
        if palavra[-1] == 'H':
            lista_auxiliar.append(palavra)
    print(lista_auxiliar)
                
seleciona_elemento_com_a_letra_H(elementos_que_terminam_com_H)
