def menor_nome(lista):
    a=""
    menor=""
    for i in range(len(lista)):
        if i==0:
            menor=lista[i].strip()
            a=menor.count("")
        elif(a>lista[i].count("")):
            menor=lista[i].strip()
            a=menor.count("")
    return menor.capitalize()

l=['maria', ' josé ', '   PAULO', 'Catarina   ']
print(menor_nome(l))