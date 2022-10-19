"""
Name: Pitchaya Musimun
ID: s364211760015
Group: MIT221
"""

# Class Relation - Aggreation
class Teacher:
    def __init__(self,name):
        self.name = name

    def teacher_info(self):
        print(f'Teacher name: {self.name}')

class Faculty:
    # class attribute
    lst_teacher = list()

    def __init__(self,fac_name):
        self.fac_name = fac_name
    def fac_info(self):
        print(f'Faculty name: {self.fac_name}')
    def add_teacher(self,Teacher):
        self.lst_teacher.append(Teacher)
    def teacher_info(self):
        print(f'Faculty: {self.fac_name} has teacher following:')
        if len(self.lst_teacher) ==0:
            print("No teacher.")
        else:
            for x in self.lst_teacher:
                x.teacher_info()

#create object
t1 = Teacher("Puriwat")
t2 = Teacher("Pornprasert")

f1 = Faculty("MT")

t1.teacher_info()
f1.fac_info()

f1.add_teacher(t1)
f1.add_teacher(t2)
f1.teacher_info()

del f1

t1.teacher_info()