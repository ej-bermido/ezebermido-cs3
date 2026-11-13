from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_data(self):
        pass

class TempSensor(Sensor):
    def get_data(self):
        return "26 degrees C"

    def __str__(self):
        return "26 degrees C"

tempsensor = TempSensor()
print(tempsensor.get_data())
print(tempsensor)
