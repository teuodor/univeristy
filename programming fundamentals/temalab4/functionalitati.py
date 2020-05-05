import math
from getset import getReal, getImag, createComplex
def formaComplex(a):
    '''
    Functia returneaza un numar complex in forma sa naturala
    in:a-complex
    pre:a-lista
    out:a'
    post:a-string-forma naturala a numarului complex
    '''
    c=getReal(a)
    d=getImag(a)
    if d>1:
        return str(c)+'+'+str(d)+'i'
    elif d<-1:
        return str(c)+str(d)+'i'
    elif d==1:
        return str(c)+'+i'
    elif d==-1:
        return str(c)+'-i'
    else:
        return str(c)+'+'+str(d)+'i'
def returnLista(lista):
    '''
    Funtia returneaza lista in forma ei naturala
    in:lista
    pre:lista-lista
    out:s
    post:s-string-lista in forma ei naturala
    '''
    s=''
    for k in range(len(lista)):
        s+=formaComplex(lista[k])+' '
    return s
def prim(a):
    '''
    Functia care verifica daca un numar este prim.
    in:a
    pre:a-intreg
    out:n
    post:n-boolean
    '''
    if(a<2):
        return False
    elif a==2:
        return True
    elif a%2==0:
        return False
    else:
        for k in range(3,int(math.sqrt(a))+1,2):
            if a%k==0:
                return False
    return True
            
def produs(complex1,complex2):
    '''
    Functia calculeaza partea reala si imaginara a unui produs dintre doua numere complexe
    in:complex1,complex2
    pre:complex1,complex2-lista/dictionar
    out:n,m
    post:n-real,m-real
    '''
    a=getReal(complex1)
    b=getImag(complex1)
    c=getReal(complex2)
    d=getImag(complex2)
    
    return [a*c-b*d,a*d+b*c]
    
def modul(complex):
    '''
    Functia calculeaza modulul uni numar complex
    in:complex
    pre:complex-lista/dictionar
    out: mod-radical din suma patratelor partii reale(real) si imaginare(imag)
    post: mod-real
    '''
    real=getReal(complex)
    imag=getImag(complex)
    real=real**2
    imag=imag**2
    mod=math.sqrt(real+imag)
    return mod

def adaugaLista(lista,elem):
    '''
    Functia adauga un element in lista
    in:lista,elem
    pre:lista-lista
    out:lista'-lista noua cu elementul adaugat
    '''
    lista.append(elem)

def inserareLista(lista,poz,elem):
    '''
    Functia insereaza un element pe o pozitie data
    in:lista,poz,elem
    pre:lista-lista,poz-natural
    output:lista'-lista noua cu elementul adaugat pe pozitia data
    '''
    lista.insert(poz,elem)

def stergePozitieLista(lista,poz):
    '''
    Functia sterge un element de pe o pozitie data
    in:lista,poz
    pre:lista-lista,poz-natural
    out:lista'-lista cu elementul scos de pe pozitia data
    '''
    del lista[poz]

def stergeIntervalLista(lista,poz1,poz2):
    '''
    Functia sterge un interval dintr-o lista  dintre doua pozitii date
    in:lista,poz1,poz2
    pre:lista-lista,poz1-natural,poz2-natural,poz1<=poz2
    out:lista'-lista cu elemetele scoase dintre cele doua pozitii
    '''
    del lista[poz1:poz2+1]

def inlocuiesteElementLista(lista,el1,el2):
    '''
    Functia inlocuieste valoarea unui element cu alta valoare data
    in:lista,el1,el2
    pre:lista-lista
    out:lista'-lista cu el1 inlocuit cu el2 in toata lista
    '''
    for k in range(len(lista)):
        if lista[k]==el1:
            lista[k]=el2
def sumaSubsecventa(lista,poz1,poz2):
    '''
    Functia calculeaza suma unei subsecvente dintr-o lista de numere complexe
    in:lista,poz1,poz2
    pre:lista-lista;poz1,poz2-naturale
    out:a
    post:a-lista/dictionar
    '''
    s1=0
    s2=0
    for k in range(poz1,poz2+1):
        s1+=getReal(lista[k])
        s2+=getImag(lista[k])
    a=createComplex(s1, s2)
    return a
def produsSubsecventa(lista,poz1,poz2):
    '''
    Functia calculeaza produsul unei subsecvente dintr-o lista de numere complexe
    in:lista,poz1,poz2
    pre:lista-lista;poz1,poz2-naturale
    out:a
    post:a-lista/dictionar,produsul subsecventei
    '''
    a=createComplex(1,0)
    for k in range(poz1,poz2+1):
        a=produs(a,lista[k])
    return a
def filtrareRealPrim(lista):
    '''
    Functia sterge elementele din lista care au partea reala prima
    in:lista
    pre:lista-lista
    out:lista'
    post:lista'-lista fara elementele care au partea reala prima
    '''
    for k in range(len(lista)-1,-1,-1):
        if prim(getReal(lista[k]))==True:
            del lista[k]
def modulMaiMic(lista,numar):
    '''
    Functia sterge elementele care au modulul mai mic decat un numar dat
    in:lista
    pre:lista-lista
    out:lista'
    post:lista'-lista noua cu elementele sterse
    '''
    for k in range(len(lista)-1,-1,-1):
        if modul(lista[k])<numar:
            del lista[k]
def modulEgal(lista,numar):
    '''
    Functia sterge elementele care au modulul egal cu un numar dat
    in:lista
    pre:lista-lista
    out:lista'
    post:lista'-lista noua cu elementele sterse
    '''
    for k in range(len(lista)-1,-1,-1):
        if modul(lista[k])==numar:
            del lista[k]
def modulMaiMare(lista,numar):
    '''
    Functia sterge elementele care au modulul mai mare decat un numar dat
    in:lista
    pre:lista-lista
    out:lista'
    post:lista'-lista noua cu elementele sterse
    '''
    for k in range(len(lista)-1,-1,-1):
        if modul(lista[k])>numar:
            del lista[k]
def grupare(lista):
    '''
    Functia grupeaza numerele complexe dupa modulul lor
    in:lista
    pre:lista-lista
    out:dict
    post:dict-dictionarul cu cheile modulele numerelor complexe
    '''
    dict={}
    lista2=[]
    for k in range(len(lista)):
        a=modul(lista[k])
        ok=True
        for k in range(len(lista2)):
            if a==lista2[k]:
                ok=False
                break
        if ok==True:
            lista2.append(a)
            dict.update({str(a):[]})
    for k in range(len(lista)):
        a=modul(lista[k])
        dict[str(a)].append(lista[k])
    return dict

