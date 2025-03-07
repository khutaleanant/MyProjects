# class Dog:
#     species= "Lab" # Class attribute


#     def __init__(self,name,age):
#         self.name=name # Instance attribute
#         self.age=age # Instance attribute
    
#     def printData(self):
#         print(self.name)
#         print(self.age)
#         print(self.species)

# # Creating an oject of the Dog class

# dog1=Dog("Puppy",4)
# dog2=Dog("Bravo",7)

# # print(dog1.name)
# # print(dog2.name)
# # print(dog1.age)
# # print(dog2.age)
# # print(dog1.species)
# # print(dog2.species)

# dog1.printData()
# dog2.printData()

#============================================================
# Purchase of Mobile data by user

class Mobile:

    def __init__(self,Mobile_Type,Price,Purchase_Date):
        self.Mobile_Type=Mobile_Type # Instance attribute
        self.Price=Price # Instance attribute
        self.Purchase_Date=Purchase_Date # Instance attribute
    

    def printData(self):
        print(self.Mobile_Type)
        print(self.Price)
        print(self.Purchase_Date)

# Creating an oject of the Dog class

Mobile1=Mobile("VIVO","RS.20000","02/10/2024")
Mobile2=Mobile("Iphone 16","Rs.90000","02/09/2024")
Mobile3=Mobile("Samsung","Rs.75000","12/12/2024")
Mobile4=Mobile("OnePlus","Rs.39000","01/10/2024")
Mobile1.printData(),Mobile2.printData(),Mobile3.printData(),Mobile4.printData()

#If we take the inputs from user then

Mobile_Type= input("Please Enter Your Mobile Type :")
Price=input("Please Enter the Mobile Price :")
Purchase_Date=input("Please Enter Mobile Purchase Date")

Vivo=Mobile(Mobile_Type,Price,Purchase_Date)
Vivo.printData()
#========================================================






        
        


