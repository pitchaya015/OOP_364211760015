"""
Name: Pitchaya Musimun
ID: s364211760015
Group: MIT221
"""

from labtop import labtop

def display_laptop(): #แสดงข้อมูล laptop
    if len(my_labtop) == 0:
        print("คุณยังไม่มีรายการ")
    else:
        num = 1
        print(f'คุณมีรายการ {len(my_labtop)} จำนวน:')
        for x in my_labtop:
            print(f'{num}. ',end="")
            x.display_labtop()
            num +=1
        print("\n")

def display_option_system(): #แสดงตัวเลือกให้ผู้ใช้เลือกใช้ฟังก์ชั่น
    print("Welcome to Labtop Store System")
    print("1.Add Labtop")
    print("2.Display Laptop")
    print("3.Delete Laptop")
    print("4.Edit Laptop")
    print("5.Exit")
    select = int(input("กรุณาเลือกตัวเลข 1-5?: "))
    if select == 1:
        input_laptop_data()
    elif select == 2:
        display_laptop()
    elif select == 3:
        delete_laptop()
    elif select == 4:
        edit_labtop_price()
    elif select == 5:
        print("ขอบคุณที่ใช้บริการค่ะ")
        exit(0)
    else:
        print("******************************")
        print("กรุณาเลือกตัวเลข 1-5 ด้วยค่ะ")
        print("******************************")
        print("\n")
def edit_labtop_price():
    print("Which one do you want to edit price?: ")
    display_laptop()
    n = len(my_labtop)
    s = 1
    while s:
        s = int(input(f"select(1-{n}) or type 0 to main options:?"))
        if s in range(1, n + 1):
            print(f'old price: {my_labtop[s-1].get_price()}')
            newprice = float(input("Enter new price: "))
            my_labtop[s-1].set_price(newprice)
            print("\nLaptop price update. \n")
            break
        elif s == 0:
            break
        else:
            print(f"Please, select number 1-{n} or type 0 to main options.")

# delete data
def delete_laptop():
    print("Which one do you want to remove?: ")
    display_laptop()
    n = len(my_labtop)
    s = 1
    while s:
        s = int(input(f"select(1-{n}) or type 0 to main options:?"))
        if s in range(1,n+1):
            my_labtop.pop(s-1)
            print("\nAlready delete laptop data. \n")
            break
        elif s ==0:
            break
        else:
            print(f"Please, select number 1-{n} or type 0 to main options.")

def input_laptop_data(): #รับข้อมูล
    brand = input("Enter Labtop Brand: ")
    model = input("Enter Labtop Model: ")
    cpu = input("Enter Labtop CPU: ")
    ram = int(input("Enter Labtop RAM(GB): "))
    display = float(input("Enter Labtop Display(inch): "))
    storage = int(input("Enter Labtop Storage(GB): "))
    price = float(input("Enter Labtop Price: "))

    l = labtop("","","",0,0,0,0)


    l.set_brand(brand)
    l.set_model(model)
    l.set_cpu(cpu)
    l.set_ram(ram)
    l.set_display(display)
    l.set_storage(storage)
    l.set_price(price)
    #return brand, model, cpu, ram, display, storage, price #return as tuple
    #my_labtop.append(labtop(brand, model, cpu, ram, display, storage, price))
    my_labtop.append(l)
    print("******************************")
    print("เพิ่มสินค้าเรียบร้อยแล้วค่ะ")
    print("******************************")
    print("\n")

my_labtop = []
my_labtop.append(labtop("ASUS","Vivobook15X","Intel Corei5-12500H","8","15.6","512","27990"))
my_labtop.append(labtop("Lenovo","IdeaPad Gaming3","Intel Corei5-11320H","8","15.6","512","25990"))
#my_labtop.append(labtop(Acer,Swift3,Intel Corei7-1260P,8,14,512,33990))
s = 0
while s == 0:
    display_option_system()

