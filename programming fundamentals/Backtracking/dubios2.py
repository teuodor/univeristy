'''
Created on 19 Feb 2019

@author: Teuodor
'''
def consistent(maxim,nr):
    p = -1
    for i in range(len(nr)):
        if nr[i] == maxim:
            p = i
            
    if p == -1:
        for i in range(len(nr)-1):
            if nr[i] <= nr[i+1]:
                return False
            
    else:
        for i in range(0,p-1):
            if nr[i] <= nr[i+1]:
                return False
        
        for i in range(p+1,len(nr)-1):
            if nr[i] >= nr[i+1]:
                return False
            
    return True
             
        
    
def solution(nr,l):
    if len(nr) == len(l):
        return True
    return False
def bckt(l):
    maxim = max(l)
    viz = [False] * len(l)
    def rec(l,maxim,viz,nr = []):
        if solution(nr,l):
            return [nr]
        else:
            sol = []
            for i in range(len(l)):
                if viz[i] == False:
                    nr.append(l[i])
                    viz[i] = True
                    if consistent(maxim,nr):#
                        sol = sol + rec(l,maxim, nr[:])
                
                    nr = nr[:-1]
                    viz[i] = False

        return sol
    
    return rec(l,maxim,viz)

print(bckt([1,2,5,3,7]))        