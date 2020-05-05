'''
Created on 13 Dec 2018

@author: Teuodor
'''
class FilmService:
    def __init__(self,FilmRepo):
        self.__rep=FilmRepo
        
    def load(self):
        self.__rep.load()
        
    def save(self):
        self.__rep.save()
    def FilmsBeginningWithStrT(self,Str):
        '''
        A function that returns a list of films which title begin with a string
        :param Str: the string
        :return: a matrix where list[0]-title of film, list[1]-id of the film
        '''
        list = []
        repo=self.__rep.get_all_films()
        for k in repo.values():
            if k.get_title().startswith(Str):
                list.append([k.get_title(),k.get_id()])
                
        list = sorted(list, key=lambda x : x[0])
        
        return list
    
    def FilmsBeginningWithStrN(self,Str):
        '''
        A function that returns a list of films which title begin with a string
        :param Str: the string
        :return: a matrix where list[0]-price*number, list[1]-id of the film
        '''
        list = []
        repo=self.__rep.get_all_films()
        for k in repo.values():
            if k.get_title().startswith(Str):
                number=int(k.get_nr())
                price=k.get_price()
                list.append([number*price,k.get_id()])
                
        list = sorted(list, key=lambda x : x[0])
        
        return list
    
    def PopularFilms(self):
        '''
        A function which return a list of films which have the number bigger than the number/number of films
        :return: a list of films
        '''
        media=0
        suma=0
        nr=0
        list=[]
        repo=self.__rep.get_all_films()
        for k in repo.values():
            number = int(k.get_nr())
            suma+=number
            nr+=1
            
        media = suma/nr
        
        for k in repo.values():
            number =  int(k.get_nr())
            if number>media:
                list.append(k)
                
        return list
    
    def Discount(self,price1):
        '''
        A function which makes all the prices that are above price1 smaller with 15%
        :param: price1
        :post: all the prices are lowered 
        '''
        repo=self.__rep.get_all_films()
        for k in repo.values():
            price2 = int(k.get_price())
            if price2>=price1:
                price2=price2-(price2*0.15)
                k.set_price(str(price2))
        self.__rep.__repo = repo
    def search(self,id):
        '''
        A function that search for film by its id
        :param: id
        :return: the film with the specific id
        '''
        return self.__rep.search(id)
        