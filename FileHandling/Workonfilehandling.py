# f=open("D:\\Anant\\ABC TRAINING\\Payton_ABC Training\\Notes\\Practical\\FileHandling\\Demo.txt","rt")
# print(f)
# print(f.read())
# print(f.read(2))
# print(f.readlines())
# f.close()
# print(f.read())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()
# #==================================================
# f=open("D:\\Anant\\ABC TRAINING\\Payton_ABC Training\\Notes\\Practical\\FileHandling\\Demo.txt","a")
# f=open("D:\\Anant\\ABC TRAINING\\Payton_ABC Training\\Notes\\Practical\\FileHandling\\Demo.txt","w")
# f.write("\nI am adding this newline in this file")
# f.close()
# #=========================================================
# f=open("G:\\ABC TRAINING\\Payton_ABC Training\\Notes\\Practical\\FileHandling\\FileCreationWorkDemo.txt","a")
# f.write("I have create this file using the python file handling")
# f.close()
#======================================================================
# f=open("G:\\ABC TRAINING\\Payton_ABC Training\\Notes\\Practical\\FileHandling\\FileCreationWorkDemo02.txt","w")
# f.write("I have create this file using the python file handling")
# f.write("\nWritting additional data in the exiting file.")
# f.close()
#=====================================================
# f=open("G:\\ABC TRAINING\\Payton_ABC Training\\Notes\\Practical\\FileHandling\\FileCreationWorkDemo02.txt","x")
# f.write("I have create this file using the python file handling")
# f.close()
#===================================================
# import os
# os.remove("G:\\ABC TRAINING\\Payton_ABC Training\\Notes\\Practical\\FileHandling\\FileCreationWorkDemo2.txt")
#===================================================
import os
if os.path.exists("G:\\ABC TRAINING\\Payton_ABC Training\\Notes\\Practical\\FileHandling\\FileCreationWorkDemo2.txt"):
    os.remove("G:\\ABC TRAINING\\Payton_ABC Training\\Notes\\Practical\\FileHandling\\FileCreationWorkDemo2.txt")
else:
    print("Does not exist file. It is already deleted")