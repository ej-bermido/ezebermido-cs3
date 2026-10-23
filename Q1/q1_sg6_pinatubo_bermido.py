#2 Ezekiel Javier L. Bermido
#9 - Pinatubo

try:
    class Lab:
        def __init__(self, rm_number):
            self.rm_number = rm_number

    class Technician:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def assign_lab(self, keycard_lab):
            self.assigned_lab = keycard_lab

    chemistry_lab = Lab("A2303")
    lab_technician = Technician("Sir Mark Paulo Cruz", 20)
    lab_technician.assign_lab(chemistry_lab)

    print("Techinican " + lab_technician.name + " has received the key card for lab " + lab_technician.assigned_lab.rm_number + ".")

except Exception:
    print("Error! Please restart the program!")
