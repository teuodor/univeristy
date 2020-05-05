'''
Created on 13 Feb 2019

@author: Teuodor
'''
def consistent(l):
    if l == []:
        return False
    nr = 0
    for i in l:
        if i == 1:
            nr += 1
    if nr<3:
        return True
    return False
def solution(l,n):
    if l[-1] != 'X':
        return True
    return False

def bcktRec(n,l=[]):
    if len(l) == n:
        if solution(l,n):
            return [l]
        else:
            return []
    else:
        sol = []
        for i in range(0,3):
            if i == 2:
                l = l +['X']
            else:
                l = l + [i+1]
            if consistent(l):
                sol = sol + bcktRec(n,l[:])
            
            l = l[:-1]
            
            
    return sol
l = bcktRec(4)
for i in l:
    print(i)                    
                    