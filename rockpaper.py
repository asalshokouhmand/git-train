player_1 = input("Enter your choice: ")
player_2 = input("Enter your choice: ")


def game(player_1, player_2):
    if player_1 == "rock" and player_2 == "scissor":
        print("Player 1 wins!")
    elif player_1 == "rock" and player_2 == "paper":
        print("Player 2 wins!")
    elif player_1 == "rock" and player_2 == "rock":
        print("Draw")
    elif player_1 == "paper" and player_2 == "scissor":
        print("Player 1 wins!")
    elif player_1 == "paper" and player_2 == "rock":
        print("Player 2 wins!")
    elif player_1 == "paper" and player_2 == "paper":
        print("Draw")
    elif player_1 == "scissor" and player_2 == "paper":
        print("Player 1 wins!")
    elif player_1 == "scissor" and player_2 == "rock":
        print("Player 2 wins!")
    elif player_1 == "scissor" and player_2 == "scissor":
        print("Draw")


game(player_1, player_2)
