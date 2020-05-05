from ui import *
from functionalitati import *
from getset import createComplex
from undo import undoLista,copyLista
def help():
    print('Meniul de comenzi al programului:')
    print('help-afisarea meniului;')
    print('a-adauga un element in lista')
    print('inserare-insereaza un element pe o pozitie data')
    print('stergePozitie-sterge elementul de pe o pozitie data')
    print('stergeInterval-sterge elementele dintre 2 pozitii date')
    print('inlocuire-inlocuieste aparitia unui element cu un alt element dat')
    print('afisare-tipareste toate elementele din lista')
    print('afisare1-tipareste toate elementele din lista care au modulul mai mic ca 10;')
    print('afisare2-tipareste toate elementele din lista care au modulul egal cu 10;')
    print('afisare3-tipareste elementele in ordine descrescatoare dupa partea lor imaginara;')
    print('afisareImag-tipareste partea imaginara a elementelor din lista intre doua pozitii date')
    print('suma-tipareste suma unei subsecvente din lista de numere complexe')
    print('produs-tipareste produsul unei subsecvente din lista de numere complexe')
    print('modulMic-sterge elementele din lista care au modulul mai mic decat un numar dat')
    print('modulEgal-sterge elementele din lista care au modulul egal cu un numar dat')
    print('modulMare-sterge elementele din lista care au modulul mai mare decat un numar dat')
    print('realPrim-sterge elementele din lista care au partea reala prima')
    print('undo-reface ultima operatie efectuata')
    print('grupare-grupeaza elementele dupa valoarea modulului lor')
    print('exit-iesire din program')
    
