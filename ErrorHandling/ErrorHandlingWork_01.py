# try:
#     x = 10 / 0  # This will raise a ZeroDivisionError
#     print(x)
# except ZeroDivisionError as e:
#     print("Error: Cannot divide by zero!")

# print("End this program")

#================
# x = 10 / 0  # This will raise a ZeroDivisionError
# print(x)
# print("End this program")
#============================================
# try:
#     num = int(input("Enter a number: "))  # User input could be invalid
#     result = 10 / num  # Division by zero could occur
# except ValueError:
#     print("Invalid input! Please enter a valid number.")
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")
#=================================================================
# try:
#     LoginHrId = input("Enter a HRID: ")
#     if LoginHrId == "20065329":
#         print("Next")
#         Password = input("Enter Your OneTime Passowrd:")
#         if Password == "Admin123":
#             print("You Have Successfully Login in to the system !")
#         else:
#             raise ValueError("Enter the Correct PASSWORD !")
#     else:
#         raise ValueError("Enter the Correct HR ID !")
# except ValueError as E:
#     print("Invalid input! Please enter a Input.",E)
   
# except ValueError as A:
#     print("Invalid input! Please enter a Input.",A)
#===================================================================================
#Program1= **Validation Login program**
# IdCounter=1
# PassCounter=1
# while(IdCounter<=3):
#     # print(Idcounter)
#     HR_ID=input("Please Enter Your HR ID :")
#     if HR_ID == "20065329":
#        while(PassCounter<=3):
#             Password=input("Please Enter Your Password :")
#             if Password=="Admin123":
#                 print("You Have Sucessfully Login in to the system")
#                 break
#             else:
#                 print("Password is incorrect")
#                 PassCounter=PassCounter+1
#                 # print(PassCounter)

#        if (PassCounter==4):
#         print("Too Many attemps,Please try agian after sometime")
#        break 
#     else:
#         print("HR ID is Incorrect, Please Try Again!")
#         if IdCounter==3:
#             print("Too Many attemps,Please try agian after sometime")
#         IdCounter=IdCounter+1
#=================================================================================
#Program1= **Validation Login program**
try:
    IdCounter=1
    PassCounter=1
    while(IdCounter<=3):
    # print(Idcounter)
        HR_ID=input("Please Enter Your HR ID :")
        if HR_ID == "20065329":
            while(PassCounter<=3):
                Password=input("Please Enter Your Password :")
                if Password=="Admin123":
                    print("You Have Sucessfully Login in to the system")
                    break
                else:
                    print("Password is incorrect")
                    PassCounter=PassCounter+1
                    # print(PassCounter)

            if (PassCounter==4):
                print("Too Many attemps,Please try agian after sometime")
            break 
        else:
            print("HR ID is Incorrect, Please Try Again!")
            if IdCounter==3:
               raise ValueError("Too Many attemps,Please try agian after sometime")
            IdCounter=IdCounter+1
except ValueError as e:
    print(e)


    
