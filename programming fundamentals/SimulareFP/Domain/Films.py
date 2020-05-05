'''
Created on 13 Dec 2018

@author: Teuodor
'''
class Films:
    def __init__(self,id,title,price,number):
        self.__id=id
        self.__title=title
        self.__price=price
        self.__nr=number
    
    def get_id(self):
        return self.__id
    
    def get_title(self):
        return self.__title
    
    def get_price(self):
        return self.__price
    
    def get_nr(self):
        return self.__nr
    
    def set_id(self, id1):
        self.__id = id1
        
    def set_title(self, title):
        self.__title = title
        
    def set_price(self, price):
        self.__price = price
        
    def set_nr(self, nr):
        self.__nr = nr