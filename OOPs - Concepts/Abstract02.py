## Example of Banking for Abstract Base Class in Python
from abc import ABC,abstractmethod

#Abstract Base Class (ABC)
class BankAccount(ABC):

    def __init__(self,BankAccountHolder,AccountBalance=0):
        self.BankAccountHolder=BankAccountHolder
        self.AccountBalance=AccountBalance
    
    @abstractmethod
    def Deposit(self,Amount):
        pass

    @abstractmethod
    def Withdraw(self,Amount):
        pass

    def GetBalance(self):
        print(f"Account Balance: INR {self.AccountBalance}")

# Concrete subclass: SavingsAccount

class SavingsAccount(BankAccount):
    def Deposit(self,Amount):
        if Amount > 0:
            self.AccountBalance +=Amount
            print(f"INR {Amount} deposited in Saving Account.")
        else:
            print("Deposit amount must be positive.")

    def Withdraw(self,Amount):
        if Amount > 0 and Amount <= self.AccountBalance:
            self.AccountBalance -= Amount
            print(f"Withdrew INR {Amount} from Savings Account.")
        else:
            print("Insufficient balance or invalid amount.")

# Concrete class for Checking Account
class ChekcingBalance(BankAccount):
    def Deposit(self, Amount:float):
        if Amount >0:
            self.AccountBalance +=Amount
            print(f"Deposite INR {Amount} into checing account.")
        else:
            print("Deposit amount must be positive.")

    def Withdraw(self, Amount):
        if 0 < Amount <= self.AccountBalance:
            self.AccountBalance -=Amount
            print(f"Withdraw INR {Amount} from checking account.")
        else:
            print("Insufficient funds or invalid amount.")

    # def GetBalance(self):
    #     print(f"Checking Account Banalce is INR {self.AccountBalance}.")

# SavingsAccount1=SavingsAccount(1111,1000)
# SavingsAccount1.GetBalance()
# ChekcingBalance1=ChekcingBalance(222,2000)
# ChekcingBalance1.Withdraw(20000)
# ChekcingBalance1.Deposit(25000)
# ChekcingBalance1.GetBalance()
# from abc import ABC, abstractmethod
##================================================================================
# Abstract Base Class for Animals
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


# Concrete class for Dog
class Dog(Animal):
    
    def sound(self):
        return "Woof!"


# Concrete class for Cat
class Cat(Animal):
    
    def sound(self):
        return "Meow!"


# Concrete class for Cow
class Cow(Animal):
    
    def sound(self):
        return "Moo!"


# Example usage
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(f"A {animal.__class__.__name__} says: {animal.sound()}")

