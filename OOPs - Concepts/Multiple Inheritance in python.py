# class A:

#     def printA(self):
#         print("A CLASS")
# class B:
#     def printB(self):
#         print("B Class")

# class C(A,B):
#     def printC(self):
#         print("C Class")

# C=C()
# C.printA()
# C.printB()
# C.printC()

#============================================

# class Father:
#     def printFather(self):
#         print("Ram")

# class Mother:
#     def printMother(self):
#         print("Seeta")

# class Son(Father,Mother):
#     def printSon(self):
#         print("Govind")

# Son=Son
# Son.printSon()
# Son.printFather()
# Son.printMother()

#========================================================
# class Mother:
#     def Mother(self):
#         print(self.MotherName)

# class Father:
#     def Father(self):
#         print(self.FatherName)

# class Son (Mother,Father):

#     def Parent(self):
#         print("Father Name:",self.FatherName)
#         print("Mother Name:",self.MotherName)
        
#     def ParenData(self,FatherName,MotherName):
#         self.FatherName=FatherName
#         self.MotherName=MotherName
   
# Son=Son()
# Son.FatherName ="Shiv"
# Son.MotherName ="Parvati"
# Son.Parent()
# Son.ParenData("Ram","Seeta")
# Son.Parent()
#===============================================

class Student:
    def StudentClass(self,RollNumber,Name,Address):
        self.StudentRollNumer=RollNumber
        self.StudentName=Name
        self.StudentAddress=Address

    def Setdata(self,StudentRollNumber,StudentName,StudentAddress):
        self.StudentRollNumer=StudentRollNumber
        self.StudentName=StudentName
        self.StudentAddress=StudentAddress
    def printstudentdata(self):
        print(self.StudentRollNumer)
        print(self.StudentName)
        print(self.StudentAddress)
               
Student=Student()
Student.Setdata("001","Anant Khutale","Kolhapur")
Student.printstudentdata()
Student.Setdata("001","Anant Khutale","Pune")
Student.printstudentdata()
Student.Setdata("001","Anant khutale","Mumbai")
Student.printstudentdata()
# ============================================================



     




    
