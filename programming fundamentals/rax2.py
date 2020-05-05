#1. Gasiti primul numar prim mai mare decat un numar dat.

# Urmatoarea functie verifica daca un numar 'n' este prim sau nu.
def prim(n):
    
    if n<2  :
        return False
    
    for i in range(2, int(n**0.5)+1 ):
        if n%i==0:
            return False

    return True
    

# Urmatoarea functie determina cel mai mic numar prim mai mare decat 'x'

def urm_prim (x):
    
    if x<2 :
       print(2)
       return
    
    if prim(x)==True :
        x=x+1
    
    while prim(x)==False :
        x=x+1
    
    return x

# Functia principala
    
def main () :
    x=1
    while(x!=-13):
       x=float(input("Numar :"))
       x=int(x)
       print(urm_prim(x))
   
main()
