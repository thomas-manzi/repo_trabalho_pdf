def maiusculas(frase):
    resposta=""
    for i in frase:
        if i != "" :
            if ord(i)>=65 and ord(i)<=90 :
                resposta += i
    return resposta


