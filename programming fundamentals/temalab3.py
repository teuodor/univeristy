def print_list(a,b,c):
    s=''
    for x in range(b,b+c):
        s+=str(a[x])+' '
    print(s)
    pass



def cmmdc(a,b):
    '''
    Functie recursiva de calculare a cmmdc-ului dintre doua numere
    input: a,b
    preconditii: a-intreg
                 b-intreg
    output: a'
    postconditii: a'-cmmdc dintre a si b
    '''
    if a==b:
        return a
    elif a>b:
        return cmmdc(a-b,b)
    else:
        return cmmdc(a,b-a)
    pass

def test_cmmdc():
    assert cmmdc(2,2)==2
    assert cmmdc(4,2)==2
    assert cmmdc(1,7)==1
    assert cmmdc(30,100)==10
    assert cmmdc(8,10)==2
    pass

def citire(v,n):
    v.clear()
    n=input('Numarul de elemente al listei: ')
    try:
        n=int(n)
        n=str(n)
        print('Lista dumneavoastra de '+n+' elemente: ')
        n=int(n)
        for k in range(n):
            x=input()
            try:
                x=int(x)
                v.append(x)
            except:
                print('Se va relua de la alegerea primului numar. Va rugam alegeti doar numere!')
                ok1=False
                break
    except:
        print('Elementul introdus trebuie sa fie numar')
    return n

#Oricare doua elemente consecutive sunt relativ prime intre ele
#a, b relativ prime daca si numai daca cmmdc(a,b) = 1).
def ok2(v,n,poz1,lmax1):
    lmax1=-1
    l=1
    for k in range(n-1):
        if cmmdc(v[k],v[k+1])==1:
            l=l+1
            if lmax1<l:
                lmax1=l
                poz=k-lmax1+1
        else:
            l=1
    return poz1,lmax1




#suma elementelor este egal cu 5
def ok3(v,n,poz1,lmax1):
    lmax1=-1
    i=0
    while i<n :
        s=0
        l=0
        for k in range(i,n):
            s=s+v[k]
            l=l+1
            if s==5:
                if l>lmax1:
                    lmax1=l
                    poz1=k-lmax1+1
            if s>5:
                break
        i=i+1
    
    return poz1,lmax1

def ok4(v,n,poz1,lmax1):
    lmax1=-1
    l=1
    for k in range(n-1):
        if v[k]==v[k+1]:
            l=l+1
            if lmax1<l:
                lmax1=l
                poz1=k-lmax1+1
        else:
            l=1
    return poz1,lmax1
            
test_cmmdc()
print('1. Citire date;')
print('2. Cea mai lunga secventa in care oricare 2 elemente consecutive sunt prime intre ele;')
print('3. Cea mai lunga secventa in care suma elementelor este egala cu 5;')
print('4. Cea mai lunga secventa in care elementele sunt egale')
print('x. Exit')
ok=1
ok1=False
v=[]
n=0
poz=0
lmax=0
ok1=False
while ok!='x':
    ok=input('Alegeti un numar:')
    if ok=='x':
        print('La revedere')
        break
    try:
        ok=int(ok)
    except:
        print('Elementul introdus trebuie sa fie numar sau x!')
    if ok==1:
      n=citire(v,n)
      ok1=True
    if ok!=1 and ok1==True :
        if ok==2:
            poz,lmax=ok2(v,n,poz,lmax)
            if lmax!=-1:
                lmax=str(lmax)
                print('Secventa de lungime maxima are '+lmax+' elemente')
                lmax=int(lmax)
                print_list(v,poz,lmax)
            else:
                print('Nu s-a gasit o secventa care sa satisfaca conditia')
        elif ok==3:
            poz,lmax=ok3(v,n,poz,lmax)
            if lmax!=-1:
                lmax=str(lmax)
                print('Secventa de lungime maxima are '+lmax+' elemente')
                lmax=int(lmax)
                print_list(v,poz,lmax)
            else:
                print('Nu s-a gasit o secventa care sa satisfaca conditia')
        elif ok==4:
            poz,lmax=ok4(v,n,poz,lmax)
            if lmax!=-1:
                lmax=str(lmax)
                print('Secventa de lungime maxima are '+lmax+' elemente')
                lmax=int(lmax)
                print_list(v,poz+1,lmax)
            else:
                print('Nu s-a gasit o secventa care sa satisfaca conditia')   
    if ok1==False:
        print('Alege 1 inainte de toate')
        
            
