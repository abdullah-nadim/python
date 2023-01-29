class Car:
    car_name = 'Bee'
    def move(self):
        print(self.car_name,"is moving")

class Truck:
    truck_name = "Optimus Prime"
    def move(self):
        print(self.truck_name, 'is moving')

class Bike:
    bike_name = "Enfield"
    def move(self):
        print(self.bike_name,"is moving")


vehicles = [ Car(),Truck(),Bike()]
for vehicle in vehicles:
    vehicle.move()