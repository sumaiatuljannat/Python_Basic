# Base class
class Bird:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def eat(self):
        print(f"{self.name} is eating.")

    def fly(self):
        print(f"{self.name} is flying.")

    def info(self):
        print(f"Bird Name: {self.name}, Color: {self.color}")


# Child class (Inheritance)
class Eagle(Bird):
    def __init__(self, name, color, speed):
        super().__init__(name, color)
        self.speed = speed

    def hunt(self):
        print(f"{self.name} is hunting at {self.speed} km/h speed.")


# Creating objects
bird1 = Bird("Parrot", "Green")
bird1.info()
bird1.eat()
bird1.fly()

print("\n--- Eagle Object ---")
eagle1 = Eagle("Golden Eagle", "Brown", 120)
eagle1.info()
eagle1.fly()
eagle1.hunt()