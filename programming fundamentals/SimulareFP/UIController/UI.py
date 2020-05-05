'''
Created on 13 Dec 2018

@author: Teuodor
'''
from Service import FilmsService
from Service.FilmsService import FilmService
from Repository.FilmsRepository import RepositoryFilms
class Consola:
    def UI(self,cmd,servFilm):
        if cmd == "1a":
            Str=input("Type a string: ")
            list = servFilm.FilmsBeginningWithStrN(Str)
            if len(list)>0:
                print("ID        Title        Price        Number of reserved seats")
                for k in list:
                    film = servFilm.search(k[1])
                    print(film.get_id()+"        "+film.get_title()+"        "+film.get_price()+"        "+film.get_nr())
            else:
                print("We couldn't find films beginning with "+Str)
        if cmd == "1b":
            Str=input("Type a string: ")
            list = servFilm.FilmsBeginningWithStrT(Str)
            if len(list)>0:
                print("ID        Title        Price        Number of reserved seats")
                for k in list:
                    film = servFilm.search(k[1])
                    print(film.get_id()+"        "+film.get_title()+"        "+film.get_price()+"        "+film.get_nr())
            else:
                print("We couldn't find films beginning with "+Str)
        if cmd == "2":
            list = servFilm.PopularFilms()
            if len(list)>0:
                print("ID        Title        Price        Number of reserved seats")
                for k in list:
                    print(k.get_id()+"        "+k.get_title()+"        "+k.get_price()+"        "+k.get_nr())
        if cmd == "3":
            while True:
                price=input("Type a price: ")
                try:
                    price=int(price)
                    servFilm.Discount(price)
                    break
                except ValueError:
                    print("Please type a number")
                    
    def run(self):
        while True:
            print("Please write a command ")
            cmd = input(">>")
            repoFilms=RepositoryFilms()
            servFilm=FilmService(repoFilms)
            servFilm.load()
            self.UI(cmd, servFilm)
            servFilm.save()
            if cmd == "4":
                print("Goodbye")
                break