import statistics

# CityId=[1001,1002,1003,1005,1006,1007,1008]
# # a=statistics.mean(CityId)
# # print(a)

# StudentId=[1111,1234,1111,1345,1143,1198,1111,2222,3333]
# b=statistics.median(StudentId)
# print(b)
##=======================================

# Data=[10,20,40,45,50,30,10,10,30,30,30,30,30]
# Obj1=statistics.mode(Data)
# print(Obj1)

# Data=[10,10,20,30,40] #UniModal or one mode
# Obj2=statistics.mode(Data)
# print(Obj2)

Data=[10,10,20,30,40,40,40,40] #MultiModal or Mutli mode
Obj2=statistics.mode(Data)
print(Obj2)