'''
Created on 28 Nov 2018

@author: Teuodor
'''
from domain.event import Event
from domain.assignament import Assignament
from domain.person import Person
from domain.validari import ValidareEvents,ValidarePersons
class TestEntitati:
    def __init__(self):
        pass
    def testEvents(self):
        e=Event('1','20/01/2018','13:00','Wedding')
        assert e.get_id()=='1'
        assert e.get_date()=='20/01/2018'
        assert e.get_time()=='13:00'
        assert e.get_desc()=='Wedding'
        e.set_id('2')
        e.set_date('21/01/2018')
        e.set_time('14:00')
        e.set_desc('Funeral')
        assert e.get_id()=='2'
        assert e.get_date()=='21/01/2018'
        assert e.get_time()=='14:00'
        assert e.get_desc()=='Funeral'
        e2=Event('2','20/01/2018','14:00','Course')
        assert e==e2
        assert e2<e
        
    def testAssignament(self):
        assig=Assignament('1','2')
        assert assig.get_event_id()=='2'
        assert assig.get_person_id()=='1'
        assig2=Assignament('1','2')
        assert assig==assig2
    
    def testPerson(self):
        p=Person('1','Teodor','Valcea')
        assert p.get_id()=='1'
        assert p.get_adr()=='Valcea'
        assert p.get_name()=='Teodor'
        p.set_adress('Brasov')
        p.set_id('2')
        p.set_name('Vlad')
        assert p.get_id()=='2'
        assert p.get_adr()=='Brasov'
        assert p.get_name()=='Vlad'
        p2=Person('2','Vlad','Brasov')
        assert p==p2
    
    def testValidareEvents(self):
        validator=ValidareEvents()
        ev=Event('1','20/05/1998','23:23','Wedding')
        try:
            validator.validare(ev)
            assert True
        except:
            assert False
    def testValidarePersons(self):
        validator=ValidarePersons()
        pers=Person('1','Ana','Valcea')
        try:
            validator.validare(pers)
            assert True
        except:
            assert False
            
test=TestEntitati()
test.testAssignament()
test.testEvents()
test.testPerson()
test.testValidareEvents()
test.testValidarePersons()