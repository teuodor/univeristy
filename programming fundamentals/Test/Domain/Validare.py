'''
Created on 12 Dec 2018

@author: Teuodor
'''
from copy import deepcopy
class Validare(Exception):
    pass

class ValidatorTelefoane():
    def validare(self, phone):
        errors=[]
        if phone.__id == "" :
            errors.append("The phone's id can't be empty ")
        if phone.__name == "" :
            errors.append("The phone's model name can't be empty ")
        else:
            if not (any(x.isalpha() for x in phone.__name) and 
            any(x.isspace() for x in phone.__name) and
            all(x.isalpha() or x.isspace() for x in phone.__name)):
                errors.append("The phone's name must contain only spaces and letters")
        if phone.__char == "" :
            errors.append("The phone's characteristics can't be empty ")
        if phone.__price == "" :
            errors.append("The phone's price can't be empty ")
        else:
            try:
                phone.set_price(int(phone.__price))
            except:
                errors.append("The price must be a number")
        
        if len(errors)>0:
            raise Validare("".join(str(x) for x in errors))
        