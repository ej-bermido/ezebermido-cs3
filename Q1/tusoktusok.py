class Sauce:
    def __init__(self,name,taste):
        self.name = name
        self.taste = taste
        print(self.name, "was created.")
    def __del__(self):
        print(self.name,"ran out.")

    def __str__(self):
        return "This is"+self.name+" and it tastes "+self.taste

class Tusoktusok:
    def __init__(self,name,sauce):
        self.name = name
        self.sauce = sauce
        print(self.name,"is cooked and dipped in",self.sauce.name)

    def eat(self):
        print("I am eating", self.name,"and it tastes",self.sauce.taste)

    def __del__(self):
        print(self.name,"was thrown in the trash.")

vinegar = Sauce("Vinegar", "Sour")
fishball = Tusoktusok("Fishball", vinegar)
fishball.eat()
del fishball
