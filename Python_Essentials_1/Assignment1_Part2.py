First_Name = input("Enter First Name")
Last_Name = input("Enter Last Name")
Age = input("Enter Age: ")
try:
    Age_Int = int(Age)
    if Age_Int < 0:
        print("Age cant be negative")
    else:
        print("Full Name: ", First_Name + Last_Name)
        print("You will be " + str(Age_Int) + " next year")
except:
    print("Invalid Age Input")
