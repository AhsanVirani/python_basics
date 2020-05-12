# -*- coding: utf-8 -*-
"""
Created on Tue May 12 00:29:35 2020

@author: asan
"""

class Employee:

    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
 
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    

class Developer(Employee):
    raise_amount = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang
        

class Manager(Employee):
     def __init__(self, first, last, pay, employees = None):
        Employee.__init__(self, first, last, pay) 
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
     def add_emp(self, emp):
            if emp not in self.employees:
                self.employees.append(emp)
                
     def rem_emp(self, emp):
            if emp in self.employees:
                self.employees.remove(emp)
                
     def check_emp(self):
            for emp in self.employees:
                print('-->', emp.fullname())
                


dev_1 = Developer('Ahsan', 'Virani', 50000, 'Python')
print(dev_1.email)  
dev_2 = Developer('Test', 'User', 70000, 'Java')
print(dev_2.prog_lang)   

print(dev_1.fullname())
dev_1.apply_raise()
print(dev_1.pay)

# Working with Managers now

man_1 = Manager('Faiz', 'Ather', 70000, [dev_1])
print(man_1.email)

man_1.add_emp(dev_2)
man_1.rem_emp(dev_1)
man_1.check_emp()

print(isinstance(man_1, Manager))
print(isinstance(man_1, Employee))
print(isinstance(man_1, Developer))

print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Employee, Developer))