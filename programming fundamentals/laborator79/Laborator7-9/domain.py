'''
Created on 9 Nov 2018

@author: Teuodor
'''
class Persons:
    def __init__(self,idPerson,Name,Adress):
        self.__id=idPerson
        self.__name=Name
        self.__adress=Adress
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_adress(self):
        return self.__adress
    def set_id(self,newId):
        self.__id=newId
    def set_name(self,newName):
        self.___name=newName
    def set_adress(self,newAdress):
        self.__adress=newAdress
    def __eq__(self,other):
        return self.__id==other.__id
class Events:
    def __init__(self,Id,Date,Time,Description):
        self.__id=Id
        self.__date=Date
        self.__time=Time
        self.__desc=Description
    def get_id(self):
        return self.__id
    def get_date(self):
        return self.__date
    def get_time(self):
        return self.__time
    def get_desc(self):
        return self.__desc
    def set_id(self,newId):
        self.__id=newId
    def set_date(self,newDate):
        self.__date=newDate
    def set_time(self,newTime):
        self.__time=newTime
    def set_desc(self,newDesc):
        self.__desc=newDesc
