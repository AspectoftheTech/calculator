
print("Select an operation to perform")
print("Type 1 for Addition")
print("Type 2 for Substraction")
print("Type 3 for Muliplication")
print("Type 4 for Division")
operation=input()
if operation =="1":
    num1= input("Enter first number: ")
    num2=input("Enter another number: ")
    print("The sum is ", float(num1)+float(num2))
elif operation =="2":
    num1= input("Enter first number: ")
    num2=input("Enter another number: ")
    print("The difference is " , float(num1)-float(num2))
elif operation =="3":
    num1= input("Enter first number: ")
    num2=input("Enter another number: ")
    print("The product is " , float(num1)*float(num2))
elif operation =="4":
    num1= input("Enter first number: ")
    num2=input("Enter another number: ")
    print("The quotient is " , float(num1)/float(num2))
else:
    print("Invalid Entry")
input()