class Patient: # parent class

    def __init__(self, name, bill_amount: float): # initialize da stuff
        self.__name = name
        self.__bill_amount = bill_amount
        
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

    # function calculate bill
    def calculate_bill(self):
        return self.__bill_amount

class Senior_Patient(Patient): # child class

    def __init__(self, name, bill_amount): # initialize da child class stuff
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return self.get_bill_amount() * 0.80
    

class PhilHealth_Patient(Patient): # child class

    def __init__(self, name, bill_amount): # initialize da child class stuff
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return self.get_bill_amount() * 0.85


# actual code
print("Hospital Billing System\n------------------------")
# patients

patient1 = Patient("Eze Bermido", 15000.00)
patient2 = Senior_Patient("Daniel Legaspi", 15000.00)
patient3 = PhilHealth_Patient("Raven Veniegas", 15000.00)

# get their bill

bill1 = patient1.calculate_bill()
bill2 = patient2.calculate_bill()
bill3 = patient3.calculate_bill()

# get their names

name1 = patient1.get_name()
name2 = patient2.get_name()
name3 = patient3.get_name()

print(f"Patient Name ::: {name1}\nOriginal Bill ::: PHP{patient1.get_bill_amount()}\nFinal Bill: PHP{bill1}\n")
print(f"Patient Name ::: {name2}\nOriginal Bill ::: PHP{patient2.get_bill_amount()}\nFinal Bill: PHP{bill2}\n")
print(f"Patient Name ::: {name3}\nOriginal Bill ::: PHP{patient3.get_bill_amount()}\nFinal Bill: PHP{bill3}\n")



    
        
        
