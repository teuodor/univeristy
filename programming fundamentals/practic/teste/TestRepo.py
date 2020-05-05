'''
Created on 4 Feb 2019

@author: Teuodor
'''
from Repository.RepoTV import RepoTvFile
class test_repo:
    def test(self):
        repo = RepoTvFile()
        repo.load()
        repo.delete('Free party','Documentar')
        assert len(repo.tvshows) == 1
        repo.update('1', '2', '3', '4', '2', '2')
        assert repo.tvshows['1'].get_tip() == '2' 
        assert repo.tvshows['1'].get_durata() == '2'
        assert repo.tvshows['1'].get_descriere() == '2'
        
test = test_repo()
test.test()
