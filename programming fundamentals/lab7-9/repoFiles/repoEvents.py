from domain.event import Event

class ExceptionRepoEvents(Exception):
    pass

class RepoEventsFile:
    def __init__(self):
        self.__events = self.__loadFromFile
    def __loadFromFile(self):
        '''
        The function creates a dictionary with the data from the file
        :return: a dict with all the events
        '''
        try:
            f = open('events.txt' , 'r')
        except IOError:
            print("The file doesn't exist")
            return {}
        line = f.readline().strip()
        content = {}
        while line != "":
            attr = line.split(',')
            ev = Event( attr[0] , attr[1] , attr[2] , attr[3] )
            content[ attr[0] ] = ev
            line = f.readline().strip()
        f.close()
        return content
    def __saveInFile(self,events):
        '''
        The function saves in file the data from a dictionary
        :param: events - a dictionary with events
        '''
        with open('events.txt' , 'w') as f:
            for event in events.values():
                s = str(event.get_id()) + ',' + str(event.get_date())+',' + str(event.get_time()) + ',' + str(event.get_desc()) + '\n'
                f.write(s)
                
    def load(self):
        '''
        The function loads from file to repository
        '''
        self.__events = self.__loadFromFile()
    
    def save(self):
        '''
        The function saves in file the repository
        '''
        self.__saveInFile(self.__events)
        
    def get_events(self):
        '''
        A function that returns a list of all the events
        :return: a list of all the events
        '''
        self.__events = self.__loadFromFile()
        return self.__events.values()
    
    def store(self, elem):
        '''
        The function add an event to the repo
        :param: elem
        :post: the event will be added to the list and file
        '''
        values = self.get_events()
        if elem in values:
            raise ExceptionRepoEvents("The event already exists")
        self.__events[elem.get_id()] = elem
        self.__saveInFile(self.__events)
        
    def delete(self, id):
        '''
        The function delete an event from the repo 
        :param: id
        :post: the event will be deleted from the list of events
        '''
        if not id in self.__events.keys():
            raise ExceptionRepoEvents("The event can't be found")
        del self.__events[id]
        self.__saveInFile(self.__events)
        
    def modify(self,elem):
        '''
        The function modify an event from the repo
        :param: ev
        :post: the event with the ev id will be updated with ev dates
        '''
        values = self.get_events()
        if not elem in values:
            raise ExceptionRepoEvents("The event can't be found")
        self.__events[elem.get_id()].set_date(elem.get_date())
        self.__events[elem.get_id()].set_time(elem.get_time())
        self.__events[elem.get_id()].set_desc(elem.get_desc())
        self.__saveInFile(self.__events)
    
    def search(self,id):
        '''
        The function searches for an event
        :param: id
        :return: the event with the id
        '''
        values = self.get_events()
        for k in values:
            if k.get_id()==id:
                return self.__events[id]
        raise ExceptionRepoEvents("The event can't be found")
    
    def clear_file(self):
        '''
        A function that clear the file
        '''
        self.__events = {}
        self.__saveInFile(self.__events)
        
        
        
        
        
        
        
        