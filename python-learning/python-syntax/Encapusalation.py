class ATM:
    def __init__(self,Name,Account_id,balance):
        self.__Name = Name #private attribute
        self.__balance = balance #private attribute
        self.__Account_id = Account_id #private attribute

    def deposite(self,amount):
        self.__balance += amount
        return amount

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"withdraw { amount},new balance { self.__balance}")
        else:
            print("insufficient balance ")


atm = ATM("varshith R",101048565415,25000)
atm.deposite(2000)
atm.withdraw(10)
    
