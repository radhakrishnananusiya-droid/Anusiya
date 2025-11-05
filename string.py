#Simple calculator in python
print("select an operation")
print("1 Addition(+)")
print("2 Subtraction(-)")
print("3 Mutiplication(*)")
print("4 Division(/)") 
#Take user input
choice = input("Enter choice(1/2/3/4):")
#Take two numbers as input
num1 = float(input("enter first numbers:"))
num2 = float(input("enter sceond number:"))


#Perform calcution based on user choice
if choice == '1':
  print("Result = ",num1+num2)
elif choice =='2':
  print("Result = ",num1-num2)
elif choice =='3':
  print("Result = ",num1*num2)
elif choice =='4':
 if num2 == 0:
  print("Result = ",num1/num2)
 else:
  print("Error;cannot divide by Zero!")
else:
  print("Invalid input !pleass chooss 1,2,3 or 4")
