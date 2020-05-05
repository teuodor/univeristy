'''
Created on 12 Dec 2018

@author: Teuodor
'''
class Phone:
    '''
    The Phone class which have an id, a name, some characteristics and a price
    '''
    def __init__(self,id,name,char,price): 
        '''
        :param id:
        :param name:
        :param char:
        :param price:
        '''
        self.__id = id
        self.__name = name
        self.__char = char
        self.__price = price
        
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_char(self):
        return self.__char
    
    def get_price(self):
        return self.__price
    
    def set_id(self, id):
        self.__id = id
    
    def set_name(self, name):
        self.__name = name
        
    def set_char(self, char):
        self.__char = char
        
    def set_price(self, price):
        self.__price = price
    
    def __eq__(self, other):
        return self.__id == other.__id
    
    def __lt__(self,other):
        if self.__name<other.__name:
            return True
        return False
    