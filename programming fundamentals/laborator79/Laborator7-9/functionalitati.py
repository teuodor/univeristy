
'''
Created on 9 Nov 2018

@author: Teuodor
'''
from domain import *
def adaugaLista(lista,elem):
    lista.append(elem)
    
def stergeLista(lista,elem):
    del lista[elem.__id]

def modifyLista(lista,elem1,elem2):
    if elem1 in lista:
        elem2=elem1



    
