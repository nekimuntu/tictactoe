import random
#1 Create a board
#2 Take player input
#3 Check if win or tie
#4 Switch player player
#5 Check if win or tie

board = ["_","_","_",
        "_","_","_",
        "_","_","_"]
currentPlayer = "X"
winner = None
gameRunning = True
nbIteration = 0

#1 
def printingBoard(board):
    print("__________")
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("__|___|___")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("__|___|___")
    print(board[6]+" | "+board[7]+" | "+board[8])
    print("__|___|___")

# printingBoard(board)


#2
def playerInput(board,nbIteration):
    global currentPlayer 
    if nbIteration == 0:        
        print("Welcome to the TicTacToe game")
        print("________________")
        print("_1_"+" | "+"_2_"+" | "+"_3_")
        print("____|_____|_____")
        print("_4_"+" | "+"_5_"+" | "+"_6_")
        print("____|_____|_____")
        print("_7_"+" | "+"_8_"+" | "+"_9_")
        print("____|_____|_____")
    try: 
        inp = int(input("Enter a number between 1 and 9:  "))
        if inp >= 1 and inp <= 9 and board[inp-1] == "_":
            board[inp-1] = currentPlayer
        else:
            print("Oooops this case is Already ticked")  
    except Exception:
        print("Oooops this is not a number Please try again")      
#3
def isItWin(board):
    #its a win for following combination of boxes ticked :
    #boxes 123 / 159 / 147 / 258 / 357 / 369 / 456 / 852 / 
    #Index Horizontal 012 345 678  Vertical 147 036 258 Diagonal 048 246  
    global winner
    #case horizontal 012 345 678
    if board[0]==board[1]==board[2] and board[0]!="_":
        winner = board[0]
        return True
    if board[3]==board[4]==board[5] and board[3]!="_":
        winner = board[3]
        return True
    if board[6]==board[7]==board[8] and board[6]!="_":
        winner = board[6]
        return True
    #case vertical 036 147 258
    if board[0]==board[3]==board[6] and board[0]!="_":
        winner = board[0]
        return True
    if board[1]==board[4]==board[7] and board[1]!="_":
        winner = board[1]
        return True
    if board[2]==board[5]==board[8] and board[2]!="_":
        winner = board[2]
        return True
    # case diagonale 048 246
    if board[0]==board[4]==board[8] and board[0]!="_":
        winner = board[0]
        return True
    if board[2]==board[4]==board[6] and board[2]!="_":
        winner = board[2]
        return True
    return False

def isItTie(board):
    global gameRunning
    if "_" not in board and gameRunning==True:        
        print("it's a tie")
        printingBoard(board) 
        gameRunning = False

def checkWin():
    global gameRunning,board, winner,nbIteration
    if isItWin(board) == True:
        print(currentPlayer, " is the Winner, Congrat")
        print("He won in ",nbIteration," steps")
        printingBoard(board)
        gameRunning = False
        
#4
def switchPlayer():
    global currentPlayer
    if currentPlayer=="X":
        currentPlayer= "O"
    else:
        currentPlayer="X"

def computerPlay(board):
    global currentPlayer
    index = random.randint(0,8)
    if currentPlayer == "O":
        if board[index]=="_":
            board[index]="O"
        printingBoard(board)

while gameRunning:    
    printingBoard(board)
    playerInput(board,nbIteration)
    nbIteration+=1
    checkWin()
    isItTie(board)
    switchPlayer()
    computerPlay(board)
    checkWin()
    isItTie(board)
    switchPlayer()