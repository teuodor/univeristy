from domain.person import Person
from repository.repoPerson import personRepository
from utils.helper import *
from domain.validari import ValidarePersons
class PersonService:
    def __init__(self,repoPers):
        self.__rep=repoPers
        
    def get_persons(self):
        return self.__rep.get_persons()
    
    def createPerson(self,id,name,address):
        '''
        Creates a person 
        :param: id
        :param: name
        :param: address
        :post: the person is added to the list
        '''
        pers=Person(id,name,address)
        validator=ValidarePersons()
        validator.validare(pers)
        self.__rep.store(pers)
        return pers
    def deletePerson(self,id):
        '''
        Deletes a person
        :param: id
        :post: the person is deleted from the list
        '''
        self.__rep.delete(id)
    def updatePerson(self,id,name,address):
        '''
        Update a person
        :param: id
        :param: name
        :param: address
        :post: the person with the id of the new person will be updated with the new name and address
        '''
        pers=Person(id,name,address)
        validator=ValidarePersons()
        validator.validare(pers)
        self.__rep.modify(pers)
    def get_random(self,number):
        '''
        Creates a number of random people
        :param: number
        :post: creates a 'number' of random people
        '''
        for k in range(number):
            rand_id=str(rand_int())
            rand_name=rand_string(5)
            rand_address=rand_string(7)
            self.createPerson(rand_id, rand_name, rand_address)
    def search(self, id):
        '''
        The function search for a person, knowing the person's id
        :param: id
        :return: the person with the id
        '''
        return self.__rep.search(id)
    def save(self):
        '''
        The function saves in file the repository
        '''
        self.__rep.save()
    def load(self):
        '''
        The function loads from file to repository
        '''
        self.__rep.load()