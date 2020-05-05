class Assignament:
    '''
    Class which define the assignament object defined by
    id_person,id_event - all strings
    '''
    def __init__(self, id_person, id_event):
        self.__id_pers = id_person
        self.__id_event = id_event
        
    def get_person_id(self):
        '''
        The function returns the current assignament person's id
        :return: a string id
        '''
        return self.__id_pers
    
    
    def get_event_id(self):
        '''
        The function returns the current assignament event's id
        :return: a string id
        '''
        return self.__id_event
    
    def __eq__(self, ot):
        '''
        Tells if two assignament objects are equal
        '''
        return (self.get_person_id() == ot.get_person_id()) and (self.get_event_id() == ot.get_event_id())