class Account_details:
    def __init__(self,Name,Account_id,balance):
        self.__Name = Name                  #private attribute
        self.__Account_id = Account_id      #private attribute
        self.__balance = balance            #private attribute

    def get_Name(self):
        return self.__Name
    
    def get_balance(self):
        return self.__balance
    
    def deposite(self,amount,Name,Account_id):
        if Name == self.__Name and Account_id == self.__Account_id:
         self.__balance += amount
         print(f"Deposited {amount} successfully for { Name}")
         print(f"New available balance:{self.__balance}")
         return self.__balance
        else:
            print("user name and account id incorrect! ")
      

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"withdraw { amount},new balance { self.__balance}")
        else:
            print("insufficient balance ")


banks = Account_details("varshith R",101048565415,25000)
banks.deposite(int(input("please enter the deposit amount, name, account id!  ")))

    
