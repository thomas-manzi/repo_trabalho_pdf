def soma_matrizes(m1,m2):
    b=len(m1)
    b1=len(m1[0])
    a=len(m2)
    a1=(len(m2[0]))
    c=[]
    if b1 == a1 and a == b :
        for i in range(len(m1)):
            c.append([])
            for j in range(len(m2[0])):
                c[i].append(m1[i][j]+m2[i][j])
        return c
    else:
        return False
    