from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models import F
from .models import Person
import asyncio

async def acreate_person(f_n, l_n):
	person = await Person.objects.acreate(first_name=f_n, last_name=l_n)

async def abulk_create_people(peoples):
	people = await Person.objects.abulk_create([Person(first_name=i[0], last_name=i[1]) for i in range(peoples.items())])

async def get_person():
	try:
		tom = Person.objects.aget(name="Tom")    # MultipleObjectsReturned
		alex = Person.objects.aget(name="Alex")  # ObjectDoesNotExist
	except ObjectDoesNotExist:
		print("Объект не сушествует")
	except MultipleObjectsReturned:
		print("Найдено более одного объекта")

def get_people():
	return Person.objects.all();

def update_person(person):
	person.save(update_fields=["first_name"])

def update_person(id, f_n, l_n, cs):
	result = Person.objects.filter(id=id).update(first_name = f_n,, last_name=l_n,course = cs)

def update_people(plus):
	result = Person.objects.all().update(age = F("age")+1)