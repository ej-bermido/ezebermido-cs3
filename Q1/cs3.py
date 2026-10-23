#02 Ezekiel Javier L. Bermido

class Vehicle:
    # Properties
    def __init__(self,kindofvehicle):
        self.kindofvehicle = kindofvehicle
        print(self.kindofvehicle, "was created.")

    #Action
    def move(self,distance):
        print(self.kindofvehicle, "moved", distance,end="")

class Car(Vehicle):
    def __init__(self,kindofvehicle, brand, model):
        self.brand = brand; self.model = model
        super().__init__(kindofvehicle)
        print("The vehicle is a", brand,model)
    def move(self, distance):
        super().move(distance)
        print("KM")

class Boat(Vehicle):
    def __init__(self, kindofvehicle, model):
        self.model = model
        super().__init__(kindofvehicle)
        print("The vehicle is a",self.model)
    def move(self,distance):
        super().move(distance)
        print("Nm")


Ford = Car("SUV", "Ford", "ABC")
Ford.move(10)

Ferry = Boat("ferry", "RoRo")
Ferry.move(20)
