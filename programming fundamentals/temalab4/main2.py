'''
Created on 8 Nov 2018

@author: Teuodor
'''
from meniu2 import meniu2
def run():
    lista=[]
    ok=False
    while ok!=True:
        cmd=input('Scrieti lista de comenzi: ')
        cmd=cmd.strip()
        cmd=cmd.split()
        meniu2(cmd,lista)
        for k in cmd:
            if k=='exit':
                ok=True
                break
                
            
run()