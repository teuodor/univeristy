from domain.event import Event
from repository.repoEvent import eventRepository
from utils.helper import compare_hours
from domain.validari import ValidareEvents
class EventService:
    def __init__(self,repoEvents):
        self.__rep=repoEvents
        
    def get_all_events_service(self):
        return self.__rep.get_events()
    
    def createEvent(self,id,date,time,desc):
        '''
        Creates an event
        :param: id
        :param: date
        :param: time 
        :param: desc
        :post: the event will be added to the list
        '''
        ev=Event(id,date,time,desc)
        validator=ValidareEvents()
        validator.validare(ev)
        self.__rep.store(ev)
        return ev
    def deleteEvent(self, id):
        '''
        Delete an event
        :param: id
        :post: delete the event from the list
        '''
        self.__rep.delete(id)
    def updateEvent(self, id, date, time, desc):
        '''
        Updates an event
        :param: id
        :param: date
        :param: time
        :param: desc
        :post: the event with the same id of the new event will be updated with the new date, time, description
        '''
        ev=Event(id,date,time,desc)
        validator=ValidareEvents()
        validator.validare(ev)
        self.__rep.modify(ev)
    def sort_secv_events(self, list_id):
        '''
        Sort a sequence of events by a list of ids
        :param: list_id
        :return: a list of events sorted 
        '''
        list_events = []
        lista = self.get_all_events_service()
        for event in lista:
            if event.get_id() in list_id:
                list_events.append(event)
        list_events = sorted(list_events, reverse=False)
        return list_events
    def get_all_id(self):
        '''
        Get all ids of the events
        :return: a list of all event's ids
        '''
        lista = []
        values=self.__rep.events.values()
        for k in values:
            lista.append(k.get_id())
        return lista
    def more_than_v(self,v):
        '''
        A function that returns a list of events which has the hour bigger than v
        :param: v-the hour for comparison
        :return: list-with the events with the hour bigger than v
        '''
        list = []
        for k in self.get_all_events_service():
            if compare_hours(k.get_time(), v) == True:
                list.append(k)
        return list
    def search(self, id):
        '''
        The function search for an event, knowing the event's id
        :param: id
        :return: the event with the id
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
