"""
Name: Pitchaya Musimun
ID: s364211760015
Group: MIT221
"""

from model import Person,Student,Vaccine,Vaccine_Passport

p1 = Person("Pitchaya",23,85.0,166)

v1 = Vaccine("Sinovac")
d1 = "2/11/2564"

vp1 = Vaccine_Passport(p1)

vp1.vaccine_passport_info()

vp1.add_vaccine(v1)
vp1.add_date(d1)

vp1.vaccine_passport_info()

v2 = Vaccine("Astrazeneca")
d2 = "2/12/2564"

vp1.add_vaccine(v2)
vp1.add_date(d2)
vp1.vaccine_passport_info()

s1 = Student("Panida",21,65.0,167,"MIT")

v3 = Vaccine("Pfizer")
d3 = "9/12/2565"

vp2 = Vaccine_Passport(s1)
vp2.add_vaccine(v3)
vp2.add_date(d3)

vp2.vaccine_passport_info()