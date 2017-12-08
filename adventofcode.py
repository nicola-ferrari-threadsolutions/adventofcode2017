def giornoUno(stringa):
    listaNumeri=[]
    contatore=0
    for num in stringa:
        if(num==stringa[contatore-1]):
            listaNumeri.append(int(num))
        contatore=contatore+1
    return sum(listaNumeri)
    
