'''
Created on 4 Feb 2019

@author: Teuodor
'''
from Repository.RepoTV import RepoTvFile
from Service.ServiceTV import ServiceTv
class test_service:
    def test(self):
        repo = RepoTvFile()
        serv = ServiceTv(repo)
        serv.load()
        serv.delete('Free party','Documentar')
        assert len(repo.tvshows) == 1
        serv.update('1', '2', '3', '4', '2', '2')
        assert serv.TVshows.tvshows['1'].get_tip() == '2' 
        assert serv.TVshows.tvshows['1'].get_durata() == '2'
        assert serv.TVshows.tvshows['1'].get_descriere() == '2'
        
test = test_service()
test.test()