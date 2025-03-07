import numpy as np
Data1=np.array([[12,13],[21,31],[90,100]])
print(Data1)
print(type(Data1))
print(Data1.ndim)

Data2=np.array([[123,141],[111,101],[11,9]])
print(Data2)

Data3=Data1+Data2
print(Data3)

Data4=Data1-Data2
print(Data4)

Data5=Data1*Data2
print(Data5)

Data6=Data1/Data2
print(Data6)