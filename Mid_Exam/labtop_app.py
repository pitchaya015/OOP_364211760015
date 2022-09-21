"""
นางสาวพิชญา มูสิมูล 364211760015 MIT221
"""
from labtop import labtop

def display_laptop(): #แสดงข้อมูล laptop
    if len(my_labtop) == 0:
        print("คุณยังไม่มีรายการ")
    else:
        print(f'คุณมีรายการ {len(my_labtop)} จำนวน:')
        for x in my_labtop:
            x.display_labtop()
        print("\n")

def display_option_system(): #แสดงตัวเลือกให้ผู้ใช้เลือกใช้ฟังก์ชั่น
    print("Welcome to Labtop Store System")
    print("1.เพิ่มข้อมูล Labtop")
    print("2.แสดงข้อมูล Laptop")
    print("3.ออกจากระบบ")
    select = int(input("กรุณาเลือกตัวเลข 1-3?: "))
    if select == 1:
        input_laptop_data()
    elif select == 2:
        display_laptop()
    elif select == 3:
        print("ขอบคุณที่ใช้บริการค่ะ")
        exit(0)
    else:
        print("******************************")
        print("กรุณาเลือกตัวเลข 1-3 ด้วยค่ะ")
        print("******************************")
        print("\n")

def input_laptop_data(): #รับข้อมูล
    no = int(input("No: "))
    brand = input("Enter Labtop Brand: ")
    model = input("Enter Labtop Model: ")
    cpu = input("Enter Labtop CPU: ")
    ram = int(input("Enter Labtop RAM(GB): "))
    display = float(input("Enter Labtop Display(inch): "))
    storage = int(input("Enter Labtop Storage(GB): "))
    price = float(input("Enter Labtop Price: "))

    #return no, brand, model, cpu, ram, display, storage, price #return as tuple
    my_labtop.append(labtop(no, brand, model, cpu, ram, display, storage, price))
    print("******************************")
    print("เพิ่มสินค้าเรียบร้อยแล้วค่ะ")
    print("******************************")
    print("\n")

my_labtop = []
l = 0
while l == 0:
    display_option_system()

