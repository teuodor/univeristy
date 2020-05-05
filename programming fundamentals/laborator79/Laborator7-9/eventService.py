from domain import Events
class EventService:
    def __init__(self,repo):
        self.__rep=repo
    def createEvent(self,IdEvent,date,time,desc):
        event=Events(IdEvent,date,time,desc)
        self.__rep.store(event)
        return event
    def delEvent(self,IdEvent):
        if event.__id in self.__rep:
            del event
        else:
            print("Nu exista id-ul evenimentului")
    def 
