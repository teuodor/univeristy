from meniu import *
from undo import copyLista
def run():
    lista=[]
    undol=[]
    while True:
        lista2=[]
        print('Va rugam sa scrieti o comanda. Daca aveti nevoie de ajutor tastati help')
        cmd=input('>>')
        meniu(cmd, lista,undol)
        if cmd.lower()=='exit':
            break
run()