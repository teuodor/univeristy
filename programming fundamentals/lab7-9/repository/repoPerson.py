'''
Created on 19 Nov 2018

@author: Teuodor
'''
class PersonRepositoryException(Exception):
    pass
class personRepository:
    def __init__(self):
        self.persons = {}
        
    def get_persons(self):
        return self.persons.values()
    
    def store(self,pers):
        '''
        The function add a person to the repo
        :param: pers
        :post: the person is added to the list of persons
        '''
        if pers.get_id() in self.persons.keys():
            raise PersonRepositoryException("A person with this id exist")
        self.persons[pers.get_id()] = pers
    def delete(self, id):
        '''
        The function deletes a person from the repo 
        :param: id
        :post: the person will be deleted from the list
        '''
        keys=self.persons.keys()
        if not id in keys:
            raise PersonRepositoryException("We can't find the person")
        del self.persons[id]
    def modify(self, pers):
        '''
        The function modifies a person from the repo
        :param: pers
        :post: the person with the id of pers will be updated with the pers dates
        '''
        if not pers in self.persons.values():
            raise PersonRepositoryException("We can't find the person to modify")
        self.persons[pers.get_id()].set_name(pers.get_name())
        self.persons[pers.get_id()].set_adress(pers.get_adr())
    def search(self, id):
        '''
        The function searches for a person
        :param: id
        :return: the person with the id
        '''
        if id in self.persons.keys():
            return self.persons[id]
        else:
            raise PersonRepositoryException("This id doesn't exist")
        
        