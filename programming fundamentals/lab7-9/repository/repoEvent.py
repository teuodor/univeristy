'''
Created on 13 Nov 2018

@author: Teuodor
'''
class EventRepositoryException(Exception):
    pass
class eventRepository:
    def __init__(self):
        self.events = {}
    
    def get_events(self):
        return self.events.values()
    
    def store(self, ev):
        '''
        The function add an event to the repo
        :param: ev
        :post: the event will be added to the list 
        '''
        if ev.get_id() in self.events.keys():
            raise EventRepositoryException("An event with this id exist")
        self.events[ev.get_id()]=ev
    def delete(self, id):
        '''
        The function delete an event from the repo 
        :param: id
        :post: the event will be deleted from the list of events
        '''
        if not id in self.events.keys():
            raise EventRepositoryException("We can't find the event")
        del self.events[id]
    def modify(self, ev):
        '''
        The function modify an event from the repo
        :param: ev
        :post: the event with the ev id will be updated with ev dates
        '''
        if not ev.get_id() in self.events.keys():
            raise EventRepositoryException("We can't find the event to modify")
        self.events[ev.get_id()].set_date(ev.get_date())
        self.events[ev.get_id()].set_time(ev.get_time())
        self.events[ev.get_id()].set_desc(ev.get_desc())
    
    def search(self, id):
        '''
        The function searches for an event
        :param: id
        :return: the event with the id
        '''
        if id in self.events.keys():
            return self.events[id]
        else:
            raise  EventRepositoryException("This id doesn't exist")
    
    def sort_secv_events(self, list_id):
        '''
        The function returns a sorted list of events
        :param: list_id
        :return: a sorted list of events by receiving a list of ids
        '''
        list_events = []
        values=self.events.values()
        for event in values:
            if event.get_id() in list_id:
                list_events.append(event)
        list_events = sorted(list_events, reverse = False)
        return list_events
