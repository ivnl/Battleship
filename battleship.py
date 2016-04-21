from random import randint
from collections import defaultdict

board = []

for x in range(5):
    board.append(["O"] * 5)


def print_board(board):
    for row in board:
        print(" ".join(row))

def randomizer(board):
    return randint(0, len(board) - 1)




print("Let's play Battleship!")
print_board(board)

num_ships = int(input("How many ships to be placed? #Greater than 0"))
ships = defaultdict(list)

def generate_ships(num_ships, board):

    for i in range(num_ships):
        ship_row = randomizer(board)
        ship_col = randomizer(board)
        ships[i].append(ship_row)
        ships[i].append(ship_col)



    print(ships[0])
    print(ships[1])
    print(ships[2])
generate_ships(num_ships, board)


# def random_row(board):
#     return randint(0, len(board) - 1)
#
#
# def random_col(board):
#     return randint(0, len(board[0]) - 1)
#
# ship_row = random_row(board)
# ship_col = random_col(board)


print
#print "Debug Row: {}".format(ship_row)
#print "Debug Col: {}".format(ship_col)
print


for turn in range(5):
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    all_destroyed = False

    if all_destroyed == True:
        print("You sunk all the battleships! You win")

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk a battleship!")
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        print ("Turn", turn + 1)
        print_board(board)
    if turn == 3:
        print
        print("Game Over")
