import math

def adaugaLista(v,a):
    v.append(a)
    pass

def inserareLista(v,poz,a):
    v.insert(poz,a)
    pass

def stergeElementLista(v,poz):
    del v[poz]
    pass

def stergeIntervalLista(v,poz1,poz2):
    del v[poz1:poz2+1]
    pass

def inlocuiesteElementLista(v,el1,el2):
    for k in range(len(v)):
        if v[k]==el1:
            v[k]=el2
    pass

def modul(a):
    c=a.real*a.real
    d=a.imag*a.imag
    return math.sqrt(c+d)

def afisareImaginar1(a):
    print(a.imag)
    pass

def tiparireElemente1(v):
    #Tipareste toate elementele din lista care au modulul mai mic ca 10
    s=[]
    for k in range(len(v)):
        if modul(v[k])<10:
            s.append(v[k])
    print(s)

def run():
    v=[complex(x) for x in input().split()]
    tiparireElemente1(v)
    print(v)
    pass
def run1():
    a=2+3j
    afisareImaginar(a)
    
run()



