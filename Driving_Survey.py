name = input("Please, Enter your name: ")

if name.endswith("i"):
    print("Welcome Miss", name)
else:
    print("Welcome Master", name)
print("==========================")

while(True):

    print("So, What's your age", name)
    age = int(input("Enter: "))
    print("==========================")

    if age == 18:
        print("Ohhh...sorry, We need some time to decide that you can drive or not")
        print("==============================================================")

    elif age <= 7:
        print("Majak chal raha hai kya yaha ?")
        print("==============================")

    elif age > 70:
        print("Sorry, You are too aged for driving")
        print("===================================")
        
    elif age > 18 and age < 70:
        print("Wnonderful, You can drive")
        print("=========================")
        
    elif age > 7 and age < 18:
        print("You are too small for driving")
        print("=============================")
        break