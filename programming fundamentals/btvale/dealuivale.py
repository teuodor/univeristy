n = input("Numarul de elemente: ")
l= []
while True:
    try:
        n=int(n)
        break
    except:
        print("Numarul de elemente trebuie sa fie un numar natural. ")
print("Elementele vor fi:")
for i in range(n):
    x = input()
    l.append(x)
    
def afisare(l):
    for i in l:
        for j in range(0,len(i)):
            print(i[j],end=' ')
        print('\n')
def solutionFound(l,nr):
    x=[]
    for i in l:
        x.append(nr[i])
    return x
    
def solution(l,nr):
    if len(l) == len(nr):
        return True
    return False

def consistent(l,nr):
    if len(l)>len(nr):
        return False
    
    for i in range(0,len(l)-1):
        if l[-1]==l[i]:
            return False
    
    i=1
    while i<len(l) and nr[l[i-1]]>nr[l[i]]:
        i+=1
    
    if i==len(l):
        return True
    
    while i<len(l) and nr[l[i-1]]<nr[l[i]]:
        i+=1
        
    if i == len(l):
        return True
    
    return False
def bktRec(nr):
    l=[]
    x=[]
    def bkt(l,nr,x):
        l.append(-1)
        for i in range(0,len(nr)):
            l[-1]=i
            if consistent(l,nr):
                if solution(l,nr):
                    x.append(solutionFound(l,nr))
                else:
                    bkt(l[:],nr,x)
        return x
    a=bkt(l,nr,x)
    return x
    
def bktIter(nr):
    x=[]
    l=[-1]
    while len(l)>0:
        bool = False
        while bool == False and l[-1] < len(nr)-1:
            l[-1] += 1
            bool = consistent(l, nr)
        if bool:
            if solution(l, nr):
                x.append(solutionFound(l, nr))
            l.append(-1)
        else:
            l=l[:-1]
    return x


while True:
    cmd=input("Alegeti daca doriti recursiv sau iterativ(r/i)")
    
    if cmd == "i":
        x=bktIter(l)
        afisare(x)
        break
    elif cmd == "r":
        x=bktRec(l)
        afisare(x)
        break
    else:
        print("Va rugam tastati r sau i")
    