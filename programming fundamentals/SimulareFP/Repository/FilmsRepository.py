'''
Created on 13 Dec 2018

@author: Teuodor
'''
from Domain.Films import Films
class RepositoryFilms:
    def __init__(self):
        self.__repo = self.__loadFromFile
    
    def __loadFromFile(self):
        '''
        A function that makes a dictionary with all the data from films.txt
        '''
        try:
            f = open("films.txt", "r")
        except IOError:
            print("The file doesn't exist")
            return {}
        
        line=f.readline().strip()
        content={}
        
        while line!="":
            attr = line.split(",")
            film = Films(attr[0],attr[1],attr[2],attr[3])
            content[film.get_id()] = film
            line = f.readline().strip()
            
        f.close()
        
        return content
    
    def __saveInFile(self,dict):
        '''
        A function that save in file the data from a dictionary
        '''
        with open("films.txt","w") as f:
            for k in dict.values():
                s=str(k.get_id())+","+str(k.get_title())+","+str(k.get_price())+","+str(k.get_nr())+"\n"
                f.write(s)
                
    def load(self):
        '''
        A function that load from file in the repository
        '''
        self.__repo = self.__loadFromFile()
        
    def save(self):
        '''
        A function that save in file tha data from the repository
        '''
        self.__saveInFile(self.__repo)       
            
    def search(self,id):
        '''
        A function that search for film by its id
        :param: id
        :return: the film with the specific id
        '''
        return self.__repo[id]
    
    def get_all_films(self):
        return self.__repo
            
        