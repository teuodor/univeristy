class Person:
    '''
    Class which define the person object defined by
    id, name and address - all strings
    '''
    def __init__(self, id_pers, name, address):
        self.__id = id_pers
        self.__name = name
        self.__address = address
        
    def get_id(self):
        '''
        The function returns the current person's id
        :return: a string id
        '''
        return self.__id
    
    def get_name(self):
        '''
        The function returns the current person's name
        :return: a string name
        '''
        return self.__name
    
    def get_adr(self):
        '''
        The function returns the current person's adress
        :return: a string adress
        '''
        return self.__address
    
    def set_id(self,id1):
        '''
        The function sets the current person's id
        :param: id
        :post: the id will be set
        '''
        self.__id=id1
        
    def set_name(self,name):
        '''
        The function sets the current person's name
        :param: name
        :post: the name will be set
        '''
        self.__name=name
        
    def set_adress(self,adress):
        '''
        The function sets the current person's adress
        :param: adress
        :post: the adress will be set
        '''
        self.__address=adress
        
    def __eq__(self, other):
        '''
        Tells if two person objects are equal
        '''
        return self.get_id()==other.get_id()
    
    
    