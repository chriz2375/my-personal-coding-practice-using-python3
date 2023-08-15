class Vehicle:
    """
    Base class representing a vehicle.
    """

    vehicle_type = 'Vehicle'
    fuel_type = 'Fuel'

    def __init__(self, brand: str, model: str) -> None:
        """
        Constructor method to initialize the brand and model attributes.
        """
        self.brand = brand
        self.model = model

    def __call__(self, age: int) -> None:
        """
        Method that takes an integer age and prints a message indicating the age of the vehicle.
        """
        print(f"This {self.brand} {self.model} is {age} year(s) old.")

class Truck(Vehicle):
    """
    Subclass representing a truck.
    """

    cargo_type = "Delivery"

    def __init__(self, brand: str, model: str, cargo_capacity: int) -> None:
        """
        Constructor method to initialize the brand, model, and cargo_capacity attributes.
        """
        super().__init__(brand, model)
        self.cargo_capacity = cargo_capacity

class Car(Vehicle):
    """
    Subclass representing a car.
    """

    car_type = 'SUV'

    def __init__(self, brand: str, model: str, num_doors: int) -> None:
        """
        Constructor method to initialize the brand, model, and num_doors attributes.
        """
        super().__init__(brand, model)
        self.num_doors = num_doors

car1 = Car("Montero", "Model123", 4)
truck1 = Truck("Isuzu", "Model221", 1000)

print("The {} {} runs on {} and is {} type".format(car1.brand, car1.model, Vehicle.fuel_type, Car.car_type))
print("It has {} doors.".format(car1.num_doors))
car1(10)

print("\nThe {} {} runs on {} and is a {}".format(truck1.brand, truck1.model, Vehicle.fuel_type, Truck.cargo_type))
print("It can carry up to {} pounds.".format(truck1.cargo_capacity))
truck1(5)
