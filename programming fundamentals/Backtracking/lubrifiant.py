'''
Created on 20 Feb 2019

@author: Teuodor
'''
class myint():
    def __init__(self,n):
        self.__n = n
        
    def __add__(self,nr):
        self.__n += nr
        return self.__n
    def get(self):
        return self.__n
    
def increm(i):
    i = i + 1
    
a = myint(1)
increm(a)
print(a.get())