'''
Created on 10 Nov 2018

@author: Teuodor
'''
from domain import *
class Validare:
    def __init__(self,exceptions):
        self.errors=exceptions
    def get_errors(self):
        return self.__errors
class ValidarePersons:
    def validare(person):
        exceptions=[]
        if person.get_id()=="":
            exceptions.append("Id can't be empty")
        if person.get_name()=="":
            exceptions.append("Name can't be empty")
        if person.get_adress()=="":
            exeptions.append("Adress can't be empty")
        if len(exceptions)>0:
            raise Validare(exceptions)
class ValidareEvents:
    def validare(event):
        exceptions=[]
        if event.get_id()=="":
            exceptions.append("Id can't be empty")
        if event.get_date()=="":
            exceptions.append("Date can't be empty")
        if event.get_time()=="":
            exceptions.append("Time can't be empty")
        if event.get_desc()=="":
            exceptions.append("Description can't be empty")
        if len(exceptions)>0:
            raise Validare(exceptions)
