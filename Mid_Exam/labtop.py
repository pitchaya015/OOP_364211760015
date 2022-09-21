"""
นางสาวพิชญา มูสิมูล 364211760015 MIT221
"""
class labtop:
    my_labtop=[]
    def __init__(self, no, brand, model, cpu, ram, display, storage, price): #สร้าง Object ของคลาส
        self.no = no
        self.brand = brand
        self.model = model
        self.cpu = cpu
        self.ram = ram
        self.display = display
        self.storage = storage
        self.price = price
        self.my_labtop.append(self)

    def display_labtop(self): #แสดงข้อมูลของ Object ของคลาส Labtop
        print(f'No:{self.no} '
              f'Brand:{self.brand} '
              f'Model:{self.model} '
              f'CPU:{self.cpu} '
              f'RAM(GB):{self.ram} '
              f'Display(inch):{self.display} '
              f'Storage(GB):{self.storage} '
              f'Price:{self.price} ')