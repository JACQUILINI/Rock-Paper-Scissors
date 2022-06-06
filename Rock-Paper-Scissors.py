# Rock, Paper, Scissors task

# Import a random module
import random

#Declaring accepted variables
possible_option = ["R", "P", "S" ]



#requesting player's input
def player_choice():
    players_input = str(input("Enter your choice: " ))
    upper_players_input= players_input.upper()
    if upper_players_input == "R":
        return upper_players_input
    elif upper_players_input == "P":
        return upper_players_input
    elif upper_players_input == "S":
        
        return upper_players_input
    else:
        return "Invalid input"

# Computer's  choice
def cpu_choice():
    cpu_input = random.choice(possible_option)
    return cpu_input


# printing their both choices
def print_choices(x, y):
    print ("You {} : CPU {}" .format(x, y))

# game engine

#Checking for a draw
def checker(x, y):
    if x == y:
        print_choices(x,y)
        print("A Tie!")
    #chenking for the winner
        main()
    elif x == "R":
        if y == "P":
            print_choices(x,y)
            print("CPU Wins!")
        else:print ("You {} : CPU {} \n You Win!" .format(x, y))
    elif x == "P":
        if y == "R":
            print_choices(x,y)
            print("You Win!")
        else: print ("You {} : CPU {} \n CPU Wins!" .format(x,y))
    elif x =="S":
        if y == "P":
            print_choices(x,y)
            print("You Win!")
        else: print ("You {} : CPU {} \n CPU Wins!" .format(x,y))
    return

# main funtion to link and run all functions
def main():

    print("Enter 'R' for Rock, 'P' for Paper, and 'S' For Scissors")

    players_move = player_choice()
    computer_move = cpu_choice()

    if players_move == "Invalid input":
        print("Invalid Input")
        main()
    else: pass

    checker(players_move, computer_move)

#Runnig the game.
main()