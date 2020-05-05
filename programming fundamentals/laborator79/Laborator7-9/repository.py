from domain import Persons
from validatons import *
class personRepository:
	def __init__():
		self.person={}
	def store(self,pers):
		if pers.get_id() in self.person:
			raise ValueError("A person with this id exist")
		if self.errors!=None:
			ValidarePersons.validare(pers)
