# Three ways of using print funtion

Data1=12
Data2="Anant"

## 1) Normal Display
print("Value of Data1 is ",Data1)
print("Value of Data2 is ",Data2)

## 2) Positional Formating
print("Value of data1 = {} and value of data2 = {}".format(Data1,Data2))
print("Value of data1 = {0} and value of data2 = {1}".format(Data1,Data2))

## 3) Format Specified
print("Value of Data1 is %s and Value of Data2 is %s"%(Data1,Data2))