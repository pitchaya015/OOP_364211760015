"""
Name: Pitchaya Musimun
ID: s364211760015
Group: MIT221
"""

# Class Relations - Dependency

from datetime import date
class Customer:
    def __init__(self,cusid,name):
        self.cusid = cusid
        self.name = name

    def customer_info(self):
        return f'CusID: {self.cusid} Customer name: {self.name}'

class Order:
    def __init__(self,orderid,date,Customer,total):
        self.orderid = orderid
        self.date = date
        self.customer = Customer
        self.total = total

    def order_info(self):
        print("Order description:")
        print(f'\tCustumer info: {self.customer.customer_info()}')
        print(f'\tDate: {self.date}')
        print(f'\tTotal cost: {self.total}')


# create object
cus1= Customer("CUS001","Pitchaya Musimun")

order1 = Order("ORDER001",date.today(),cus1,15000)

order1.order_info()