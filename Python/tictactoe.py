import os

#defining varibles
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
turn = True
moves = 0

#Fucntion that prints the game board to the command window
def printBoard():
    print("%s | %s | %s" % (board[0], board[1], board[2]))
    print("---------")
    print("%s | %s | %s" % (board[3], board[4], board[5]))
    print("---------")
    print("%s | %s | %s" % (board[6], board[7], board[8]))

#Function that checks if there is a winner
def checkWinner():
    if((board[0] == board[1] and board[1] == board[2]) or (board[3] == board[4] and board[4] == board[5]) or (board[6] == board[7] and board[7] == board[8])
    or (board[0] == board[3] and board[3] == board[6]) or (board[1] == board[4] and board[4] == board[7]) or (board[2] == board[5] and board[5] == board[8])
    or (board[0] == board[4] and board[4] == board[8]) or (board[2] == board[4] and board[4] == board[6])):
        return True
    else:
        return False

#Print the initial board
printBoard()

#Game Loop
while(True):
    if(turn):
        player = "Player 1"
    else:
        player = "Player 2"

    try:    
        inp = input("%s Please Enter a Number:" % (player))
        if(inp < 1 or inp > 9):
            os.system("cls")
            printBoard()
            print("Please Enter a valid Number:")
        else:
            if(board[inp - 1] != 'X' and board[inp - 1] != 'O'):
                if(turn):
                    board[inp - 1] = "X"
                    moves = moves + 1
                else:
                    board[inp - 1] = "O"
                    moves = moves + 1
                os.system("cls")
                printBoard()
                
                if(checkWinner()):
                    if(turn):
                        print("Player 1 is the Winner!")
                    else:
                        print("Player 2 is the Winner!")
                    break

                if(turn):
                    turn = False
                else:
                    turn = True

                if(moves == 9):
                    print("Board is full, No Winner.")
                    break
            else:
                os.system("cls")
                printBoard()
                print("That spot is already taken.")
    except:
        os.system("cls")
        printBoard()
        print("That is not a valid Number")

input("Press any Key to Continue.")