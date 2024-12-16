class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def get_info(self):
        return f"Vehicle make: {self.make}, model: {self.model}"
class Car (Vehicle):
    def __init__(self,make, model, fuel_type):
        super().__init__(make=make,model=model)
        self.fuel_type = fuel_type
    def get_info(self):
        super().get_info()
        return f"Car Make: {self.make} ,Model: {self.model}, Fuel_Type:{self.fuel_type} "
    vehicle = Vehicle("Carl Benz", "S")
    print(vehicle.get_info())
car = Car("Mercedes" , "S" , "Petrol")
print(car.get_info())