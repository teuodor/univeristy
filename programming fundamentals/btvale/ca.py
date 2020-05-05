'''
Created on 3 Feb 2019

@author: Teuodor
'''
def prime(x):
    if x==0 or x==1:
        return False
    if x==2:
        return True
    if x%2==0:
        return False
    d=3
    while d*d<=x:
        if x%d == 0:
            return False
        d+=2
    return True
def div_imp_prime(list):
    if len(list) == 1:
        if(prime(list[0])):
            return 1
        else:
            return 0
    else:
        m = len(list)//2
        return div_imp_prime(list[:m])+div_imp_prime(list[m:])
    
print(div_imp_prime([2,3,4,5,6,7,8,9,20]))