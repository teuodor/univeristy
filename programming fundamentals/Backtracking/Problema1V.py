def consistent(l,s):
    suma = 0
    for i in l:
        suma += i
    if suma<=s:
        return True
    return False
def solution(l,s):
    suma = 0
    for i in l:
        suma += i
    if suma == s:
        return True
    return False

def bckt(l,s):
    def rec(l, s, x = []):
        if solution(x,s):
            return [x]
        else:
            sol = []
            x.append(-1)
            for i in l:
                x[-1] = i
                if consistent(x, s):
                    sol += rec(l,s,x[:])
                
            x = x[:-1]
                
            return sol
    return rec(l, s)
            
    

print(bckt([1,5,10,50],40))
     