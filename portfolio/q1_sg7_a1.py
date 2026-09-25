class Glassware:

      def __init__(self, material = "glass"):
          self.material = material

class Beaker(Glassware):

    def __init__(self, ml=250):
        super().__init__(material = "glass")
        self.ml = ml

class Tray:
    
    def __init__(self):
        self.beakers = [Beaker() for i in range(5)]

    def __del__(self):
        self.beakers.clear

beaker_tray = Tray()
print(f"Tray is created, carrying {len(beaker_tray.beakers)}beakers.")
del beaker_tray
