class employee:
    __count=0
    def __init__(self):
        employee.__count=employee.__count+1
    def Display(self):
        print("Employee Count is",employee.__count)

Employee=employee()
# Employee.Display()
# print(Employee.__count)
# # try:
# #     print(Employee.__count)
# # finally:
#     Employee.Display()

##=================================================================