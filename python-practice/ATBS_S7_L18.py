# ATBS_S7_L18.py is a proram that wrote to test my understanding of
# Automate the boring stuff Section 6, Lecture 18

# Data Structures

# Custom data structure tic tac toe
board = {'TL': ' ', 'TM': ' ', 'TR': ' ',
         'ML': ' ', 'MM': ' ', 'MR': ' ',
         'BL': ' ', 'BM': ' ', 'BR': ' '}


# function to print tic tac toe board

def printboardpositions():
    print("\nYou can use below reference\n")
    print('TL' + ' | ' + 'TM' + ' | ' + 'TR')
    print("------------")
    print('ML' + ' | ' + 'MM' + ' | ' + 'MR')
    print("------------")
    print('BL' + ' | ' + 'BM' + ' | ' + 'BR')
    print('\n')


def printboard(board):
    print(board['TL'] + ' | ' + board['TM'] + ' | ' + board['TR'])
    print("----------")
    print(board['ML'] + ' | ' + board['MM'] + ' | ' + board['MR'])
    print("----------")
    print(board['BL'] + ' | ' + board['BM'] + ' | ' + board['BR'])
    print('\n')


# function to chose a side X or O
def chooseside():
    playerside = ""
    while playerside == "":
        print("Choose your mark by entering X or O")
        playerinput = input().upper()
        if playerinput == 'X':
            playerside = 'X'
        elif playerinput == 'O':
            playerside = 'O'
    print("You chose " + playerside)
    return playerside


def checkwinner(side):
    print('This function returns true if there is a winner')
    if (
        # top horizontal
        (board['TL'] == board['TM'] == board['TR'] == side) or
        # middle horizontal
        (board['ML'] == board['MM'] == board['MR'] == side) or
        # bottom horizontal
        (board['BL'] == board['BM'] == board['BR'] == side) or
        # left vertical
        (board['TL'] == board['ML'] == board['BL'] == side) or
        # middle vertical
        (board['TM'] == board['MM'] == board['BM'] == side) or
        # right vertical
        (board['TR'] == board['MR'] == board['BR'] == side) or
        # left top right bottom
        (board['TL'] == board['MM'] == board['BR'] == side) or
        # right top left bottom
        (board['BL'] == board['MM'] == board['TR'] == side)):
        print(side + ' is a winner')
        return True
    else:
        return False


def checkboardspace(board):
    print('This function returns true if board has space')
    checkboardspace = False
    for i in board.keys():
        print("checking " + i)
        if board[i] == ' ':
            print(i + 'is empty')
            checkboardspace = True
            break
    return checkboardspace


def getplayerinput(board, playerside):
    print("This is the current board")
    printboard(board)
    playerinputposition = ''
    while playerinputposition == '':
        print('Please select the new position')
        printboardpositions()
        playerinput = input().upper()
        if playerinput in board:
            if board[playerinput] in ('X', 'Y'):
                print('This position already has data')
                printboard(board)
            elif board[playerinput] == ' ':
                playerinputposition = playerinput
                board[playerinputposition] = playerside
    return board


def getcominput(board, compside):
    print("This is the current board")
    printboard(board)
    playerinputposition = ''
    while playerinputposition == '':
        print('Please select the new position, using below template')
        printboardpositions()
        playerinput = input().upper()
        if playerinput in board:
            if board[playerinput] in ('X', 'Y'):
                print('This position already has data')
                printboard(board)
            elif board[playerinput] == ' ':
                playerinputposition = playerinput
                board[playerinputposition] = playerside
    return board


print("Lets play a game of tic tac toe")
playerside = chooseside()
if playerside == 'X':
    compside = 'O'
    nextturn = 'player'
else:
    compside = 'X'
    nextturn = 'comp'

while checkboardspace(board):
    if nextturn == 'player':
        printboard(getplayerinput(board, playerside))
        if checkwinner(playerside):
            print(nextturn + ' Has wan')
            break
        else:
            nextturn = 'comp'
    elif nextturn == 'comp':
        printboard(getcominput(board, compside))
        if checkwinner(compside):
            print(nextturn + ' Has wan')
            break
        else:
            nextturn = 'player'

printboardpositions()

board['TL'] = 'X'
board['TM'] = 'O'
board['TR'] = 'O'

printboard(board)
printboard(board)
checkboardspace(board)


# i = 0
# while i < 1:
#     if checkboardspace(board):
#
#
#     else
#         no empty spaces left, better luck next time


if checkwinner("O"):
    print("game finished")
