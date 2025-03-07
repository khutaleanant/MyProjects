class SchoolTree:
    def Fun1(self):
        print("This function is in SchoolTree")
class Student1:
    def Fun2(self):
        print("This function is in Student1")
class Student2:
    def Fun3(self):
        print("This function is in student2")
        
class Student3(Student2,SchoolTree):
    def Fun4(self):
        print("This function is in Student3")

OBJ1=Student3()
OBJ1.Fun1()
OBJ1.Fun3()
OBJ1.Fun4()
#=========================================================