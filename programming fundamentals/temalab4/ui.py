from operator import itemgetter
from getset import getImag
from functionalitati import modul,grupare,returnLista,formaComplex
def afisareLista(lista):
    '''
    Functia afiseaza lista
    '''
    print(returnLista(lista))
def afisareImaginar(lista,poz1,poz2):
    '''
    Functia afiseaza toate partile imaginare ale elementelor din lista
    '''
    a=''
    for k in range(poz1,poz2+1):
        a+=str(int(getImag(lista[k])))+' '
    print(a)
def tiparireElemente1(lista):
    '''
    Tipareste toate elementele din lista care au modulul mai mic ca 10
    '''
    s=''
    for k in range(len(lista)):
        if modul(lista[k])<10:
            s+=formaComplex(lista[k])+' '
    print(s)

def tiparireElemente2(lista):
    '''
    Tipareste toate elementele din lista care au modulul egal cu 10
    '''
    s=''
    for k in range(len(lista)):
        if modul(lista[k])==10:
            s+=formaComplex(lista[k])+' '
    print(s)
def tiparireElementeDesc(lista):
    '''
    Tipareste elementele in ordine descrescatoare dupa partea lor imaginara
    '''
    lista2=sorted(lista,key=itemgetter(1),reverse=True)
    afisareLista(lista2)

def tiparireGrupare(lista):
    '''
    Functia afiseaza gruparea elementelor dupa module
    '''
    dict=grupare(lista)
    for key in dict.keys():
        print(key+': '+returnLista(dict[key]))