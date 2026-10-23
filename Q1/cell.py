class Nucleus:
    def __init__(self):
        print("Nucleus created")

    def __del__(self):
        print("Nucleus was destroyed...")

class Mitochondria:
    def __init__(self):
        print("Mitochondria created")

    def powerthecell(self):
        print("Mitochondria is producing energy.")

    def __del__(self):
        print("Mitochondria was destroyed...")

class Cell:
    def __init__(self):
        print("Cell created")
        self.nucleus = Nucleus()
        self.mitochondria = Mitochondria()

    def exist(self):
        print("Cell is existing")
        self.mitochondria.powerthecell()

    def __del__(self):
        del self.nucleus
        del self.mitochondria
        print("Cell was destroyed...")

while True:

    cellatwork = Cell()
    cellatwork.exist()
    del cellatwork

