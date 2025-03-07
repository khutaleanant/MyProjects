# # Example of Iterator
# # tuple= ("Anant","Sachin","Mahesh","Vinod")
# # MyIterator=iter(tuple)
# # print(next(MyIterator))
# # print(next(MyIterator))
# # print(next(MyIterator))
# # print(next(MyIterator))

# # #Example2 of Iterator
# # string = "GFG"
# # ch_iterator = iter(string)
# # print(next(ch_iterator))
# # print(next(ch_iterator))
# # print(next(ch_iterator))

# #==========================================
# # my_list = [1, 2, 3, 4]

# # # Using for loop with an iterator
# # for item in my_list:
# #     print(item)
# #===========================================
# # Transactions = ["order123, John Doe, 3 items, unpaid",
# #                 "order124, Jane Smith, 2 items, unpaid",
# #                 "order125, Alice Brown, 5 items, paid",]
# # Myitr=iter(Transactions)
# # # print(next(Myitr))
# # print(next(Myitr))
# # for Order in Transactions:
# #     print(f"Processing order: {Order}")
# #     if 'unpaid' in Order:
# #         print("Order is unpaid. Awaiting payment.")
# #     else:
# #         print("Order is paid. Proceeding with shipment.")
# #========================================
# # # Example of Generator
# # def FirstGenerator():
# #     yield ["Anant,Sachin"]
# #     yield ["Mahesh","Ganesh"]
# #     yield ["Raju","Shyam"]
# # for value in FirstGenerator():
# #     print(value)
# #     print("One List end")
# #========================================
# # Example of thr "return" keyword
# # def Addition(A,b):
# #     c=A+b
# #     # print(c)
# #     return c
# # result=Addition(100,200)
# # print(result)   
# # result=Addition(10,20)
# # print(result)
# ##============================================================
# ## Example1 of "Closures"
# # def Greeting(Name):
# #     def DisplayName():
# #         print("Hi",Name)
# #     DisplayName()
# # Greeting("Anant")
# #======================================
# ## Example2 of "Closures"
# # def OuterValue(OuterValues):
# #     def InnerValue(InnerValues):
# #         return OuterValues+InnerValues
# #     return InnerValue

# # Result=OuterValue(100)
# # print(Result(10))
# ##==============================================
# #Example of the "Decorator"
# def shout(text):
#     return text.upper()

# def wishper(text):
#     return text.lower()

# def Greeting(func):
#     Greeting=func("I am created this function for the practise")
#     print(Greeting)

# Greeting(shout)
# Greeting(wishper)
# ##======================================================
# # Example fo the "Property"
# ##Python programming provides us with a built-in property decorator
# ##which makes usage of getter and setters much easier in Object- Oriented Programming.

# class Alphabet:
#     def __init__(self, value):
#         self._value = value
    
#     def getValue(self):
#         print('Getting value')
#         return self._value
    
#     def setValue(self, value):
#         print('Setting value to ' + value)
#         self._value = value
    
#     def delValue(self):
#         print('Deleting value')
#         del self._value
    
#     # Define property for getting, setting, and deleting the value
#     value = property(getValue, setValue, delValue)

# # Create an instance of Alphabet
# x = Alphabet('GeeksforGeeks')

# # Access the value using the property getter
# print(x.value)

# # Set a new value using the property setter
# x.value = 'GfG'

# # Delete the value using the property deleter
# del x.value
# ##==========================================================
# Example 2 fo the "Property"
# Banking System with Properties

class HSBCBankAccount:
    def __init__(self,AccountInitialBalance=0):
        self.AccountInitialBalance=AccountInitialBalance

    def GetBalance(self):
        return self.AccountInitialBalance
    
    def SetBalance(self,value):
        if value < 0:
            raise ValueError("Balance can not Negative")
        self._value=value
  
    Balance=property(GetBalance,SetBalance)

# Creating a bank account   
Account=HSBCBankAccount (2000)

# Accessing the balance using the property getter
# print(Account.Balance)

# Setting a new balance using the property setter
Account.Balance = 4000
# print(Account.AccountInitialBalance)
print(Account.Balance)

# try:
#     Account.Balance= -20000
# except ValueError as e:
#     print(e)


# Arnav's first python project program.
cost1=200
cost2=300
cost3=200
total=cost1+cost2+cost3
print(total)