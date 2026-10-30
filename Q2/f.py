class Bill:

    amount = 0

    def __init__(self, amount):
        self.amount = amount

    # functions for paying

    def pay(self, payment):
        self.amount -= payment.amount
        print("Payment paid using ::: ",payment.mode)
        print("Balance ::: ", self.amount)

class Payment:

    amount = 0
    mode = "Cash"

    def __init__(self, amount):
        self.amount = amount

class Ewallet(Payment):
    def __init__(self, name, amount):
        super().__init__(amount)
        self.mode = name

bigbeautifulbill = Bill(1000)
bayad = Payment(900)
bigbeautifulbill.pay(bayad)

gcash = Ewallet("GCash", 100)
bigbeautifulbill.pay(gcash)
