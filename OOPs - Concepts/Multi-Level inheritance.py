# #Building Base Class
# class BaseClass:
#     #Constructore to set data
#     def __init__(self,Name,RollNumber,Role):
#         self.Name=Name
#         self.RollNumber=RollNumber
#         self.Role=Role

# #Building Intermediate Class (Intermediate Class: Inherits the Base Class)
# class IntermediateClass(BaseClass):
#     def __init__(self,Age,Name,RollNumber,Role):
#         super().__init__(Name,RollNumber,Role)
#         self.Age = Age

# #Buidling Derived Class: Inherits the Intermediate Class to print the data
# class DerivedClass(IntermediateClass):
#     #method to print data
#     def __init__(self, Age, Name, RollNumber, Role):
#         super().__init__(Age, Name, RollNumber, Role)
#     def printdata(self):
#         print(f"Student Name is:{self.Name}")
#         print(f"Student Age is:{self.Age}")
#         print(f"Student RollNumberis:{self.RollNumber}")
#         print(f"Student Role is:{self.Role}")

# # Creating objects
# Student1=DerivedClass("Anant Khutuale","42","007","Senior Student")
# Student2=DerivedClass("Anant Khutuale","42","007","Senior Student")
# Student1.printdata()
# Student2.printdata()
#=====================================================================================
# class BaseCar:
#     def __init__(self,CarName,CarType,CarTransmission):
#         self.CarName=CarName
#         self.CarType=CarType
#         self.CarTransmission=CarTransmission

# class AdditionalFunction(BaseCar):
#     def __init__(self, CarName, CarType, CarTransmission,CarFuleType,Carprice):
#         super().__init__(CarName, CarType, CarTransmission)
#         self.CarfuelType=CarFuleType
#         self.CarPrice=Carprice

# class FinalCarDesc(AdditionalFunction):
#     def __init__(self, CarName, CarType, CarTransmission, CarFuleType, Carprice):
#         super().__init__(CarName, CarType, CarTransmission, CarFuleType, Carprice)

#     def printdata(self):
#         print(f"Car Name:- {self.CarName}")
#         print(f"Car Type:- {self.CarType}")
#         print(f"Car Transmission:- {self.CarTransmission}")
#         print(f"Car Fuel Type:- {self.CarfuelType}")
#         print(f"Car Price:- {self.CarPrice}")

# MarutiSwiftMN1=FinalCarDesc("Maruti Swift","HatchBack","Manual 5 Gear","PETROL","Rs.7,50,000")
# MarutiSwiftAT2=FinalCarDesc("Maruti Swift","HatchBack","AUTOMATIC IMT","PETROL","Rs.8,50,000")
# MarutiSwiftMN3=FinalCarDesc("Maruti Swift","HatchBack","Manual 5 Gear","DIESEL","Rs.9,50,000")
# MarutiSwiftAT4=FinalCarDesc("Maruti Swift","HatchBack","AUTOMATIC IMT","DIESEL","Rs.10,50,000")
# MarutiSwiftMN5=FinalCarDesc("Maruti Swift","HatchBack","Manual 5 Gear","CNG","Rs.11,50,000")
# MarutiSwiftAT6=FinalCarDesc("Maruti Swift","HatchBack","AUTOMATIC IMT","CNG","Rs.12,50,000")
# MarutiSwiftMN7=FinalCarDesc("Maruti Swift","HatchBack","Manual 5 Gear","EV","Rs.15,50,000")
# MarutiSwiftAT7=FinalCarDesc("Maruti Swift","HatchBack","AUTOMATIC IMT","Petrol","Rs.8,50,000")
# MarutiDzireMN1=FinalCarDesc("Maruti Swift Dzire","Sedan","Manual 5 Gear","PETROL","Rs.8,50,000")
# MarutiDzireAT2=FinalCarDesc("Maruti Swift Dzire","Sedan","AUTOMATIC IMT","PETROL","Rs.9,50,000")
# MarutiDzireMN3=FinalCarDesc("Maruti Swift Dzire","Sedan","Manual 5 Gear","DIESEL","Rs.10,50,000")
# MarutiDzireAT4=FinalCarDesc("Maruti Swift Dzire","Sedan","AUTOMATIC IMT","DIESEL","Rs.11,50,000")
# MarutiDzireMN5=FinalCarDesc("Maruti Swift Dzire","Sedan","Manual 5 Gear","CNG","Rs.12,50,000")
# MarutiDzireAT6=FinalCarDesc("Maruti Swift Dzire","Sedan","AUTOMATIC IMT","CNG","Rs.13,50,000")
# MarutiDzireMN7=FinalCarDesc("Maruti Swift Dzire","Sedan","Manual 5 Gear","EV","Rs.17,50,000")

