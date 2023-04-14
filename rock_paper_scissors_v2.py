import random

print("......Rock.......")
print("......Paper.......")
print("......Scissors.......")



player_input = input("(enter Player 1's choice): ").lower()

print("*************NO CHEATING**************\n\n" * 30)

options = ['rock','paper','scissor']

computer_choice = random.choice(options)
print("Computer Plays: " + computer_choice)




if player_input == computer_choice:
    print("Game Draw")
elif player_input == 'rock' and computer_choice == "scissor":
    print("You Win")
elif player_input == "paper" and computer_choice == "rock":
    print("You Win")
elif player_input == "scissor" and computer_choice == "paper":
    print("You Win")
else:
    print("Computer Wins")