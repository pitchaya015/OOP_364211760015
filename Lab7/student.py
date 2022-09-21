"""
Name: Pitchaya Musimun
ID: s364211760015
Group: MIT221
"""

class Student:
    def __init__(self,name,id):
        #attributes
        self.name = name #public member
        self.__id = id #private member
    def __str__(self):
        print(f'Name: {self.name} ID: {self.__id}')

std =Student("Pitchaya","015")
#direct access
#print(std.name, std.__id)

std.__str__()

std.name = "Panida" # change data attribute
std.__str__()

std.__id ="016"
std.__str__()

#name mangling
print(std._Student__id)

std._Student__id = "016"
std.__str__()