# Rock, Paper, Scissors tas
import random
possible_option = ["R", "P", "S" ]

def player_choice():
    #requesting player's input
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

# Computers  choice
def cpu_choice():
    cpu_input = random.choice(possible_option)
    return cpu_input
# printing their both choices
def print_choices(x, y):
    print ("You {} : CPU {}" .format(x, y))

# game engine
def checker(x, y):
    if x == y:
        print_choices(x,y)
        print("A Tie!")
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
    players_move = player_choice()
    computer_move = cpu_choice()

    if players_move == "Invalid input":
        print("Invalid Input")
        main()
    else: pass

    checker(players_move, computer_move)

main()