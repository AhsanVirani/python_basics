# -*- coding: utf-8 -*-
"""
Created on Fri May  8 06:57:49 2020

@author: asan
"""

# Creating and instanciating classes
# Tut 1

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

'''        
# Instances of a class
emp_1 = Employee()    
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'Ahsan'
emp_1.last = 'Virani'
emp_1.email = 'ahsan.virani08@gmail.com'
emp_1.pay = 100000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.user@gmail.com'
emp_2.pay = 60000

print(emp_1.last)
print(emp_2.last)
'''

# Using the Class object to do the same thing as above
emp_1 = Employee('Ahsan', 'Virani', 100000)
emp_2 = Employee('Test', 'User', 60000)


# Making method of redundant work
print(emp_1.email)
print(emp_2.email)

# print('{} {}'.format(emp_1.first, emp_1.last))


print(emp_1.fullname())
print(emp_2.fullname())