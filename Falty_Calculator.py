print("Welcome to Calcuator")
print("====================")

while(True):
     
    operation = int(input("Press:\n 1. For Addition\n 2. For Subtraction\n 3. For Multiplication\n 4. For Division\n 5. For Square\n 6. For Cube\n Enter: "))
    print("====================")

    if operation == 1:
        Number_1 = int(input("Enter your number: "))
        Number_2 = int(input("Enter your number: "))

        if Number_1 == 41 and Number_2 == 63:
            print("===========================================")
            print("Addition is:", 103)
            print("===========================================")

        else:    
            print("===========================================")
            print("Addition is:", int(Number_1) + int(Number_2))
            print("===========================================")

    elif operation == 2:
        Number_1 = int(input("Enter your number: "))
        Number_2 = int(input("Enter your number: "))

        if Number_1 == 94 and Number_2 == 56:
            print("===========================================")
            print("Subtraction is:", 34)
            print("===========================================")

        else:
            print("===========================================")
            print("Subtraction is:", int(Number_1) - int(Number_2))
            print("===========================================")

    elif operation == 3:
        Number_1 = int(input("Enter your number: "))
        Number_2 = int(input("Enter your number: "))

        if Number_1 == 54 and Number_2 == 6:
            print("===========================================")
            print("Addition is:", 326)
            print("===========================================")

        else:
            print("===========================================")
            print("Multiplication is:", int(Number_1) * int(Number_2))
            print("===========================================")

    elif operation == 4:
        Number_1 = int(input("Enter your number: "))
        Number_2 = int(input("Enter your number: "))
        print("===========================================")
        print("Division is:", int(Number_1) / int(Number_2))
        print("===========================================")

    elif operation == 5:
        Number_1 = int(input("Enter your number: "))
        print("===========================================")
        print("Square is:", int(Number_1)**2 )
        print("===========================================")

    elif operation == 6:
        Number_1 = int(input("Enter your number: "))
        print("===========================================")
        print("Cube is:", int(Number_1)**3 )
        print("===========================================")

    else:
        print("Invalid Input!!!")
        print("===========================================")