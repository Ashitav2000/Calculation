# write a car class, that has a start_engine method and inherit from vehicle class

class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def start_engine(self):
        print(f"{self.name} engine started")

class Car(Vehicle):
    def __init__(self, name, color):
        super().__init__(name, color)

    def start_engine(self):
        print(f"{self.name} car engine started")

