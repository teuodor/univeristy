'''
Created on 28 Nov 2018

@author: Teuodor
'''
from repository.repoAssign import assignamentRepository
from service.serviceAssignament import AssignamentService
from repository.repoPerson import personRepository
from service.servicePerson import PersonService
from repository.repoEvent import eventRepository
from service.serviceEvent import EventService
class TestService:
    def __init__(self):
        pass
    def testPersonService(self):
        a=personRepository()
        b=PersonService(a)
        b.createPerson('1', 'Teodor', 'Valcea')
        b.createPerson('2', 'Vlad', 'Brasov')
        b.createPerson('3', 'Dragos', 'Ramnic')
        b.deletePerson('1')
        assert len(b.get_all_id())==2
        
    def testEventService(self):
        a=eventRepository()
        b=EventService(a)
        b.createEvent('1', '20/09/2019', '12:00', 'Birthday')
        b.createEvent('2', '21/08/2022', '13:00', 'Concert')
        b.createEvent('3', '30/01/2019', '14:00', 'Wedding')
        b.deleteEvent('3')
        assert len(b.get_all_id())==2
        
    def testAssignamentService(self):
        a=assignamentRepository()
        b=AssignamentService(a)
        b.create_assign('1', '2')
        b.create_assign('3', '4')
        b.create_assign('1', '1')
        b.create_assign('2', '2')
        b.create_assign('2', '1')
        b.create_assign('2', '3')
        b.create_assign('3','2')
        c=b.get_person_enrolled('1')
        assert c==['2','1']
        c=b.get_most_participants()
        assert c==['2']
        c=b.first_20_percent()
        assert c==[['2',3]]
    
test=TestService() 
test.testPersonService()   
test.testEventService()
test.testAssignamentService()
