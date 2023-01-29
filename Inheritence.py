class smartdevice:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def recharge(self):
        print("Eating Electricity")
        print("Electricity is Yummy!")

class Watch(smartdevice):
    def __init__(self,brand,price,has_gps):
        smartdevice.__init__(self,brand ,price)
        self.steps_count= 0
        self.has_gps = has_gps
class Phone(smartdevice):
    def __init__(self,brand,price,network):
        smartdevice.__init__(self,brand,price)
        self.network = network

my_watch=Watch("Fitbit",2200,False)
print(my_watch.brand)
my_watch.recharge()
my_phone = Phone("Nokia",22999,True)
print(my_phone.brand)
my_phone.recharge()