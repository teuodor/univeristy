class Event:
    '''
    Class which represents the event object defined by
    id, date, time and description - all strings
    '''
    
    def __init__(self, id_event, date, time, desc):
        self.__id = id_event
        self.__date = date
        self.__time = time
        self.__desc = desc
        
    def get_id(self):
        '''
        The function returns the current event's id
        :return: a string id
        '''
        return self.__id
    
    def get_date(self):
        '''
        The function returns the current event's date
        :return: a string date
        '''
        return self.__date
    
    def get_time(self):
        '''
        The function returns the current event's time
        :return: a string time
        '''
        return self.__time
    
    def get_desc(self):
        '''
        The function returns the current event's description
        :return: a string description
        '''
        return self.__desc
    
    def set_id(self,id1):
        '''
        The function sets the current event's id
        :param: id
        :post: the id will be set
        '''
        self.__id=id1
        
    def set_date(self,date):
        '''
        The function sets the current event's date
        :param: date
        :post: the date will be set
        '''
        self.__date=date
        
    def set_time(self,time):
        '''
        The function sets the current event's time
        :param: time
        :post: the time will be set
        '''
        self.__time=time
        
    def set_desc(self,desc):
        '''
        The function sets the current event's description
        :param: description
        :post: the description will be set
        '''
        self.__desc=desc
        
    def __lt__(self, other):
        '''
        Tells how to compare 2 event objects
        '''
        if self.__desc < other.__desc:
            return True
        if self.__desc == other.__desc:
            if self.__date <= other.__date:
                return True
        return False
    
    def __eq__(self,other):
        '''
        Tells when 2 event objects are equal
        '''
        return self.get_id()==other.get_id()