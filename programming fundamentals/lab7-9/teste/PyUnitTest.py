'''
Created on 19 Dec 2018

@author: Teuodor
'''
from unittest.case import TestCase
from domain.person import Person
from domain.event import Event
from domain.validari import ValidarePersons, ValidareEvents
from repository.repoPerson import personRepository, PersonRepositoryException
from repository.repoEvent import eventRepository, EventRepositoryException
from service.servicePerson import PersonService
from service.serviceEvent import EventService
from repository.repoAssign import assignamentRepository
from service.serviceAssignament import AssignamentService

class test_person(TestCase):
    def test_person_entity(self):
        '''
        Function for testing the person entity
        '''
        pers = Person('1','Teo','Valcea')
        self.assertEqual(pers.get_id(),'1')
        self.assertEqual(pers.get_name(), 'Teo')
        self.assertEqual(pers.get_adr(), 'Valcea')
   
class test_event(TestCase):     
    def test_event_entity(self):
        '''
        Function for testing the event entity
        '''
        ev = Event('1','12/09/1999','17:00','The end of the world')
        self.assertEqual(ev.get_id(), '1')
        self.assertEqual(ev.get_date(), '12/09/1999')
        self.assertEqual(ev.get_time(), '17:00')
        self.assertEqual(ev.get_desc(), 'The end of the world')
        
class test_person_validator(TestCase):
    def test_validator(self):
        '''
        Function for testing the validator of persons
        '''
        pers = Person("","","")
        validator = ValidarePersons()
        
        with self.assertRaises(Exception):
            validator.validare(pers)
        
        pers = Person("1","","")
        
        with self.assertRaises(Exception):
            validator.validare(pers)
            
        pers = Person("1","Dragos","")
        
        with self.assertRaises(Exception):
            validator.validare(pers)
            
class test_event_validator(TestCase):            
    def test_validator(self):
        '''
        Function for testing the validator of events
        '''
        ev = Event("","","","")
        
        validator = ValidareEvents()
        
        with self.assertRaises(Exception):
            validator.validare(ev)
        
        ev = Event("1","","","")
        
        with self.assertRaises(Exception):
            validator.validare(ev)
            
        ev = Event("1","12/09/2108","","Funeral")
        
        with self.assertRaises(Exception):
            validator.validare(ev)
            
class test_person_repo(TestCase):
    def test_repo(self):
        '''
        Function for testting the person repository
        '''
        pers = Person('1','Teo','Valcea')
        repo =  personRepository()
        
        self.assertEqual(len(repo.persons),0)
        
        repo.store(pers)
        
        self.assertEqual(len(repo.persons),1)
        
        pers = Person('2','Cristi','Maramures')
        repo.store(pers)
        
        self.assertEqual(len(repo.persons),2)
        
        repo.delete('2')
        
        self.assertEqual(len(repo.persons),1)
        
class test_event_repo(TestCase):
    def test_repo(self):
        '''
        Function for testing the event repossitory
        '''        
        
        ev = Event('1','31/03/2019','12:00','Wedding')
        repo = eventRepository()
        
        self.assertEqual(len(repo.events),0)
        
        repo.store(ev)
        
        self.assertEqual(len(repo.events),1)
        
        ev = Event('2','22/08/2019','13:00','Pomana')
        repo.store(ev)
        
        self.assertEqual(len(repo.events),2)

        repo.delete('2')
        
        self.assertEqual(len(repo.events),1)
        
class test_person_service(TestCase):
    def test_service(self):
        '''
        Function for testing the person service
        '''
        
        repo = personRepository()
        service = PersonService(repo)
        
        pers = service.createPerson('1', 'Teo', 'Valcea')
        
        self.assertEqual(pers.get_id(),1)
        self.assertEqual(pers.get_name(),'Teo')
        self.assertEqual(pers.get_adr(),'Valcea')
        
        dict = service.get_persons()
        
        self.assertEqual(len(dict),1)
        
        with self.assertRaises(Exception):
            service.createPerson('1','Adi','Bistrita')
            
        with self.assertRaises(Exception):
            service.createPerson("","","")
            
class test_event_service(TestCase):
    def test_service(self):
        '''
        Function for testing the event service
        '''
        repo = eventRepository()
        service = EventService(repo)
        
        ev = service.createEvent('1', '12/08/1999','17:00', 'Wow')
        self.assertEqual(ev.get_id(),'1')
        self.assertEqual(ev.get_date(),'12/08/1999')
        self.assertEqual(ev.get_time(),'17:00')
        self.assertEqual(ev.get_desc(),'Wow')
        
        dict = service.get_all_events_service()
        
        self.assertEqual(len(dict),1)
        
        with self.assertRaises(Exception):
            service.createEvent('1','31/03/2108','17:00','Wow')
            
        with self.assertRaises(Exception):
            service.createEvent("", "", "", "")
            
class test_assignament_service(TestCase):
    def test_service(self):
        '''
        Function for testing the assignament service
        '''
        
        repo = assignamentRepository()
        service = AssignamentService(repo)
        
        assign = service.create_assign('1', '2')
        
        self.assertEqual(assign.get_person_id(),'1')
        self.assertEqual(assign.get_event_id(), '2')
        
        
class test_person_store(TestCase):
    
    def setUp(self):
        self.repo = personRepository()
        self.person3 = Person("5", "Andrei", "Roman")
        self.person1 = Person("2", "Alex", "Caracal")
        self.person2 = Person("3", "Andrada", "Valcea")
        self.repo.store(self.person1)
        self.repo.store(self.person2)
        self.repo.store(self.person3)
        
    def tearDown(self):
        for i in self.repo.persons:
            self.repo.delete(i.get_id())
            
    def test_store(self):
        self.assertEqual(len(self.repo.persons), 3)
        self.assertEqual(self.repo.search('2'), self.person1)
        #verify if the person is in repo
        self.assertEqual(len(self.repo.persons), 3)
        self.assertEqual(self.repo.search('3'), self.person2)


class test_event_store(TestCase):
    
    def setUp(self):
        self.repo = eventRepository()
        self.event1 = Event("1", "20/11/2012", "10:58", "Funeral")
        self.event2 = Event("2", "20/09/2013", "11:21", "Party")
        self.event3 = Event("3", "19/06/2017", "12:31", "Wedding")
        self.repo.store(self.event1)
        self.repo.store(self.event2)
        self.repo.store(self.event3)
        
    def tearDown(self):
        for i in self.repo.events:
            self.repo.delete(i.get_id())
            
    def test_store(self):
        self.assertEqual(len(self.repo.events), 3)
        self.assertEqual(self.repo.search('2'), self.event2)
        #verify if the person is in repo
        self.assertEqual(len(self.repo.events), 3)
        self.assertEqual(self.repo.search('3'), self.event3)
            