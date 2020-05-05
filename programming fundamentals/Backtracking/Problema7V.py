'''
Created on 15 Feb 2019

@author: Teuodor
'''
def consistent(l):
    nr1 = 0
    nr2 = 0
    
    for i in l:
        if i == '(':
            nr1 = nr1 + 1
        if i == ')':
            nr2 = nr2 + 1
        
    if nr1 < nr2:
        return False
    
    return True
def solutie(l,n):
    
    nr1 = 0
    nr2 = 0
    for i in l:
        if i == '(':
            nr1 += 1
        if i == ')':
            nr2 += 1
    
    if nr1 == nr2:
            return True
        
    return False
    

def bckt(n,l=[]):
    if len(l) == n:
        if solutie(l,n):
            return [l]
        else:
            return []
    else:
        sol = []
        for i in range(0,2):
            if i == 0:
                l = l + ['(']
            if i == 1:
                l = l + [')']
            if consistent(l):
                sol = sol + bckt(n, l[:])
                
            l = l[:-1]

    return sol
            
l = bckt(4)
for i in l:
    x = "".join([y for y in i])
    print(x)
            