class Animal:
    def Speak(self):
        print("Speaking")

class Dog(Animal):
    def Speak(self):
        print("Barking")
      
class ChildDog(Dog):
    def Speak(self):
        print(" Eating only Bread")
       
Obejct1=ChildDog()
Obejct1.Speak()
#===============================================================
## Real Life Example of method overriding ##

class Bank:
    def GetROI(self):
        return "10.00%"

class SBIBank(Bank):
    def GetROI(self):
        return "8.50%"

class HDFCBank(Bank):
    def GetROI(self):
        return "9.50%"

class ICICIBank(Bank):
    def GetROI(self):
        return "9.00%"
    
Obj1=Bank()
Obj2=SBIBank()
Obj3=HDFCBank()
Obj4=ICICIBank()
print("Rate of Intrest for Main Bank is",Obj1.GetROI())
print("Rate of Intrest for SBI Bank is",Obj2.GetROI())
print("Rate of Intrest for HDFC Bank is",Obj3.GetROI())
print("Rate of Intrest for ICICI Bank is",Obj4.GetROI())
Obj1.GetROI()
#==============================
import DataAbstractionInPython

Object1=DataAbstractionInPython.employee()
Object1.Display()
#=================================================