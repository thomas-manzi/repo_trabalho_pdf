def ordenada(lista):
    for i in range(len(lista)-1):
        pos_min=i
        for j in range(i+1,len(lista)):
            if lista[j] < lista[pos_min]:
                #fazer a troca
                return False        
    return True



