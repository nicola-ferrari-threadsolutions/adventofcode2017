def giornoUno(stringa):
    listaNumeri=[]
    for contatore,  num in enumerate(stringa):
        if(num==stringa[contatore-1]):
            listaNumeri.append(int(num))
    return sum(listaNumeri)

def giornoUno_Due(stringa):
    listaNumeri=[int(num )for num in stringa]
    halfSize=int(len(listaNumeri)/2)
    listaUno=listaNumeri[:halfSize]
    listaDue=listaNumeri[halfSize:]
    listaNumeri=[]
    for index,  val in enumerate(listaUno):
        if(val==listaDue[index]):
            listaNumeri.append(val*2)
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

def giornoDue_Due(spreedSheet):
    listaSomme=[]
    for riga in spreedSheet:
            riga.sort(reverse=True)
            for index,  val in enumerate(riga):
                for valDue in riga[index+1:]:
                    if(val%valDue==0):
                        listaSomme.append(val/valDue)
    return sum(listaSomme)
    
    
def giornoTre():
    # usato script/logica Dede
    input=312051
    return 430

def giornoQuattro(pathFile):
    fileGiorno4=open("%s" %pathFile, "r") 
    contatore=0
    listaRiga=[]
    fileGiorno4=open("%s" %pathFile, "r") 
    for line in fileGiorno4: 
        listaRiga=list(line.rstrip().split(" "))
        if(len(list(listaRiga))==len(list(set(listaRiga)))):
            contatore=contatore+1
       # listaParole.extend(line.rstrip().split(" "))
    return contatore    
   
def giornoQuattro_Due(pathFile):
    contatore=0
    fileGiorno4=open("%s" %pathFile, "r") 
    for line in fileGiorno4: 
        listaRiga=list(line.rstrip().split(" "))
        valid=True
        for index in range(0,  len(listaRiga)-1):
            val=''.join(sorted(listaRiga[index]))
            i=index+1
            while i<len(listaRiga):
                valDue=listaRiga[i]
                print (val,  valDue,  ''.join(sorted(valDue)))
                if (val==valDue or val== ''.join(sorted(valDue))):
                    valid=False
                    break
                i+=1
        if valid==True:
            contatore+=1
    return contatore
    
def giornoCinque(pathFile):
    #carico il file in una lista
    fileGiorno5=open("%s" %pathFile, "r") 
    lst=[]
    for line in fileGiorno5: 
        lst.append(int(line.rstrip()))
    # lista pronta
    print ("inizio")   
    pos=0
    nMov=0
    while pos<len(lst):
        valoreAttuale=lst[pos]
        lst[pos]+=1
        pos+=valoreAttuale
        nMov+=1
    print ("fine") 
    return nMov
  
  
def main():
    giornoUno("1122")
    lista=[[5,1,9,5]]
    lista.append([7,5,3])
    lista.append([2,4,6,8])
    giornoDue(lista)    
    giornoCinque("/home/nicola/Studio/adventofcode2017/testoGiorno5.txt")
    
        
if __name__ == "__main__":
    main()
