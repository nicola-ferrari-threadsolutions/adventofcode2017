def giornoUno(stringa):
    listaNumeri=[]
    contatore=0
    for num in stringa:
        if(num==stringa[contatore-1]):
            listaNumeri.append(int(num))
        contatore=contatore+1
    return sum(listaNumeri)
    
    
def giornoDue(spreedSheet):
    '''
    spreedSheet è una struttura  "lista di liste".
    Ogni elemento (riga) contiene una lista di numeri(contenuto della riga)
    esempio:
    5 1 9 5
    7 5 3
    2 4 6 8
    
    verrebbe rappresentato dalla seguente struttura
    
    lista=[[5,1,9,5]]
    lista.append([7,5,3])
    lista.append([2,4,6,8])
    '''
    listaSomme=[]
    for riga in spreedSheet:
            listaSomme.append(max(riga)-min(riga))
    return sum(listaSomme)

def main():
    giornoUno("1122")
    lista=[[5,1,9,5]]
    lista.append([7,5,3])
    lista.append([2,4,6,8])
    giornoDue(lista)    
        
        
if __name__ == "__main__":
    main()
