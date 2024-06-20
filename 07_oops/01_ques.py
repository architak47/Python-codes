class Car:
    total_cars = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_cars += 1
    
    def get_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_definition():
        return "A car is a wheeled motor vehicle used for transportation."
    
    @property
    def model(self):
        return self.__model 
        
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"
    
    
    
# my_car = Car("Toyota", "Corolla")
# my_car.model = "nano"

# print(my_car.model)
    
    
# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

# print(my_tesla.get_brand())
# print(my_tesla.fuel_type())

# my_car = Car("Tata", "Safari")
# Car("Tata", "Nexon")
# print(my_car.general_definition())
# print(Car.general_definition())


# print(Safari.get_brand())
# print(Safari.fuel_type())

# print(Car.total_cars)





# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.brand)



class Battery:
    def battery_info(self):
        return "Battery Available"

class Engine:
    def engine_info(self):
        return "Engine Available"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")

print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())