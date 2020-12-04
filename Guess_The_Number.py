print("Welcome to Guess The Number")
print("===========================")

print("Rules:\n 1. You have seven guesses\n 2. You have to guess the number between '0' and '150'")
print("============================")

Num = 78

while(True):
    
    Number = int(input("Enter the number: "))

    if Number == Num:
        print("You Won")
        print("=======")

    elif Number > 150:
        print("You have to guess the number between '0' and '150'")
        print("==================================================")

    elif Number < 0:
        print("You have to guess the number between '0' and '150'")
        print("==================================================")

    elif Number < Num:
        print("Increase the number")
        print("===================")

    else:
        print("Decrease the Number")
        print("===================")