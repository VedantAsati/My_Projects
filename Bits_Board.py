import random
print("\nWelcome to the BitsBoard game!!\n")

name = input("Enter your name: ").capitalize()
print("Welcome {}!\n".format(name))

correct_greetings = ["Perfect!", "Good!", "Hmmm, impressive!", "Getting into groove...", "Excellent!"]
incorrect_greetings = ["Wrong answer!", "Better luck next time!", "Try again!"]

words_to_riddles = {"Vocabulary":"V_ca__la_y", "Language":"L__gu_g_", "Judge":"_ud_e", "Heart rate":"H__rt r__e", "Speed":"S___d", "Terrible":"T__r___e", "Frozen":"__oz_n", "Height":"H__gh_", "Attention":"__t_n___n", "Introvert":"___r_v__t"}

score = 0
for index, original_word in enumerate(words_to_riddles.keys()):
    
    for i in range(1, 4):
        print(f"Question {index+1}: {words_to_riddles[original_word]}")
        ans = input("Enter the answer: ")

        if ans.capitalize() == original_word:
            print(random.choice(correct_greetings))
            score += 1
            break

        else:
            print(random.choice(incorrect_greetings))
            print("Chances left:", 3 - i)
        
    print("The answer was {}.".format(original_word))
    print("\n---------------------------------------------------\n")

print("\nResults:")
print(f"{name}, you scored {score*10}% ({score}/10).")