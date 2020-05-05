'''
Created on 13 Nov 2018

@author: Teuodor
'''
import time
class Validare(Exception):
    pass
class ValidarePersons:
    def validare(self,person):
        exceptions=[]
        nume=person.get_name()
        if person.get_id()=="":
            exceptions.append("Id can't be empty ")
        if person.get_name()=="":
            exceptions.append("Name can't be empty ")
        elif nume[0]<'A' or nume[0]>'Z':
            exceptions.append("The first letter of the name must be big ")
        if person.get_adr()=="":
            exceptions.append("Adress can't be empty ")
        
        
        if len(exceptions)>0:
            raise Validare("".join(str(x) for x in exceptions))
class ValidareEvents:
    def validare(self,event):
        exceptions=[]
        if event.get_id() == "":
            exceptions.append("Id can't be empty ")
        if event.get_date() == "":
            exceptions.append("Date can't be empty ")
        if event.get_time() == "":
            exceptions.append("Time can't be empty ")
        if event.get_desc() == "":
            exceptions.append("Description can't be empty ")
        try:
            t = time.strptime(event.get_time(),'%H:%M')
        except:
            exceptions.append("Time must be HH:MM format ")
        if len(exceptions)>0:
            raise Validare("".join(str(x) for x in exceptions))
