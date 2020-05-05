'''
Created on 4 Feb 2019

@author: Teuodor
'''
from Domain.Emisiuni import TV
class ExceptionRepoTv(Exception):
    pass

class RepoTvFile:
    '''
    The repository for tv shows
    '''
    def __init__(self):
        self.tvshows = self.__loadFromFile
    def __loadFromFile(self):
        '''
        The function creates a dictionary with the data from the file
        :return: a dict with all the tv shows
        '''
        try:
            f = open('shows.txt' , 'r')
        except IOError:
            print("The file doesn't exist")
            return {}
        line = f.readline().strip()
        content = {}
        while line != "":
            attr = line.split(',')
            st = TV(attr[0],attr[1],attr[2],attr[3])
            content[ attr[0] ] = st
            line = f.readline().strip()
        f.close()
        return content
    
    def __saveInFile(self,tv_shows):
        '''
        The function saves in file the data from a dictionary
        :param: tvshows - a dictionary with tv shows
        '''
        with open('shows.txt' , 'w') as f:
            for show in tv_shows.values():
                s = str(show.get_nume()) + ',' + str(show.get_tip()) + ',' + str(show.get_durata())+ ',' + str(show.get_descriere())+ '\n'
                f.write(s)
            
    def load(self):
        '''
        The function loads from file to repository
        '''
        self.tvshows = self.__loadFromFile()
        
    def save(self):
        '''
        The function saves in file the repository
        '''
        self.__saveInFile(self.tvshows)
    
    def delete(self,name,tip):
        '''
        The function deletes a tv show from the repo and file
        :param: name,tip
        :post: the tv show will be deleted from the dict and file
        '''
        if not name in self.tvshows.keys():
            raise ExceptionRepoTv("This name doesn't exist")
        elif not tip == self.tvshows[name].get_tip():
            raise ExceptionRepoTv("This tip doesn't exist")
        del self.tvshows[name]
        self.__saveInFile(self.tvshows)
        
    def update(self,name,tip,durata,descriere,new_desc,new_time):
        '''
        The function updates the time and description of a tv show
        :param: name,tip,durata,descriere
        :post: the tv show will be updated
        '''
        if not name in self.tvshows.keys():
            raise ExceptionRepoTv("This name doesn't exist")
        elif not tip == self.tvshows[name].get_tip():
            raise ExceptionRepoTv("This tip doesn't exist")
        elif not durata == self.tvshows[name].get_durata():
            raise ExceptionRepoTv("This time doesn't exist")
        elif not descriere == self.tvshows[name].get_descriere():
            raise ExceptionRepoTv("This description doesn't exist")
        
        self.tvshows[name].set_descriere(new_desc)
        self.tvshows[name].set_durata(new_time)
        
    def search(self,name):
        '''
        The function searches after a tv show object
        :input: name - one of the keys
        :return: the object which has the key
        '''
        if not name in self.tvshows.keys():
            raise ExceptionRepoTv("This name doesn't exist")
        return self.tvshows[name]
        