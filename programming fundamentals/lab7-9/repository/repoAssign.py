'''
Created on 19 Nov 2018

@author: Teuodor
'''
class AssignRepositoryException(Exception):
    pass
class assignamentRepository:
    def __init__(self):
        self.assigs=[]
    def get_all_assign(self):
        '''
        Function that gets all the assignments from the list
        :return: a list of all assignaments
        '''
        return self.assigs
    def store(self,newassig):
        '''
        The function stores a new assignament
        :param: newassig
        :post: the new assignament will be added to the list
        '''
        if newassig in self.assigs:
            raise AssignRepositoryException("This person already goes to this event")
        self.list.append(newassig)
    def delete_person(self,id):
        '''
        A function that deletes all assignaments which have an person id
        :param id: the person id
        :post: the assignament will be deleted from the list and file 
        '''
        lun=len(self.assigs)
        index=0
        while index<lun:
            if self.assigs[index].get_person_id() == id:
                self.assigs.remove(self.assigs[index])
                index-=1
                lun-=1
            index+=1
    def delete_event(self,id):
        '''
        A function that deletes all assignaments which have an event id
        :param id: the event id
        :post: the assignament will be deleted from the list
        '''
        lun=len(self.__assigs)
        index=0
        while index<lun:
            if self.__assigs[index].get_event_id() == id:
                self.__assigs.remove(self.__assigs[index])
                index-=1
                lun-=1
            index+=1