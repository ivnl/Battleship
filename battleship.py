from random import randint
from collections import defaultdict

# users display board
displayboard = []

# ship placement board
answerboard = []

# dictionary of lists to store ship properties
ships = defaultdict(list)

# append all O's to display board and set all to false
def initialize_board(dis_board, ans_board):
    for x in range(5):
        dis_board.append(["O"] * 5)
        ans_board.append([False] * 5)

# reset board values for new game
def wipe_board(dis_board, ans_board):
    ships_sunk = 0
    for y in range(5):
        for x in range(5):
            displayboard[y][x] = "O"
            answerboard[y][x] = False

# display board to user
def print_board(board):
    for row in board:
        print(" ".join(row))

# randomize a number for ship placement purpose
def randomizer(board):
    return randint(0, len(board) - 1)

# generate the number of ships the user specified and set their positions on the boards
def generate_ships(num_ships, dis_board, ans_board):

    for i in range(num_ships):
        ship_row = randomizer(dis_board)
        ship_col = randomizer(dis_board)

        while(ans_board[ship_row][ship_col]==True):
            ship_row = randomizer(dis_board)
            ship_col = randomizer(dis_board)

        ans_board[ship_row][ship_col] = True

        ships[i].append(ship_row)
        ships[i].append(ship_col)


initialize_board(displayboard, answerboard)
play_again = "yes"

while play_again == "yes":

    ships_sunk = 0
    wipe_board(displayboard, answerboard)

    print("Let's play Battleship!\n")
    print_board(displayboard)

    # let user input the amount of ships they would like placed on the board
    num_ships = int(input("\nHow many ships to be placed? "))
    if num_ships>25: ###needs improvement
        print("Number of ships can't exceed size of the grid!")
        break

    generate_ships(num_ships, displayboard, answerboard)

    #print "Debug Row: {}".format(ship_row)
    #print "Debug Col: {}".format(ship_col)

    for turn in range(5):

        if ships_sunk == num_ships:
            print("\nYou sunk all the battleships! You win")
            break

        print("\nTurn", turn + 1)
        guess_row = int(input("\nGuess Row: "))
        guess_col = int(input("Guess Col: "))

        if answerboard[guess_row][guess_col] == True:
            print("\nCongratulations! You sunk a battleship at loc: ",guess_row, guess_col)
            displayboard[guess_row][guess_col] = "!"

            ships_sunk+=1
            print(num_ships-ships_sunk, "ships remaining")
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print("\nOops, that's not even in the ocean.")
            elif displayboard[guess_row][guess_col] == "X":
                print("\nYou guessed that one already.")
            else:
                print("\nYou didn't hit anything!")
                displayboard[guess_row][guess_col] = "X"

        print_board(displayboard)

        if turn == 4:
            print
            print("\nOut of turns, Game Over")

    play_again = input("Play again? (yes/no): ")
