def bubble_sort(lista):
    final= len(lista)

    for i in range(final-1,0,-1): #for inverso
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j] #troca em python
                print(lista)
    return lista

