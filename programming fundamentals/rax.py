def prim(x):
    if x<2:
        return False
    for d in range (2,int(x**0.5)+1):
        if x%d==0:
            return False
    return True

def main():
    x=1
    while x!=-1:
        x=int(input("Numarul:"))
        while(x>2):
            x-=1
            if prim(x):
                print(x)
                break
        if x<=2:
            print("Nu merge")
            
main()
