def cifra(a,b):
    l = [0]*10
    while a != 0:
        l[a%10] = 1
        a = a//10
    while b != 0:
        if l[b%10] != 0 :
            return True
        b = b//10
    return False       
def consistent(l):
    for i in range(1,len(l)):
        if l[i-1]>=l[i]:
            return False
        
    return True
def solution(l):
    for i in range(1,len(l)):
        if cifra(l[i-1], l[i]) == False:
            return False
    
    return True

def bckt(x,l=[]):
    if len(l) >= 2:
        if solution(l):
            return [l]
        else:
            return []
    else:
        sol =[]
        for i in x:
            l = l + [i]
            if consistent(l):
                sol = sol + bckt(x, l[:])
            
            l=l[:-1]
        
    return sol
    
print(bckt([1234,2334,2897,3333]))