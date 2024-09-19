dias_da_semana = ["Domingo","Segunda","Terça","Quarta","Quinta", "Sexta", "Sabado"]

def seleciona_dias_da_semana_que_têm_a_letra_S(Dias_com_S):
    Lista_auxiliar = []
    for dias in Dias_com_S:
        if "S" in dias:
            Lista_auxiliar.append(dias)
    return Lista_auxiliar

dias_da_semana_que_contêm_a_letra_S = seleciona_dias_da_semana_que_têm_a_letra_S(dias_da_semana)
print(dias_da_semana_que_contêm_a_letra_S)