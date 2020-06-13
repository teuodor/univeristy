'''
Created on 13 Feb 2019

@author: Teuodor
'''
def modul(n):
    if n<0:
        return -1*n
    return n
def solutie(l,n):
    if len(l) == n:
        return True
    return False
def consistent(l,n):
    if len(l) == 1:
        return True
    i = 0
    for i in range(1,len(l)):
        for j in range(0,i):
            if modul(l[i]-l[j])==1:
                return True
    return False
def bckt(n):
    def rec(n,l = []):
        if solutie(l,n):
            return [l]
        else:
            sol = []
            for i in range(1,n+1):
                l = l + [i]
                if consistent(l, n):
                    sol += rec(n,l[:])
                l = l[:-1]
            
        return sol
    return rec(n)


print(bckt(3))