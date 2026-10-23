class Student:
    __name: str
    __age = 0

    def __init__(self, name):
        self.__name = name

    def set_age(self, age):
        if age > 0:
            self.__age = age

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def greet(self):
        return f"Howdy! My name is {self.__name}"

    def set_name(self, name):
        self.__name = name

student1 = Student("Josef")
student1.set_age(-16)
student1.set_name("JM")
print(f"Student name : {student1.get_name()}")
print(f"Student age : {student1.get_age()}")
