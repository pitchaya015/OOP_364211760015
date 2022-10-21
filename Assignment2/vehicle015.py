"""
Student Name: Pitchaya Musimun
ID: 364211760015
Grop: MIT221

"""

from Vehicle import Vehicle

Vehicle_store = []
num = int(input('คุณมีรถกี่คัน :'))

for x in range(num):
    brand = input('ยี่ห้อรถ:')
    model = input('รุ่นรถ:')
    color = input('สีรถ:')
    max_speed = input('ความเร็วสูงสุด:')
    price = float(input('ราคา:'))

    car = Vehicle(brand,model,color,max_speed,price)
    Vehicle_store.append(car)
print("*******************")
def display_Vehicle(Vehicle):
    print('จำนวนรถทั้งหมด:',len(Vehicle))
    for x in Vehicle:
        x.Vehicle_detail()

display_Vehicle(Vehicle_store)

class Vehicle:
    def __init__(self,brand,model,color,max_speed,price):
        # object attributes
        self.brand = brand
        self.model = model
        self.color = color
        self.max_speed = max_speed
        self.price = price

    def Vehicle_detail(self):
        print(f'brand: {self.brand} model: {self.model} '
              f'color: {self.color} max_speed: {self.max_speed} price: {self.price} THB')
print("*******************")
