'''
Created on 4 Feb 2019

@author: Teuodor
'''
from Repository.RepoTV import RepoTvFile
from Service.ServiceTV import ServiceTv
class Consola:
    def meniu(self,cmd,serviceTv, block = []):
        if cmd == '0':
            print("Goodbye")
        elif cmd == '1':
            nume = input("Give the name: ")
            tip = input("Give the type: ")
            if tip in block:
                print("You can't delete this type of tv shows")
            else:
                serviceTv.delete(nume,tip)
        elif cmd == '2':
            nume = input("Give the name: ")
            tip = input("Give the type: ")
            durata = input("Give the time: ")
            descriere = input("Give the description: ")
            new_time = input("Give the new time: ")
            new_desc = input("Give the new description: ")
            if tip in block:
                print("You can't update this type of tv shows")
            else:
                serviceTv.update(nume,tip,durata,descriere,new_desc,new_time)
        elif cmd == '3':
            dict = serviceTv.transmission_day()
            print("Ora"+"        "+"Nume"+"            "+"Tip"+"            "+"Descriere")
            for key,value in dict.items():
                a = serviceTv.search(value)
                print(str(key)+"        "+str(a.get_nume())+"        "+str(a.get_tip())+"        "+str(a.get_descriere()))
        
        elif cmd == '4':
            blocare = input("Tipul blocat dorit: ")
            if blocare =='[]':
                block.clear()
                print("The block list was cleared")
            else:
                block.append(blocare.strip())
        else:
            print("Please write a number between 0 and 4")
    
    def run(self):
        repoTv = RepoTvFile()   
        serviceTv = ServiceTv(repoTv)
        while True:
            serviceTv.load()
            print("Please write a command(0-4). ")
            cmd = input(">>")
            self.meniu(cmd, serviceTv)  
            serviceTv.save()      
            if cmd == '0':
                break
            
con = Consola()
con.run()
                
                