import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("===== ROCK PAPER SCISSORS GAME =====")
print("Instructions:")
print("Type rock, paper, or scissors to play.\n")

while True:

    user_choice = input("Enter your choice: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Try again.")
        continue

    
    computer_choice = random.choice(choices)

    print("\nYou chose:", user_choice)
    print("Computer chose:", computer_choice)
    if user_choice == computer_choice:
        print("Result: It's a Tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("Result: You Win! 🎉")
        user_score += 1

    else:
        print("Result: Computer Wins!")
        computer_score += 1
    print("\nScore Board")
    print("You:", user_score)
    print("Computer:", computer_score)

    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("\nFinal Score -> You:", user_score, "| Computer:", computer_score)
        print("Thanks for playing!")
        break