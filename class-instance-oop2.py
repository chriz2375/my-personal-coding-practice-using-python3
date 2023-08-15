"""
Coding Challenge: Vehicle System

You are tasked with creating a Python class system for vehicles. The system should have the following features:

1. Create a base class called Vehicle with the following attributes and methods:

    *Attributes:
        vehicle_type (class attribute): A string representing the type of the vehicle (e.g., "Car", "Truck").
        fuel_type (class attribute): A string representing the type of fuel the vehicle 
        runs on (e.g., "Gasoline", "Diesel").
    brand (instance attribute): A string representing the brand of the vehicle.
    model (instance attribute): A string representing the model of the vehicle.

    *Methods:
        __init__(self, brand: str, model: str): Constructor method to initialize the brand 
        and model attributes.
        __call__(self, years_old): Method that takes an integer years_old and 
        prints a message indicating the age of the vehicle.

2. Create two subclasses of Vehicle:

    *Car: This subclass should have an additional instance attribute num_doors (number of doors) 
    and a class attribute car_type (e.g., "Sedan", "SUV").
    *Truck: This subclass should have an additional instance attribute cargo_capacity
    (maximum cargo capacity in pounds) and a class attribute truck_type (e.g., "Pickup", "Delivery").
    Your task is to implement the Vehicle, Car, and Truck classes as described above. 
    Then, create instances of each class and demonstrate the following:

Creating objects with appropriate attributes.
Accessing class and instance attributes.
Calling the instances to display their age.

Feel free to create additional methods or attributes if you think they would enhance the system. Good luck!
"""

from typing import Any


class Vehicle:

    # class attributes
    vehicle_type = 'Car'
    fuel_type = 'Diesel'

    # instance attributes

    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model

    def __call__(self, age: int) -> None:
        print(f'This car {self.brand} is {age} year/s old')

class Truck(Vehicle):

    # creating additional class 
    cargo_type = "Delivery"

    # creating additional instance attribute
    def __init__(self, brand: str, model: str, cargo_cap: int) -> None:
        super().__init__(brand, model)
        self.cargo_cap = cargo_cap

class Car(Vehicle):
    
    # creating additional class attribute
    car_type = 'SUV'

    # creating addtional instance attribute
    def __init__(self, brand: str, model: str, no_of_doors: int) -> None:
        super().__init__(brand, model)
        self.no_of_doors = no_of_doors
    

car1 = Car("Montero", "Model123", 6)

truck1 = Truck("Isuzu", "Model221", 500)


print("The vehicle1 is a {} vehicle type that fuels only {}".format(car1.__class__.vehicle_type, car1.__class__.fuel_type))
print("This vehicle is a brand of {} model {} and has {} no of doors".format(car1.brand, car1.model, car1.no_of_doors))
print("Also, this car type is {}".format(car1.__class__.car_type))
car1(10)

# print("The vehicle2 is a {} vehicle type that fuels only {}".format(truck1.__class__.))
print("\nThe vehicle2 is a {} vehicle type that fules only {}".format(truck1.__class__.vehicle_type, truck1.__class__.fuel_type))
print("This vehicle is a brand of {} model {} and has a weight capacity of {} pounds".format(truck1.brand, truck1.model, truck1.cargo_cap))
print("Also, this truck type is {}".format(truck1.__class__.cargo_type))
truck1(25)

print("Hello world! , this is a test to see how git works when some code are changes! ")