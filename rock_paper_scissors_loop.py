import random

print("......Rock.......")
print("......Paper.......")
print("......Scissors.......")





options = ['rock','paper','scissors']




player_wins = 0
computer_wins = 0

winnings = 3



while player_wins < winnings and computer_wins < winnings:

    print(f"Player wins: {player_wins}, Computer wins: {computer_wins}")

    player_input = input("(enter Your choice): ").lower()
    if player_input == "quit" or player_input == "q":
        break

    computer_choice = random.choice(options)
    print("Computer Plays: " + computer_choice)

    if player_input == computer_choice:
        print("Game Draw")
    elif player_input == 'rock' and computer_choice == "scissors":
        print("You Win")
        player_wins += 1
    elif player_input == "paper" and computer_choice == "rock":
        print("You Win")
        player_wins += 1
    elif player_input == "scissors" and computer_choice == "paper":
        print("You Win")
        player_wins += 1
    else:
        print("Computer Wins")
        computer_wins += 1


print(f"Final Scores: Player wins: {player_wins}, Computer wins: {computer_wins}")
if player_wins > computer_wins:
    print("Congratulations!!! You Win!!")
elif player_wins == computer_wins:
    print("It's a tie")
else:
    print("Oh no.... Computer wins!!! :()")
