'''
Created on 3 Feb 2019

@author: Teuodor
'''
from Domain.Jucator import Jucator
class ExceptionRepoJucatori(Exception):
    pass

class RepoJucFile:
    def __init__(self):
        self.__jucatori = self.__loadFromFile
    def __loadFromFile(self):
        '''
        O functie ce creeaza un dictionar de jucatori
        :return: un dictionar cu toti jucatorii
        '''
        try:
            f = open('jucatori.txt' , 'r')
        except IOError:
            print("The file doesn't exist")
            return {}
        line = f.readline().strip()
        content = {}
        while line != "":
            attr = line.split(',')
            st = Jucator(attr[0],attr[1],attr[2],attr[3])
            content[ attr[0] ] = st
            line = f.readline().strip()
        f.close()
        return content
    
    def __saveInFile(self,jucatori):
        '''
        Functia salveaza intr un fisier un dictionar
        :param: jucatori - un dictionar cu jucatori
        '''
        with open('jucatori.txt' , 'w') as f:
            for jucator in jucatori.values():
                s = str(jucator.get_nume()) + ',' + str(jucator.get_prenume()) + ',' + str(jucator.get_post()) +','+str(jucator.get_inaltime)+ '\n'
                f.write(s)
            
    def load(self):
        '''
        Functia pune din fisier in repo
        '''
        self.__jucatori = self.__loadFromFile()
        
    def save(self):
        '''
        Functia salveaza in fisier din repo
        '''
        self.__saveInFile(self.__jucatori)
    
    def get_persons(self):
        '''
        A function that returns a list of all the events
        :return: a list of all the events
        '''
        self.__persons = self.__loadFromFile()
        return self.__persons.values()
    
    def store(self, elem):
        '''
        The function add a person to the repo and file
        :param: elem
        :post: the person is added to the list of persons and file
        '''
        values = self.get_persons()
        if elem in values:
            raise ExceptionRepoPersons("This person already exist")
        self.__persons[elem.get_id()] = elem
        self.__saveInFile(self.__persons)
    
    def delete(self,id):
        '''
        The function deletes a person from the repo and file
        :param: id
        :post: the person will be deleted from the list and file
        '''
        if not id in self.__persons.keys():
            raise ExceptionRepoPersons("This id doesn't exist")
        del self.__persons[id]
        self.__saveInFile(self.__persons)
        
    def modify(self,pers):
        '''
        The function modifies a person from the repo and file
        :param: pers
        :post: the person with the id of pers will be updated with the pers dates
        '''
        values = self.get_persons()
        if not pers in values:
            raise ExceptionRepoPersons("This person doesn't exist")
        self.__persons[pers.get_id()].set_name(pers.get_name())
        self.__persons[pers.get_id()].set_adress(pers.get_adr())
        self.__saveInFile(self.__persons)
    
    def search(self,id):
        '''
        The function searches for a person
        :param: id
        :return: the person with the id
        '''
        values = self.get_persons()
        for k in values:
            if k.get_id()==id:
                return self.__persons[id]
        raise ExceptionRepoPersons("This id doesn't exist")
    
    def clear_file(self):
        '''
        A function that clear the file
        '''
        self.__persons = {}
        self.__saveInFile(self.__persons)