'''
Created on 29 Nov 2018

@author: Teuodor
'''
'''
Created on 29 Nov 2018

@author: Teuodor
'''
class NameNrEventHour:
    def __init__(self,name,number_events,hour):
        self.__name=name
        self.__nr_ev=number_events
        self.__hour=hour
    def get_name(self):
        return self.__name
    def get_nr(self):
        return self.__nr_ev
    def get_hour(self):
        return self.__hour
    def set_name(self,name1):
        self.__name=name1
    def set_nr(self,nr1):
        self.__nr_ev=nr1
    def set_hour(self,hour1):
        self.__hour=hour1
        