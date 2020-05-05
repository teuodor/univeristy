'''
Created on 12 Dec 2018

@author: Teuodor
'''
from Domain.Telefoane import Phone
class RepositoryPhone:
    def __init__(self):
        self.__repo = self.__loadFromFile
    
    def __loadFromFile(self):
        try:
            f = open("phone.txt", 'r')
        except IOError:
            print("The file doesn't exist")
            return {}
        line = f.readline().strip()
        content = {}
        while line != "":
            attr = line.split(',')
            phone = Phone(attr[0],attr[1],attr[2],attr[3])
            content[phone.get_id()] = phone
            
        