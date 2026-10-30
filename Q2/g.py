class Vehicle:

    color = "Gray"

    def __init__(self, name, passengers):
        self.name = name
        self.passengers = passengers

    def move(self):
        print("Vehicle",self.color, self.name, "is moving.")
        print("It has", self.passengers,"passengers.")

class Car(Vehicle):

    def move (self):
        print("The car", self.color, self.name, "is travelling along the road.")
        print("It has", self.passengers, "passengers.")

class Boat(Vehicle):

    def move (self):
        print("The boat", self.color, self.name, "is saiing along the road.")
        print("It has", self.passengers, "passengers.")

class Skateboard:
    
    def move (self):
        print("The skateboard", self.color, self.name, "is rolling along the road.")
        print("It has", self.passengers, "passengers.")


car1 = Car("Ecosport", 5)
car1.color = "Red"

boat1 = Boat("Yacht", 10)
boat1.color = "White"

skbd = Skateboard()

vehicles = [car1, boat1, skbd]
for i in vehicles:
    i.move()
