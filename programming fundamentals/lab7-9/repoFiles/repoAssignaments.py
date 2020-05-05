from domain.assignament import Assignament
class ExceptionRepoAssig(Exception):
    pass

class RepoAssigsFile:
    def __init__(self):
        self.__assigs = self.__loadFromFile
    
    def __loadFromFile(self):
        '''
        The function creates a list with the data from the file
        :return: a list with all the assignaments
        '''
        try:
            f = open('assignaments.txt' , 'r')
        except IOError:
            print("The file doesn't exist")
            return {}
        line = f.readline().strip()
        content = []
        while line != "":
            attr = line.split(',')
            ass = Assignament( attr[0] , attr[1] )
            content.append(ass)
            line = f.readline().strip()
        
        f.close()
        return content
    def __saveInFile(self,assig):
        '''
        The function saves in file the data from a list
        :param: assig - a dictionary with assignaments
        '''
        with open('assignaments.txt' , 'w') as f:
            for ass in assig:
                s = str(ass.get_person_id()) + ',' + str(ass.get_event_id()) + '\n'
                f.write(s)
    
    def getAllAssig(self):
        self.__assigs = self.__loadFromFile()
        return self.__assigs
    
    def load(self):
        '''
        The function loads from file to repository
        '''
        self.__assigs = self.__loadFromFile()
    
    def save(self):
        '''
        The function saves in file the repository
        '''
        self.__saveInFile(self.__assigs)
        
    def store(self,assig):
        '''
        The function stores a new assignament
        :param: assig
        :post: the new assignament will be added to the list and file
        '''
        if assig in self.__assigs:
            raise ExceptionRepoAssig("This assignament already exists")
        self.__assigs.append(assig)
        self.__saveInFile(self.__assigs)
    def delete_person(self,id):
        '''
        A function that deletes all assignaments which have an person id
        :param id: the person id
        :post: the assignament will be deleted from the list and file 
        '''
        lun=len(self.__assigs)
        index=0
        while index<lun:
            if self.__assigs[index].get_person_id() == id:
                self.__assigs.remove(self.__assigs[index])
                index-=1
                lun-=1
            index+=1
        self.__saveInFile(self.__assigs)
    def delete_event(self,id):
        '''
        A function that deletes all assignaments which have an event id
        :param id: the event id
        :post: the assignament will be deleted from the list and file 
        '''
        lun=len(self.__assigs)
        index=0
        while index<lun:
            if self.__assigs[index].get_event_id() == id:
                self.__assigs.remove(self.__assigs[index])
                index-=1
                lun-=1
            index+=1
        self.__saveInFile(self.__assigs)
    def clear_file(self):
        '''
        A function that clear the file
        '''
        self.__assigs = []
        self.__saveInFile(self.__assigs)
    def get_all_assign(self):
        '''
        A function which returns a list of all the assignaments
        :return: a list of all assignaments
        '''
        return self.__assigs
        