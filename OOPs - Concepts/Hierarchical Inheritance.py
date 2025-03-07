#Hierarchical Inheritance example
class parent:
    def fun1(self):
        print("This function is in parent class")

class child1(parent):
    def fun2(self):
        print("This function is in child1")

class child2(parent):
    def fun3(self):
        print("This function is in child2")

# Kid1=child1()
# Kid2=child2()
# Kid1.fun1()
# Kid2.fun1()
# Kid1.fun2()
# Kid2.fun3()
#================================================
class MobileProccesorSnapDragon:
    def Fun1(self):
        print("This is function for the Mobile processor")

class VivoMobile(MobileProccesorSnapDragon):
    def Fun2(self):
        print("This function is for the Vivo Mobile")

class OppoMobile(MobileProccesorSnapDragon):
    def Fun3(self):
        print("This function is for the Oppo Mobile")

class SamsungMobile(MobileProccesorSnapDragon):
    def Fun4(self):
        print("This function is for the Samsung Mobile")

class RedmeMobile(MobileProccesorSnapDragon):
    def Fun5(self):
        print("This function is for the Redme Mobile")

Mobile1=VivoMobile()
Mobile2=OppoMobile()
Mobile3=SamsungMobile()
Mobile4=RedmeMobile()

Mobile1.Fun2()
Mobile2.Fun3()
Mobile3.Fun4()
Mobile4.Fun5()
Mobile1.Fun1()
Mobile2.Fun1()
Mobile3.Fun1()
Mobile4.Fun1()
#=================================================================