def arruma_matriz (coluna,linha,matriz):
    for i in range(linha):
        linha=[]
        for j in range(coluna):
            linha.append(j)
            
        #print(quebralinha)       
        matriz.append(linha)

    return matriz
m=[[1,2,3],[1,2,3],[1,2,3]]
print(arruma_matriz(3,3,m))