def meniu(cmd,lista,undol):
    if cmd.lower()=='help':
        help()
    elif cmd.lower()=='a':
        lista2=copyLista(lista)
        undol.append(lista2)
        ok=False
        while ok==False:
            x=input('Partea reala a numarului:')
            try:
                x=int(x)
                y=input('Partea imaginara a numarului:')
                try:
                    y=int(y)
                    elem=createComplex(x,y)
                    adaugaLista(lista,elem)
                    ok=True
                except:
                    print('Va rugam sa puneti numere')
            except:
                print('Va rugam sa puneti numere')
    elif cmd.lower()=='stergepozitie':
        lista2=copyLista(lista)
        undol.append(lista2)
        ok=False
        while ok==False:
            poz=input('Pozitia de stergere:')
            try:
                poz=int(poz)
                stergePozitieLista(lista,poz)
                ok=True
            except:
                print('Va rugam sa puneti numere sau pozitii existente')
    elif cmd.lower()=='stergeinterval':
        lista2=copyLista(lista)
        undol.append(lista2)
        ok=False
        while ok==False:
            poz1=input('Pozitia de inceput de stergere:')
            try:
                poz1=int(poz1)
                poz2=input('Pozitia de sfarsit de stergere:')
                try:
                
                    poz2=int(poz2)
                    poz2=input('Pozitia de sfarsit de stergere:')
                    stergeIntervalLista(lista,poz1,poz2)
                    ok=True
                except:
                    print('Va rugam sa puneti numere sau pozitii existente')
            except:
                print('Va rugam sa puneti numere sau pozitii existente')
    elif cmd.lower()=='inlocuire':
        lista2=copyLista(lista)
        undol.append(lista2)
        ok=False
        while ok==False:
            a=input('Partea reala(de inlocuit):')
            try:
                a=int(a)
                b=input('Partea imaginara(de inlocuit):')
                try:
                    b=int(b)
                    c=input('Partea reala:')
                    try:
                        c=int(c)
                        d=input('Partea imaginara:')
                        try:
                            d=int(d)
                            x=createComplex(a, b)
                            y=createComplex(c, d)
                            inlocuiesteElementLista(lista,x,y)
                            ok=True
                        except:
                            print('Va rugam sa puneti numere')
                    except:
                        print('Va rugam sa puneti numere')
                except:
                    print('Va rugam sa puneti numere')
            except:
                print('Va rugam sa puneti numere')
    elif cmd.lower()=='inserare':
        lista2=copyLista(lista)
        undol.append(lista2)
        ok=False
        while ok==False:
            x=input('Partea reala a numarului:')
            try:
                x=int(x)
                y=input('Partea imaginara a numarului:')
                try:
                    y=int(y)
                    poz=input('Pozitia de inserare:')
                    try:
                        poz=int(poz)
                        elem=createComplex(x,y)
                        inserareLista(lista,poz,elem)
                        ok=True
                    except:
                        print('Va rugam sa puneti numere')
                except:
                    print('Va rugam sa puneti numere')
            except:
                print('Va rugam sa puneti numere')
    elif cmd.lower()=='afisare':
        afisareLista(lista)
    elif cmd.lower()=='afisare1':
        tiparireElemente1(lista)
    elif cmd.lower()=='afisare2':
        tiparireElemente2(lista)
    elif cmd.lower()=='afisare3':
        tiparireElementeDesc(lista)
    elif cmd.lower()=='afisareimag':
        ok=False
        while ok==False:
            poz1=input('Pozitia de inceput:')
            try:
                poz1=int(poz1)
                poz2=input('Pozitia de final:')
                try:
                    poz2=int(poz2)
                    afisareImaginar(lista, poz1, poz2)
                    ok=True
                except:
                    print('Va rugam sa alegeti pozitii numere naturale sau pozitii existente in lista')
            except:
                print('Va rugam sa alegeti pozitii numere naturale sau pozitii existente in lista')
        afisareImaginar(lista)
    elif cmd.lower()=='suma':
        ok=False
        while ok==False:
            poz1=input('Pozitia de inceput:')
            try:
                poz1=int(poz1)
                poz2=input('Pozitia de final:')
                try:
                    poz2=int(poz2) 
                    print(formaComplex(sumaSubsecventa(lista,poz1,poz2)))
                    ok=True
                except:
                    print('Va rugam sa alegeti pozitii numere naturale sau pozitii existente in lista')
            except:
                print('Va rugam sa alegeti pozitii numere naturale sau pozitii existente in lista')  
    elif cmd.lower()=='produs':
        ok=False
        while ok==False:
            poz1=input('Pozitia de inceput:')
            try:
                poz1=int(poz1)
                poz2=input('Pozitia de final:')
                try:
                    poz2=int(poz2)
                    print(formaComplex(produsSubsecventa(lista,poz1,poz2)))
                    ok=True
                except:
                    print('Va rugam sa alegeti pozitii numere naturale sau pozitii existente in lista')  
            except:
                print('Va rugam sa alegeti pozitii numere naturale sau pozitii existente in lista')  
    elif cmd.lower()=='realprim':
        lista2=copyLista(lista)
        undol.append(lista2)
        filtrareRealPrim(lista)
    elif cmd.lower()=='modulmic':
        lista2=copyLista(lista)
        undol.append(lista2)
        ok=False
        while ok==False:
            k=input('Alegeti un numar:')
            try:
                k=int(k)
                modulMaiMic(lista,k)
                ok=True
            except:
                print('Va rugam sa alegeti numere!')
    elif cmd.lower()=='modulegal':
        lista2=copyLista(lista)
        undol.append(lista2)
        ok=False
        while ok==False:
            k=input('Alegeti un numar:')
            try:
                k=int(k)
                modulEgal(lista,k)
                ok=True
            except:
                print('Va rugam sa alegeti numere!')
    elif cmd.lower()=='modulmare':
        lista2=copyLista(lista)
        undol.append(lista2)
        ok=False
        while ok==False:
            k=input('Alegeti un numar:')
            try:
                k=int(k)
                modulMaiMare(lista,k)
                ok=True
            except:
                print('Va rugam sa alegeti numere!')
    elif cmd.lower()=='grupare':
        tiparireGrupare(lista)
    elif cmd.lower()=='undo':
        if len(undol)<1:
            print('Nu se poate')
        else:
            lista=copyLista(undoLista(lista,undol))
    elif cmd.lower()=='exit':
        print('La revedere!')
    else:
        print('Comanda invalida!')
    
    
    