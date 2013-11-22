database={}

def addToDictionary(key, value):
	update={key:value}
	database.update(update)

i=0

while i < 3:
	name=raw_input("name? ")
	age=raw_input("age? ")
	addToDictionary(name, age)	
	i += 1


print database

