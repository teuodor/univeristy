import math
from getset import *
from functionalitati import *
from undo import *
def testGetSet():
    a=createComplex(1, 2)
    b=getReal(a)
    c=getImag(a)
    assert b==1
    assert c==2
    setReal(a, 3)
    setImag(a, 3)
    b=getReal(a)
    c=getImag(a)
    assert b==3
    assert c==3
def testFunctionalitati():
    a=[3,4]
    b=createComplex(1, 1)
    assert modul(b)==math.sqrt(2)
    b=createComplex(3, 4)
    assert modul(b)==5
    adaugaLista(a, 3)
    assert a==[3,4,3]
    inserareLista(a, 1, 2)
    assert a==[3,2,4,3]
    stergePozitieLista(a, 1)
    assert a==[3,4,3]
    stergeIntervalLista(a, 0,2)
    assert a==[]
    a=[3,3,3]
    inlocuiesteElementLista(a,3,2)
    assert a==[2,2,2]
    a=createComplex(1,1)
    b=createComplex(1,-1)
    assert produs(a, b)==createComplex(2, 0)
    v=[]
    adaugaLista(v, a)
    adaugaLista(v, b)
    adaugaLista(v, createComplex(1, 2))
    adaugaLista(v, createComplex(3, 4))
    adaugaLista(v, createComplex(2, 6))
    assert sumaSubsecventa(v, 1, 3)==createComplex(5,5)
    assert produsSubsecventa(v, 0, 2)==createComplex(2, 4)
    assert prim(3)==True
    assert prim(2)==True
    assert prim(25)==False
    assert prim(1)==False
    assert prim(0)==False
    assert prim(8)==False
    assert prim(-2)==False
    lista=[]
    a=createComplex(1, 2)
    assert formaComplex(a)=='1+2i'
    adaugaLista(lista, a)
    adaugaLista(lista, a)
    assert returnLista(lista)=='1+2i 1+2i '
    a=createComplex(-3,4)
    assert produsSubsecventa(lista,0,1)==a
    a=createComplex(2,4)
    assert sumaSubsecventa(lista,0,1)==a
    lista2=lista
    filtrareRealPrim(lista)
    assert lista==lista2
    modulEgal(lista, math.sqrt(5))
    lista2=[]
    assert lista==lista2
    adaugaLista(lista, createComplex(1, 2))
    adaugaLista(lista, createComplex(2, 3))
    adaugaLista(lista, createComplex(2, 3))
    adaugaLista(lista, createComplex(5, 6))
    adaugaLista(lista, createComplex(7, 8))
    modulMaiMare(lista, math.sqrt(5))
    adaugaLista(lista2, createComplex(1,2))
    assert lista==lista2
    lista2=[]
    modulMaiMic(lista, 3)
    assert lista==lista2
    
def testUndo():
    lista=[]
    undol=[]
    a=createComplex(1, 2)
    adaugaLista(lista, a)
    undol.append(copyLista(lista))
    adaugaLista(lista, a)
    lista=undoLista(lista, undol)
    assert undol==[]
    assert lista==[[1,2]]
testGetSet()
testFunctionalitati()
testUndo()