from typing import Any


class Dog:
    # class attribute
    attr1 = "Mammal"        
    breed = "Aspine"

    # instance attribute
    def __init__(self, name: str) -> None:
        self.name = name

    def __call__(self, arg) -> Any:
        print(f'{self.name} is a {arg} years old dog')

# creating object   
dog1 = Dog("Thunder")
dog2 = Dog("Summer")

# accessing class and instance attribute
print("Hi! I'm {}, aw aw!".format(dog1.name))
print("He is a {}".format(dog1.__class__.attr1) + " and a breed type of {}".format(dog1.__class__.breed))
dog1(5)

print("\nHi! I'm {} aw aw!".format(dog2.name))
print("He is a {}".format(dog2.__class__.attr1) + " and a breed type of {}".format(dog2.__class__.breed))
dog2(10)

