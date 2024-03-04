# File Name : CS112_A1_T2_Game3_20230380

# Purpose: It is played by two people with a pile of coins
#         The players take turns removing a non-zero square number of coins
#        The player who removes the last coin wins

# Author:Marwan Tamer Sayed Ali

# ID : 20230380

import math
import random
print("Welcome To Subtract a Square Game.")
print("It is played by two people with a pile of coins.")
print("The players take turns removing a non-zero square number of coins.")
print("The player who removes the last coin wins.\n")

def player_move(player, coins): # Function to get a player's move
    print("Player" ,player,"'s turn.")
    while True:
        try:
            move = int(input("Choose the number of coins to remove: "))
            if move <= 0:  # Ensure the move is a positive integer
                print("Invalid input. Please enter a positive integer.")
                continue
            if move > coins:   # Ensure the move does not bigger than coins
                print("Invalid move. Please choose a number less than coins")
                continue
            if math.isqrt(move) ** 2 == move :  # Ensure the move is a square number
                return move
            
            else:
                print("Invalid move. Please choose a valid square number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")        

def subtract_square_game():  # The main function
    print("The coins value :")
    print("A) Input.\nB)Random value.")
    choice = input() 
    while True:   # Prompt user to choose whether to input coins manually or a random value
        if choice.upper()== "A":  # Check the case of char
            while True:
                try:
                    coins = int(input("Enter the number of coins: "))
                    if coins <= 0: # Ensure the number of coins is a positive integer
                        print("Invalid input. Please enter a positive integer.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer")
            break    
        elif choice.upper() == "B":   # Check the case of char
            coins = random.randint(1,100)   # The Random value between 1,100
            print("The value of coins :",coins)
            break
        else:
            print("Invalid input.Please choose from (A/B).  ")
            choice = input()        
    current_player = 1

    while coins > 0:
        move = player_move(current_player, coins)
        coins -= move
        print(move,"coins removed.",coins, "left ")
        print("=========================")

        if coins == 0:
            print("Player",current_player, "wins")
            break

        current_player = 3 - current_player
subtract_square_game()
while True:  # Loop to ask the player if they want to play again
    play_again = input("Do you want to play again ? ...(yes/no)")
    if play_again.lower() == "yes":
        subtract_square_game()
    else:
        print("Thank you for playing.")
        break