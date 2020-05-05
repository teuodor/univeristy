'''
Created on 3 Feb 2019

@author: Teuodor
'''
class Jucator:
    '''
    
    '''
    def __init__(self,nume,prenume,post,inaltime):
        self.nume = nume
        self.prenume = prenume
        self.post = post
        self.inaltime = inaltime
    def get_nume(self):  
        return self.nume
    
    def get_prenume(self):
        return self.prenume
    
    def get_post(self):
        return self.post
    
    def get_inaltime(self):
        return self.inaltime
    
    def set_nume(self,nume):  
        self.nume = nume
        
    def set_prenume(self,prenume):
        self.prenume = prenume
        
    def set_post(self,post):
        self.post = post
        
    def set_inaltime(self,inaltime):
        self.inaltime = inaltime
        