# Parent class
class Payment:
    def pay(self, amount):
        print("Processing payment...")


# Child class 1
class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


# Child class 2
class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


# Child class 3
class Cash(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")


# Create objects
p1 = CreditCard()
p2 = UPI()
p3 = Cash()

# Same method, different behavior
p1.pay(1000)
p2.pay(500)
p3.pay(200)