# MarutiSwiftMN1.printdata()
# MarutiSwiftAT2.printdata()
# MarutiSwiftMN3.printdata()
# MarutiSwiftAT4.printdata()
# MarutiSwiftMN5.printdata()
# MarutiSwiftAT6.printdata()
# MarutiSwiftMN7.printdata()
# MarutiSwiftAT7.printdata()
# MarutiDzireMN1.printdata()
# MarutiDzireAT2.printdata()
# MarutiDzireMN3.printdata()
# MarutiDzireAT4.printdata()
# MarutiDzireMN5.printdata()
# MarutiDzireAT6.printdata()

#=========================
#### OTT SUBCRIPTION program in Inheritance for Practice #####

#Creating BaseClass
class OTTSubcription:
    def __init__(self,SubcriberID,SubcriptionPlan,SubcriptionLenght,SubcriptionPrice):
        self.SubcriberId=SubcriberID
        self.SubcriptionPlan=SubcriptionPlan
        self.SubcriptionLenght=SubcriptionLenght
        self.SubcriptionPrice=SubcriptionPrice

    def OTTSubcription(self):
          print(f"Subcriber ID: {self.SubcriberId}\nPlan Name: {self.SubcriptionPlan}\nPlan Lenght: {self.SubcriptionLenght}\nPrice Rs. {self.SubcriptionPrice}")

    def Subcribe(self):
        print(f"You are subcribed {self.SubcriptionLenght} {self.SubcriptionPlan}")

    def Unsubcribe(self):
        print(f"You are Unsubcribed {self.SubcriptionLenght} {self.SubcriptionPlan}")

class OTTPremiumSubcripition(OTTSubcription):
    def __init__(self,SubcriberID,SubcriptionPlan,SubcriptionLenght,SubcriptionPrice,Resulotion,Screens):
        super().__init__(SubcriberID,SubcriptionPlan,SubcriptionLenght,SubcriptionPrice)
        self.Screens=Screens
        self.Resulotion=Resulotion
    
    def OTTPremiumSubcripition(self):
        print(f"Subcriber ID: {self.SubcriberId}\nPlan Name: {self.SubcriptionPlan}\nPlan Lenght: {self.SubcriptionLenght}\nPrice Rs: {self.SubcriptionPrice}\nResolution: {self.Resulotion}\nScreen Limit: {self.Screens}")

# Netflix1=OTTSubcription("1080","BASE PLAN","MONTHLY","320")
# Netflix1.OTTSubcription()
# # Netflix1.Subcribe()
# Netflix1.Unsubcribe()
# Netflix2=OTTPremiumSubcripition("1008","PREMIUM PLAN","MONTHLY","1200","4K UHD","4")
# Netflix2.OTTPremiumSubcripition()
# Netflix2.Subcribe()
# Netflix2.Unsubcribe()
##==================================================================================
# Example: Employee Management System

class Employee:
    def __init__(self,EmployeeID,EmployeeName,EmployeeRole,EmployeeSalary):
        self.EmployeeId=EmployeeID
        self.EmployeeName=EmployeeName
        self.EmployeeRole=EmployeeRole
        self.EmployeeSalary=EmployeeSalary
    
    def DisplayEmployeeDetails(self):
        print(f"Employee ID:{self.EmployeeId}\nEmployee Name:{self.EmployeeName}\nEmployee Role:{self.EmployeeRole}\nEmployee Salary:{self.EmployeeSalary}")

    def Work(self):
        print(f"{self.EmployeeName} is working with the company as Team Leader.")

