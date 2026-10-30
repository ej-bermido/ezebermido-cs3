class Patient: # parent class

    def __init__(self, name, bill_amount: float, patient_type = "Patient"): # initialize da stuff
        self.__name = name
        self.__bill_amount = bill_amount
        self.patient_type = patient_type
        
        
    # get-ter functions
    def get_name(self):
        return self.__name

    def get_bill_amount(self):
        return self.__bill_amount

    # set-ter functions
    def set_name(self, name):
        self.__name = name

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    # display
    def display_patient_type(self):
        return self.patient_type
        

    # function calculate bill
    def calculate_bill(self):
        return self.__bill_amount

class Senior_Patient(Patient): # child class


    def __init__(self, name, bill_amount, patient_type = "Sr. Patient"): # initialize da child class stuff
        super().__init__(name, bill_amount, patient_type)

    # display
    def display_patient_type(self):
        return self.patient_type

    def calculate_bill(self):
        return self.get_bill_amount() * 0.80
    

class PhilHealth_Patient(Patient): # child class

    def __init__(self, name, bill_amount, patient_type = "PhilHealth Patient"): # initialize da child class stuff
        super().__init__(name, bill_amount, patient_type)

    # display
    def display_patient_type(self):
        return self.patient_type

    def calculate_bill(self):
        return self.get_bill_amount() * 0.85


# actual code
print("Hospital Billing System\n------------------------")

# patients

patient1 = Patient("Eze Bermido", 15000.00)
patient2 = Senior_Patient("Daniel Legaspi", 15000.00)
patient3 = PhilHealth_Patient("Raven Veniegas", 15000.00)

# display

print(f"Patient Name ::: {patient1.get_name()}\nOriginal Bill ::: PHP{patient1.get_bill_amount()}\nType ::: {patient1.display_patient_type()}\nFinal Bill: PHP{patient1.calculate_bill()}\n")
print(f"Patient Name ::: {patient2.get_name()}\nOriginal Bill ::: PHP{patient2.get_bill_amount()}\nType ::: {patient2.display_patient_type()}\nFinal Bill: PHP{patient2.calculate_bill()}\n")
print(f"Patient Name ::: {patient3.get_name()}\nOriginal Bill ::: PHP{patient3.get_bill_amount()}\nType ::: {patient3.display_patient_type()}\nFinal Bill: PHP{patient3.calculate_bill()}\n")



    
        
        
