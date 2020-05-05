n=1
while n!=0:
    n=input('Introduceti valori pana la 0: ')
    n=int(n)
    n1=n
    k=0
    while n1>0:
        k=k*10+n1%10
        n1=n1//10
    print(k)
