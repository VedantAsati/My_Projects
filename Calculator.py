print("Welcome to Calcuator")
print("====================")

while(True):
     
    operation = input("Press:\n + For Addition\n - For Subtraction\n * For Multiplication\n / For Division\n **2 For Square\n **3 For Cube\n Enter: ")
    print("====================")

    if operation == ("+"):
        Number_1 = float(input("Enter your number: "))
        Number_2 = float(input("Enter your number: "))
        print("===========================================")
        print("Addition is:", float(Number_1) + float(Number_2))
        print("===========================================")

    elif operation == ("-"):
        Number_1 = float(input("Enter your number: "))
        Number_2 = float(input("Enter your number: "))
        print("===========================================")
        print("Subtraction is:", float(Number_1) - float(Number_2))
        print("===========================================")

    elif operation == ("*"):
        Number_1 = float(input("Enter your number: "))
        Number_2 = float(input("Enter your number: "))
        print("===========================================")
        print("Multiplication tion is:", float(Number_1) * float(Number_2))
        print("===========================================")

    elif operation == ("/"):
        Number_1 = float(input("Enter your number: "))
        Number_2 = float(input("Enter your number: "))
        print("===========================================")
        print("Division is:", float(Number_1) / float(Number_2))
        print("===========================================")

    elif operation == ("**2"):
        Number_1 = float(input("Enter your number: "))
        print("===========================================")
        print("Square is:", float(Number_1)**2 )
        print("===========================================")

    elif operation == ("**3"):
        Number_1 = float(input("Enter your number: "))
        print("===========================================")
        print("Cube is:", float(Number_1)**3 )
        print("===========================================")

    else:
        print("Invalid Input!!!")
        print("===========================================")