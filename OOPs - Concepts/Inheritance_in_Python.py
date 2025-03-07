# class Animal:
#     def __init__(self,name):
#         self.name=name

#     def sound(self):
#         pass

# class Dog(Animal):
    
#     def sound(self):
#         print(f"{self.name} Bark")

# class Cat(Animal):
#     def sound(self):
#         print(f"{self.name} Meww")

# Dog1=Dog("Tommy")
# # print(Dog1.name)
# Dog1.sound()

# # Cat1=Cat("Snowee")
# # print(Cat1.name)
# # Cat1.sound()
# #=========================================================
# # **Example of Vaiours Cars**
# class Car:
#     def __init__(self,name,price,FuelType,Transmission):
#         self.name=name
#         self.price=price
#         self.FuelType=FuelType
#         self.Transmission=Transmission
        
#     def PrintData(self):
#         pass

# class Tata(Car):
#     def PrintData(self):
#         print(f"Car Name -{self.name}")
#         print(f"Car Price -{self.price}")
#         print(f"Car Fuel type -{self.FuelType}")
#         print(f"Car Transmission -{self.Transmission}")

#     def TataFuture():
#         print(f"NACH 5 STAR RATING")


# class Maruti(Tata):
#     def PrintData(self):
#         pass
#         print(f"Car Name -{self.name}")
#         print(f"Car Price -{self.price}")
#         print(f"Car Fuel type -{self.FuelType}")
#         print(f"Car Transmission -{self.Transmission}")

# Harihar=Maruti("Harriar","1200000","Petrol","Auto-AMT")
# Harihar.PrintData()
# Maruti.TataFuture()
#===========================================
########### CAR MANUFACTURING DATA FOR USE ############# ERORR Function Overloading
# class CAR:
#     def __init__(self,CAR_TRANSMISSION,CAR_TYPE,FUEL_TYPE, Price):
#         self.TRANSMISSION=CAR_TRANSMISSION 
#         self.TYPE=CAR_TYPE
#         self.FUEL=FUEL_TYPE
#         self.Price=Price

#     def printdata(self):
#         print(f" CAR TRANSMISSION: {self.TRANSMISSION}")
#         print(self.FUEL)
#         print(self.TYPE)
#         print(self.Price)
    
#     # def printdata(self,newprice):
#     #     self.Price=newprice
      
# TATA=CAR("AUTO","HATCHBACK","PETROL","RS.500000")

# # CAR.printdata()
# # CAR.printdata("180000")

# TATA.printdata()
# =================================================================
class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)

#Use the Person class to create an object, and then execute the printname method:
X=person("Anant","Khutale")
X.printname()
#==================================================================
class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)
class student(person):
    pass

#Use the Person class to create an object, and then execute the printname method:
X=person("Anant","Khutale")
X=student("Mahesh","Jadhav")
X.printname()
#=====================================================
    

        









    