class Manager(Employee):
    def __init__(self,EmployeeID,EmployeeName,EmployeeRole,EmployeeSalary,TeamSize):
        super().__init__(EmployeeID,EmployeeName,EmployeeRole,EmployeeSalary)
        self.TeamSize=TeamSize
    
    def DisplayManagerDetails(self):
        print(f"Employee ID:{self.EmployeeId}\nEmployee Name:{self.EmployeeName}\nEmployee Role:{self.EmployeeRole}\nEmployee Salary:{self.EmployeeSalary}\nTeam Size:{self.TeamSize}")

    def Work(self):
        print(f"{self.EmployeeName} is Managing the team of {self.TeamSize} employees.")

class Developer(Employee):
    def __init__(self, EmployeeID, EmployeeName, EmployeeRole, EmployeeSalary,ProgrammingLanguage):
        super().__init__(EmployeeID, EmployeeName, EmployeeRole, EmployeeSalary)
        self.ProgrammingLanguage=ProgrammingLanguage
    
    def DisplayDeveloperDetails(self):
        print(f"Employee ID:{self.EmployeeId}\nEmployee Name:{self.EmployeeName}\nEmployee Role:{self.EmployeeRole}\nEmployee Salary:{self.EmployeeSalary}\nProgramming Language:{self.ProgrammingLanguage}")

    def Work(self):
        print(f"{self.EmployeeName} is {self.EmployeeRole} and he is coding in {self.ProgrammingLanguage}.")

# Employee1=Employee("20065329","Anant Khutale"," Team Leader","INR 90000")
# Employee1.DisplayEmployeeDetails()
# Employee1.Work()

# Manager1=Manager("20065000","Arnav Patil","Manager","INR 150000",20)
# Manager1.DisplayManagerDetails()
# Manager1.Work()

# Developer1=Developer("20009090","Avinash Kadam","Software Developer","INR 75000","Java, Python")
# Developer1.DisplayDeveloperDetails()
# Developer1.Work()

##===========================================================
## Example: Bank Account System
#Base Class: Bank Account

class BankAccount:
    def __init__(self,AccountNumber,AccountBalance):
        self.AccountNumber=AccountNumber
        self.AccountBalance=AccountBalance
    
    def Deposit(self,Amount):
        self.AccountBalance += Amount
        print(f"Deposit Amount:{Amount} \nNew Balance:{self.AccountBalance}")
    
    def Withdraw(self,Amount):
        if self.AccountBalance>=Amount:
            self.AccountBalance -=Amount
            print(f"withdraw Amount:{Amount}\nNew Balance:{self.AccountBalance}")
        else:
            print("Insufficient Funds")
    
    def CheckBalance(self):
        print(f"Account Balance is {self.AccountBalance}")

#Derived class: SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, AccountNumber, AccountBalance,ROI):
        super().__init__(AccountNumber, AccountBalance)
        self.ROI=ROI

    def ApplyIntrest(self):
        Intrest=self.AccountBalance * self.ROI/100
        self.AccountBalance +=Intrest
        print(f"Applied Intrest:{Intrest}\nNew Balance:{self.AccountBalance}")

class CurrentAccount(BankAccount):
    def __init__(self, AccountNumber, AccountBalance,OverDraftLimit):
        super().__init__(AccountNumber, AccountBalance)
        self.OverDraftLimit=OverDraftLimit
    
    def Withdraw(self, Amount):
        if self.AccountBalance+self.OverDraftLimit>=Amount:
            self.AccountBalance -=Amount
            print(f"Withdraw Amount:{Amount}\nNew Balance:{self.AccountBalance}")
        else:
            print(f"OverDraft Limit Exceeeded")

#Create Objects

# SavingsAccount1=SavingsAccount("S/A No: 1234",1000,5)
# SavingsAccount1.Deposit(2000)
# SavingsAccount1.ApplyIntrest()
# SavingsAccount1.Withdraw(1000)
# SavingsAccount1.CheckBalance()

# SavingsAccount2=SavingsAccount("S/A No: 9999",10000,10)
# SavingsAccount2.Deposit(2000)
# SavingsAccount2.ApplyIntrest()
# SavingsAccount2.Withdraw(1000)
# SavingsAccount2.CheckBalance()

# CurrentAccount1=CurrentAccount("C/A No: 1111",2000,2500)
# CurrentAccount1.Withdraw(1000)
# CurrentAccount1.CheckBalance()

CurrentAccount2=CurrentAccount("C/A No:2222",1000,1000)
CurrentAccount2.Withdraw(2000)
CurrentAccount2.CheckBalance()
##==========================================================================