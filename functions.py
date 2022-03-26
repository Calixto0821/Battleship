import os
def title():
    print('88888888ba                                 88                         88           88               ')
    print('88      "8b                ,d       ,d     88                         88           ""               ')               
    print('88      ,8P                88       88     88                         88                            ')
    print('88aaaaaa8P\'  ,adPPYYba,  MM88MMM  MM88MMM  88   ,adPPYba,  ,adPPYba,  88,dPPYba,   88  8b,dPPYba,   ')
    print('88""""""8b,  ""     `Y8    88       88     88  a8P_____88  I8[    ""  88P\'    "8a  88  88P\'    "8a  ')
    print('88      `8b  ,adPPPPP88    88       88     88  8PP"""""""   `"Y8ba,   88       88  88  88       d8  ')
    print('88      a8P  88,    ,88    88,      88,    88  "8b,   ,aa  aa    ]8I  88       88  88  88b,   ,a8"  ')
    print('88888888P"   `"8bbdP"Y8    "Y888    "Y888  88   `"Ybbd8"\'  `"YbbdP"\'  88       88  88  88`YbbdP"\'   ')
    print('                                                                                       88           ')
    print('                                                                                       88           ')
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    title()
def createBoard(rows, columns):
    cont = 1
    board = []
    for r in range(rows):
        board.append([])
        for c in range(columns):
                board[r].append(' ')
                cont += 1
    return board
def drawBox(board):   
    print("     1   2   3   4   5   6   7   8  ")
    print("   +---+---+---+---+---+---+---+---+")
    currentRow= 1
    for row in board:
        print(" {file} | {c1} | {c2} | {c3} | {c4} | {c5} | {c6} | {c7} | {c8} |"
        .format(
        file=currentRow,
        c1=row[0],
        c2=row[1],
        c3=row[2],
        c4=row[3],
        c5=row[4],
        c6=row[5],
        c7=row[6],
        c8=row[7]))
        print("   +---+---+---+---+---+---+---+---+")
        currentRow += 1
def mainMenu():
    print('1. Plyer vs PC')#Return True
    print('2. Multiplayer')#Return False
    validAnswer = False
    while not validAnswer:
        try:
            answer = int(input('Choose one mood game: '))
        except ValueError:
            print('Try again')
        else:
            if answer == 1:
                validAnswer = True
                return True
            elif answer == 2:
                validAnswer = True
                return False     