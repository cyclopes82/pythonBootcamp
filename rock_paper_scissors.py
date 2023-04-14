print("......Rock.......")
print("......Paper.......")
print("......Scissors.......")

player1_input = input("(enter Player 1's choice): ")

print("*************NO CHEATING**************\n\n" * 30)

player2_input = input("(enter Player 2's choice): ")




if player1_input == player2_input:
    print("Game Draw")
elif player1_input == 'rock' and player2_input == "scissor":
    print("Player1 Wins")
elif player1_input == "paper" and player2_input == "rock":
    print("Player1 Wins")
elif player1_input == "scissor" and player2_input == "paper":
    print("Player1 Wins")
else:
    print("Player 2 Wins")