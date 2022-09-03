from re import S
from telnetlib import SE


class myStudent: 

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self. gpa = gpa
        self.is_on_probation = is_on_probation
    
    def __str__(self):
        return self.name + self.gpa + self.is_on_probation
