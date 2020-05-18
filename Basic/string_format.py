person = {'name':'Jenn', 'age':23}

sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print(sentence)
print(person['age'])

sentence_1 = 'My name is {0} and I am {1} years old'.format(person['name'], person['age'])
print(sentence_1)

sentence_1 = 'My name is {1} and I am {0} years old'.format(person['name'], person['age'])
print(sentence_1)

sentence_1 = 'My name is {0} and I am {0} years old'.format(person['name'])
print(sentence_1)

# Working with class

class person():

	def __init__(self, name, age):
		self.name = name
		self.age = age

p1 = person('Ahsan', 22)
sentence =  'My name is {0.name} and I am {0.age} years old'.format(p1)
print(sentence)

sentence = 'My name is {name} and I am {age} years old'.format(name = 'Faiz', age = 30)
print(sentence)

print('{:.2f}'.format(3.142))

import datetime as dt 

my_date = dt.datetime(1998, 9, 23, 12, 00, 00, 00)
print(my_date)

sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

sentence = '{0:%B %d, %Y} fell on {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)