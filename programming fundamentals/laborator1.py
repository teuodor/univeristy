import datetime
currentDate=datetime.date.today()
ok=1
while ok==1:
    nastere=input('Scrieti data nasterii (DD/MM/YYYY) : ')
    nastere=datetime.datetime.strptime(nastere,"%d/%m/%Y").date()
    varsta=currentDate-nastere
    print(varsta.days)
    ok=input('Doriti sa mai continuati? 1/0 ')
    ok=int(ok)

