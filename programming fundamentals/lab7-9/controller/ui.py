'''
Created on 13 Nov 2018

@author: Teuodor
'''
from domain.person import Person
from domain.event import Event
from domain.assignament import Assignament
from repository.repoEvent import eventRepository
from repository.repoPerson import personRepository
from repository.repoAssign import assignamentRepository
from service.servicePerson import PersonService
from service.serviceEvent import EventService
from service.serviceAssignament import AssignamentService 
from repository import repoEvent
from domain.name_nrevent_hour import NameNrEventHour
from repoFiles.repoPersons import RepoPersFile
from repoFiles.repoEvents import RepoEventsFile
from repoFiles.repoAssignaments import RepoAssigsFile
from repoFiles.repoPersons import ExceptionRepoPersons
from repoFiles.repoEvents import ExceptionRepoEvents
from repository.repoPerson import PersonRepositoryException
from repository.repoEvent import EventRepositoryException
from domain.validari import Validare
from repository.repoAssign import AssignRepositoryException
from repoFiles.repoAssignaments import ExceptionRepoAssig
class Consola:
    def meniu(self, cmd, persService, eventService, assignService):
        if cmd.lower()=="help":
            print("These are the 5 commands you can type:")
            print("        1.Store(1p,1e)")
            print("        2.Delete(2p,2e)")
            print("        3.Update(3p,3e)")
            print("        4.Print(4p,4e)")
            print("        5.Enroll a person to an event")
            print("        6.The list of events where a person goes")
            print("        7.Exit")
            print("        8.Generate a number of random people")
            print("        9.Print all the people")
            print("        10.Print the people who goes to the biggest number of events")
            print("        11.Print 20% of the events with the most participants")
            print("        12.Print the participants who participates at most of the events which begin later than an hour")
        elif cmd == "1p":
            while True:
                id = input("Id person: ")
                nume = input("Name person: ")
                adresa = input("Adress person: ")
                try:
                    persService.createPerson(id, nume, adresa)
                    print("The person was added succesfully")
                    break
                except PersonRepositoryException as ve:
                    print(ve)
                except ExceptionRepoPersons as ve:
                    print(ve)
                except Validare as ve:
                    print(ve)
        elif cmd.lower() == "1e":
            while True:
                id = input("Id event: ")
                data = input("Date event: ")
                timp = input("Hour event: ")
                desc = input("Description event: ")
                try:
                    eventService.createEvent(id, data, timp, desc)
                    print("The event was added succesfully")
                    break
                except Validare as ve:
                    print(ve)
                except ExceptionRepoEvents as ve:
                    print(ve)
                except EventRepositoryException as ve:
                    print(ve)
        elif cmd.lower() == "2p":
            id = input("Id person: ")
            try:
                persService.deletePerson(id)
                assignService.del_person(id)
                print("The person was deleted succesfully")
            except PersonRepositoryException as ve:
                print(ve)
            except ExceptionRepoPersons as ve:
                print(ve)
        elif cmd.lower() == "2e":
            id = input("Id event: ")
            try:
                eventService.deleteEvent(id)
                assignService.del_event(id)
                print("The event was deleted succesfully")
            except EventRepositoryException as ve:
                print(ve)
            except ExceptionRepoEvents as ve:
                print(ve)
        elif cmd.lower() == "3p":
            id = input("Id person to be replaced:")
            nume = input("Name of the new person:")
            adresa = input("Adress of the new person: ")
            try:
                persService.updatePerson(id, nume, adresa)
                print("The person was updated")
            except PersonRepositoryException as ve:
                print(ve)
            except ExceptionRepoPersons as ve:
                print(ve)
            except Validare as ve:
                print(ve)
        elif cmd.lower() == "3e":
            id = input("Id event to be replaced:")
            data = input("Date of the new event: ")
            timp = input("Hour of the new event: ")
            desc = input("Description of the new event: ")
            try:
                eventService.updateEvent(id, data, timp, desc)
                print("The event was updated")
            except EventRepositoryException as ve:
                print(ve)
            except ExceptionRepoEvents as ve:
                print(ve)
            except Validare as ve:
                print(ve)
        elif cmd.lower() == "4p":
            id = input("Id person: ")
            try:
                pers = persService.search(id)
                print("ID        Name        Adress")
                print(pers.get_id() + "        " + pers.get_name()+"        " + pers.get_adr())
            except ExceptionRepoPersons as ve:
                print(ve)
            except PersonRepositoryException as ve:
                print(ve)
        elif cmd.lower() == "4e":
            id = input("Id event: ")
            try:
                event = eventService.search(id)
                print("ID        Date        Hour        Description")
                print(event.get_id() + "        " + event.get_date() + "        " + event.get_time() + "        " + event.get_desc())
            except ExceptionRepoEvents as ve:
                print(ve)
            except EventRepositoryException as ve:
                print(ve)
        elif cmd.lower() == '5':
            id_person = input("Id person: ")                
            id_event = input("Id event: ")
            list_pers=[]
            list_ev=[]
            persons=persService.get_persons()
            events=eventService.get_all_events_service()
            for k in persons:
                list_pers.append(k.get_id())
            for k in events:
                list_ev.append(k.get_id())
            if not id_person in list_pers :
                print("The person doesn't exist")
            elif not id_event in list_ev :
                print("The event doesn't exist")
            else:
                try:
                    assignService.create_assign(id_person, id_event)
                    print("The person was enrolled succesfully")
                except AssignRepositoryException as ve:
                    print(ve)
                except ExceptionRepoAssig as ve:
                    print(ve)
        elif cmd.lower() == '6':
            id_person=input("Id person: ")
            lista=eventService.sort_secv_events(assignService.get_person_enrolled(id_person))
            if len(lista)>0:
                print("ID        Date        Hour        Description")
                for event in lista:
                    print(event.get_id()+"        "+event.get_date()+"        "+event.get_time()+"        "+event.get_desc())
            else:
                print("The person is not enrolled in an event")
                
        elif cmd == "7":
            print("Goodbye")
        elif cmd == "8":
            while True:
                number = input("How many random persons do you want?")
                try:
                    number = int(number)
                    persService.get_random(number)
                    break
                except ValueError as ve:
                    print(ve)
        elif cmd=="9":
            list = persService.get_persons()
            if len(list)>0:
                print("Id        Name        Address")
                for k in list:
                    print(k.get_id()+"        "+k.get_name()+"        "+k.get_adr())
            else:
                print("We can't find any person to print")
        elif cmd == "10":
            list = assignService.get_most_participants()
            if len(list) > 0:
                print("Id        Name        Address")
                for k in list:
                    pers = persService.search(k)
                    print(pers.get_id()+"        "+pers.get_name()+"        "+pers.get_adr())
            else:
                print("We can't find assignaments")
        elif cmd == "11":
            list = assignService.first_20_percent()
            if len(list)>0:
                print("Id    Number of participants")
                for k in range(len(list)):
                    print(str(list[k][0])+"    "+str(list[k][1]))
            else:
                print("We can't find assignaments")
        elif cmd == "12":
            v = input("Choose an hour(HH:MM): ")
            try:
                dict = assignService.mostEvents(eventService.more_than_v(v))
                list = assignService.name_nr_hour(dict, persService, v)
                for k in list:
                    print("Persoana " + k.get_name() + " participa la " + str(k.get_nr()) + " evenimente care au ora mai mare decat " + str(k.get_hour()))
            except:
                print("Please respect the time format")
    def run(self):
        while True:
            cmd=input("Choose memory or files(m/f): ")
            if cmd=='m':
                repoPers = personRepository()
                persService = PersonService(repoPers)
                repoEvents = eventRepository()
                eventService = EventService(repoEvents)
                repoAssign = assignamentRepository()
                assignService = AssignamentService(repoAssign)
                while True:
                    print("Please write a command")
                    cmd=input(">>")
                    self.meniu(cmd,persService,eventService,assignService)
                    if cmd=="7":
                        break
                break
            elif cmd=='f':
                repoPers = RepoPersFile()
                repoPers.load()
                repoPers.save()
                persService = PersonService(repoPers)
                repoEvents = RepoEventsFile()
                repoEvents.load()
                repoEvents.save()
                eventService = EventService(repoEvents)
                repoAssign = RepoAssigsFile()
                repoAssign.load()
                repoAssign.save()
                assignService = AssignamentService(repoAssign)
                while True:
                    persService.load()
                    eventService.load()
                    assignService.load()
                    print("Please write a command")
                    cmd=input(">>")
                    self.meniu(cmd,persService,eventService,assignService)
                    persService.save()
                    eventService.save()
                    assignService.save()

                    if cmd=="7":
                        break
                break
            else:
                print("You must type m or f")
                
con=Consola()
con.run()