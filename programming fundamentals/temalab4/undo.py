'''
Created on 6 Nov 2018

@author: Teuodor
'''
from getset import getReal,getImag
from getset import createComplex
def copyLista(l1):
    l2=[]
    for k in l1:
        a=createComplex(getReal(k),getImag(k))
        l2.append(a)
    return l2
def undoLista(lista,undol):
    lista=copyLista(undol[len(undol)-1])
    undol.pop()
    return lista