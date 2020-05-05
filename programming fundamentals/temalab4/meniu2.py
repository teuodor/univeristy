'''
Created on 8 Nov 2018

@author: Teuodor
'''
from functionalitati import adaugaLista, filtrareRealPrim
from getset import createComplex
from ui import tiparireGrupare, afisareImaginar,tiparireElementeDesc
def meniu2(cmd,lista):
    for k in range(len(cmd)):
        if cmd[k]=='a':
            try:
                a=int(cmd[k+1])
                b=int(cmd[k+2])
                adaugaLista(lista,createComplex(a,b) )
                k=k+2
            except:
                print('Nu s-a putut adauga elementul deoarece nu ati pus numere')
        elif cmd[k]=='realprim':
            filtrareRealPrim(lista)
        elif cmd[k].lower()=='grupare':
            tiparireGrupare(lista)
        elif cmd[k].lower()=='afisimag':
            try:
                poz1=int(cmd[k+1])
                poz2=int(cmd[k+2])
                afisareImaginar(lista, poz1, poz2)
                k=k+2
            except:
                print('Nu se pot afisa deoarece nu ati ales pozitii numere')
        elif cmd[k].lower()=='afisdesc':
            tiparireElementeDesc(lista) 
        elif cmd[k].lower()=='exit':
            print('La revedere')
            break