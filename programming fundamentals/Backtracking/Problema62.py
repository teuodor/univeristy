'''
Created on 16 Feb 2019

@author: Teuodor
'''


def solutionFound(poz,list):
    l = []
    for i in poz:
        l.append(list[i])
    return l

def consistent(poz,list):
    if len(poz) >= 2:
        if list[poz[-1]] <= list[poz[-2]]:
            return False
        
    return True

def solution(poz,list,n):
    suma = 0
    for i in poz:
        suma += list[i]
    
    if suma%n == 0:
        return True
    return False

def bckt(list,n):
    poz = []
    sol = []
    def rec(poz,list,n,sol):
        poz.append(-1)
        for i in range(0,len(list)):
            poz[-1] = i
            if consistent(poz,list):
                if solution(poz, list, n):
                    sol.append(solutionFound(poz, list))
                rec(poz[:], list, n, sol)
                    
        poz.pop()
                    
        return sol  
      
    return rec(poz,list,n,sol)

print(bckt([1,2,3,4], 2))
        