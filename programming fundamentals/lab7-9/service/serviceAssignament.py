from domain.assignament import Assignament
from repository.repoAssign import assignamentRepository
from domain.name_nrevent_hour import NameNrEventHour
class AssignamentService:
    def __init__(self,assignRepo):
        self.__rep=assignRepo
    def get_all_assign_service(self):
        '''
        Function that gets all assignments from repository
        :return: a list with all assignments
        '''
        return self.__rep.get_all_assign()
    def create_assign(self,id_person,id_event):
        '''
        Creates an assignament
        :param: id_person
        :param: id_events
        :post: the assignament will be added to the list
        '''
        assign=Assignament(id_person,id_event)
        self.__rep.store(assign)
        return assign
    def get_person_enrolled(self,person_id):
        '''
        Make a list of the events where a person goes
        :param: person_id
        :return: the list of events in which the person is enrolled
        '''
        list_events=[]
        list_assig=self.__rep.get_all_assign()
        for assignament in list_assig:
            if person_id==assignament.get_person_id():
                list_events.append(assignament.get_event_id())
        return list_events
    def get_most_participants(self):
        '''
        Functions that returns the most partcipants to the most events
        :return: a list of persons with the biggest number of events
        '''
        dict = {}
        list = []
        list2 = self.get_all_assign_service()
        for assig in list2:
            if assig.get_person_id() in dict:
                dict[assig.get_person_id()] += 1
            else:
                dict[assig.get_person_id()] = 1
        max_events = 0
        for k,val in dict.items():
            if val > max_events:
                max_events = val
        for k,val in dict.items():
            if val == max_events:
                list.append(k)
        return list
    
    
    def first_20_percent(self):
        '''
        Determine the first 20% of the events by the number of participants
        :return: a matrix of 2 columns where list_events[x][0]=the event id and list_events[x][1]=the number of participants
        '''
        list = self.get_all_assign_service()
        dict = {}
        for assig in list:
            if assig.get_event_id() in dict:
                dict[assig.get_event_id()] += 1
            else:
                dict[assig.get_event_id()] = 1
                
        list_events=[]
        
        for event,val in dict.items():
            list_events.append([event,val])
        list_events=sorted(list_events,key = lambda x: x[1], reverse=True)
        
        if len(list_events)>=5:
            index=len(list_events)//5
        else:
            index=1
        
        return list_events[0:index]
    def mostEvents(self,list):
        '''
        The persons with the biggest number of events which are in the list
        :param: list-the events which starts at a bigger hour than v
        :return: list with the persons
        '''
        dict={}
        list2=[]
        all_assign=self.get_all_assign_service()
        for x in list:
            for y in all_assign:
                if x.get_id()==y.get_event_id():
                    if y.get_person_id() in dict.keys():
                        dict[y.get_person_id()] += 1
                    else:
                        dict[y.get_person_id()] = 1
        
        max=0
        for val in dict.values():
            if val > max:
                max=val
                
        for key,val in dict.items():
            if not val == max:
                list2.append(key)
        
        for key in list2:
            if key in dict:
                del dict[key]
                
        return dict
    def name_nr_hour(self, dict, persService, v):
        '''
        Tha function create a list of NameNrEventHour objects from the data of a dictionary
        :param: dict - a dictionary with the data
        :param: persService - for searching the pers with the id
        :param: v - the condition
        :return: list - a list of objects
        '''
        list=[]
        for key,val in dict.items():
            pers = persService.search(key)
            p = NameNrEventHour(pers.get_name(),val,v)
            list.append(p)
        return list
    def del_person(self,id):
        '''
        A function that deletes all assignaments which have an person id
        :param id: the person id
        :post: the assignament will be deleted from the list and file 
        '''
        self.__rep.delete_person(id)
    def del_event(self,id):
        '''
        A function that deletes all assignaments which have an event id
        :param id: the event id
        :post: the assignament will be deleted from the list SSSand file 
        '''
        self.__rep.delete_event(id)
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
