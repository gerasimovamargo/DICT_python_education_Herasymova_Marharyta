import sys
import os
import time

# A list that will store the player's choice in the future, namely the CROSS or NULL in one or another position on
# the playing field
blist = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# Variables for game workflows, as well as checks for wins and draws
game_win = True
game_draw = -1
game_run = False
our_game = game_run


def board():
    """In this function, we draw the playing field and add empty cells to it from the list for future storage of the
    CROSS or TOKE"""
    print("\n")
    print("\t      |      |")
    print(f"\t   {blist[1]}  |  {blist[2]}   |  {blist[3]}")
    print('\t______|______|______')
    print("\t      |      |")

    print(f"\t   {blist[4]}  |  {blist[5]}   |  {blist[6]}")
    print('\t______|______|______')
    print("\t      |      |")

    print(f"\t   {blist[7]}  |  {blist[8]}   |  {blist[9]}")
    print("\t      |      |")
    print("\n")


def win_or_not():
    """In this function, we check whether this or that player has won using different combinations."""
    global our_game
    if blist[1] == blist[2] and blist[2] == blist[3] and blist[1] != ' ':
        our_game = game_win
    elif blist[4] == blist[5] and blist[5] == blist[6] and blist[4] != ' ':
        our_game = game_win
    elif blist[7] == blist[8] and blist[8] == blist[9] and blist[7] != ' ':
        our_game = game_win
    elif blist[1] == blist[4] and blist[4] == blist[7] and blist[1] != ' ':
        our_game = game_win
    elif blist[2] == blist[5] and blist[5] == blist[8] and blist[2] != ' ':
        our_game = game_win
    elif blist[3] == blist[6] and blist[6] == blist[9] and blist[3] != ' ':
        our_game = game_win
    elif blist[1] == blist[5] and blist[5] == blist[9] and blist[5] != ' ':
        our_game = game_win
    elif blist[3] == blist[5] and blist[5] == blist[7] and blist[5] != ' ':
        our_game = game_win
    elif (blist[1] != ' ' and blist[2] != ' ' and blist[3] != ' ' and blist[4] != ' '
          and blist[5] != ' ' and blist[6] != ' ' and blist[7] != ' ' and
          blist[8] != ' ' and blist[9] != ' '):
        our_game = game_draw


def pos(x):
    """Function to check if cells are empty or not"""
    if blist[x] == ' ':
        return True
    else:
        print("\nThis cell is already taken!")
        return False


def restart():
    """Function to prompt the player to restart the game"""
    users_input = input("Do you want to restart the game?Write \"YES\" or \"NO\" -->")
    while users_input != 0:
        if users_input == "YES":
            print("Loading...")
            time.sleep(5)
            os.system("python main.py")
            exit()
        elif users_input == "NO":
            print("Loading...")
            time.sleep(5)
            sys.exit("Goodbye!")
        else:
            print("Invalid Choice!")


def how_is_winner(player):
    """Function to check the draw and which particular player has won"""
    if our_game == game_draw:
        print("Game Draw")
    elif our_game == game_win:
        player -= 1
        if player % 2 != 0:
            print("Player 1 Won""\nThanks for playing!")
            restart()
        else:
            print("Player 2 Won""\nThanks for playing!")
            restart()


def process_game():
    """The main function of the game in which there is a change in the turn of the players and the provision of a
    choice of position on the playing field """
    player = 1
    while our_game == game_run:
        board()
        if player % 2 != 0:
            print("Player 1's chance")
            mark = 'X'
        else:
            print("Player 2's chance")
            mark = '0'
        try:
            choice = int(input("Enter the position between [1-9] where you want to mark:"))
        except ValueError:
            print("Invalid Input!!! Try Again")
            continue
        if choice < 1 or choice > 9:
            print("Invalid Input!!! Try Again")
            continue
        if pos(choice):
            blist[choice] = mark
            player += 1
            win_or_not()
    board()
    how_is_winner(player)


def menu():
    """Prints for menu function"""
    print("1.Start game")
    print("2.Exit")


menu()
# Game start menu
menu_input = int(input("Enter your choice -->"))
while menu_input != 0:
    if menu_input == 1:
        print("Loading...")
        time.sleep(5)
        process_game()
        pass
    elif menu_input == 2:
        sys.exit("Goodbye!")
        pass
    else:
        print("Invalid Choice!")

    menu()
    menu_input = int(input("Enter your choice -->"))
