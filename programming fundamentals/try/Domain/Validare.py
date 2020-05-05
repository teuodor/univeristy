'''
Created on 3 Feb 2019

@author: Teuodor
'''
class ExceptValJuc(Exception):
    pass
class ValidareJuc:
    def validare(self,juc):
        exceptions = []
        if juc.nume == "":
            exceptions.append("Numele nu poate fi gol")
        if juc.prenume == "":
            exceptions.append("Prenumele nu poate fi gol")
        if juc.post == "":
            exceptions.append("Postul nu poate fi gol")
        elif not juc.post == "extrema" or juc.post.lower() == "fundas"or juc.post.lower() == "pivot":
            exceptions.append("Postul poate fi doar Extrema, Fundas, Pivot")
            
        if juc.inaltime == "":
            exceptions.append("Inaltimea nu poate fi goala")
        else:
            try:
                juc.inaltime = int(juc.inaltime)
            except:
                exceptions.append("Inaltimea trebuie sa fie un numar pozitiv")
            
            if juc.inaltime>0:
                exceptions.append("Inaltimea trebuie sa fie un numar pozitiv")
       
        if len(exceptions)>0:
            raise ExceptValJuc("".join(str(x) for x in exceptions))
            
            
            
            
            