'''
Created on 28 Nov 2018

@author: Teuodor
'''
from domain.person import Person
from repository.repoPerson import personRepository
from domain.event import Event
from repository.repoEvent import eventRepository
from domain.assignament import Assignament
from repository.repoAssign import assignamentRepository
class TestRepo:
    def __init__(self):
        pass
    def testPerson(self):
        p1=Person('1','Teodor','Valcea')
        p2=Person('2','Vlad','Brasov')
        p3=Person('3','Mark','Anglia')
        repo=personRepository()
        repo.store(p1)
        repo.store(p2)
        repo.store(p3)
        repo.delete('1')
        p4=Person('3','Richard','Scotia')
        repo.modify(p4)
        assert repo.persons['2']==p2
        assert repo.persons['3']==p4
    def testEvents(self):
        e1=Event('1','20/01/2018','20:00','Ohai')
        e2=Event('2','12/12/2018','21:00','HEllo')
        e3=Event('3','22/02/2019','23:00','Fart')
        repo=eventRepository()
        repo.store(e1)
        repo.store(e2)
        repo.store(e3)
        repo.delete('1')
        e4=Event('3','30/01/2019','23:23','Party')
        repo.modify(e4)
        assert repo.events['2']==e2
        assert repo.events['3']==e4
    def testAssignament(self):
        a1=Assignament('1','2')
        a2=Assignament('2',1)
        repo=assignamentRepository()
        repo.store(a1)
        repo.store(a2)
        assert repo.list==[a1,a2]
        

        
test=TestRepo()
test.testAssignament()
test.testPerson()
test.testEvents()