# -*- coding: utf-8 -*-
"""
Created on Tue May 12 00:29:35 2020

@author: asan
"""

class Employee:
    
    num_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
 
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str):
         first, last, pay = emp_str.split('-')
         return cls(first, last, pay)
     
    @staticmethod
    def is_workday(day):
        if day.weekday() != 5 and day.weekday() != 6:
            return True
        return False

        
import datetime  
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))

  
emp_1 = Employee('Ahsan', 'Virani', 100000)
emp_2 = Employee('Test', 'User', 60000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

'''
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
print(new_emp_1.email)
'''
emp_3 = Employee.from_string('John-Doe-70000')
print(emp_3.first)

# Statis Methods
