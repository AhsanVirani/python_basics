# -*- coding: utf-8 -*-
"""
Created on Tue May 12 05:28:56 2020

@author: asan
"""


class Person(object):
    
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        
    def print_name(self):
        print(self.name)
        
    

ahsan = Person("Ahsan", "transgender")

ahsan.print_name()

Person.print_name(ahsan)