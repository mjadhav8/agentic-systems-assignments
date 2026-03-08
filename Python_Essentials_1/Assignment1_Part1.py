num1 = input("Enter first number : ")
num2 = input("Enter second number : ")

try:
    int_num1 = int(num1)
    int_num2 = int(num2)

    if int_num2==0:
        print("Cannot Divide by Zero")
    else:
        print("Sum of the numbers is : ", int(int_num1+int_num2))
    print("Division of numbers is : ", int(int_num1/int_num2))


except:
    print("Invalid Input")
        
