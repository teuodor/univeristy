'''
Created on 3 Feb 2019

@author: Teuodor
'''
def abs(x):
    if x<0:
        return -x
    return x
def consistent(l):
    i=1
    while i<len(l) and (abs(l[i]-l[i-1]) == 1 or abs(l[i]-l[i-1]) == 2):
        i=i+1
    if i == len(l):
        return True
    return False
def solution(l):
    if l[0] == 0 and l[len(l)-1] == 0:
        return True
    return False
def bcktRec(l,n):
    if len(l) == 2*n+1:
        if solution(l):
            return [l]
        else:
            return []
    else:
        sol = []
        for i in range(0,3):
            l = l +[i-1]
            if consistent(l):
                sol = sol + bcktRec(l[:], n)
            
            l=l[:-1]
            
        return sol

      
print(bcktRec([],2))       