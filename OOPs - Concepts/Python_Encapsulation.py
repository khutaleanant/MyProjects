# Python program to demonstrate private memebers
# "__" double underscore represents private attribute.
# Private attributes start with "__".

# Creating a Base class
class Base:
    def __init__(self):
        self.a="Python"
        self.__c="Python"
    def printdata(self):
        print(self.__c)


# Creating a deriverd class
class Deriverd(Base):
    def __init__(self):
        print(self.__c)

Obj1=Base()
print(Obj1.a)
print(Obj1.__c)
Obj1.printdata()
