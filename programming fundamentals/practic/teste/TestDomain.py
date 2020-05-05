'''
Created on 4 Feb 2019

@author: Teuodor
'''
from Domain.Emisiuni import TV
class test_domain:
    def test(self):
        a = TV('Free party','Documentar',3,'Information')
        assert a.get_nume() == 'Free party'
        assert a.get_tip() == 'Documentar'
        assert a.get_durata() == 3
        assert a.get_descriere() == 'Information'
        a.set_nume('Posibil')
        a.set_tip('Posibilitate')
        a.set_durata(4)
        a.set_descriere('Informare')
        assert a.get_nume() == 'Posibil'
        assert a.get_tip() == 'Posibilitate'
        assert a.get_durata() == 4
        assert a.get_descriere() == 'Informare'
        
        
test = test_domain()
test.test()