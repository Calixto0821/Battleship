from operator import truediv
import os
import random
import ship as S
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

def requestShipData(shipLength, user):
    if user.type == 1:
        print('Where is the origin from you first ship')
        originX = int(input('Coordinate X:'))
        originY = int(input('Coordinate Y:'))
    elif user.type == 2:
        originX = random.randint (1,8)
        originY = random.randint (1,8)
    else:
        print('Error with the User Type [S1]')

    validOrientation = False
    while not validOrientation:
        if user.type == 1:
            orientation = input('How do you want to orient this ship? [V] Vertical|[H] Horizontal: ')
            answer = orientation.upper()
            if answer == 'V' or answer == 'H':
                validOrientation = True
        elif user.type == 2:
            n_letter = random.randint(1,2)
            if n_letter == 1:
                orientation = 'V'
                validOrientation = True
            elif n_letter == 2:
                orientation = 'H'
                validOrientation = True
            else:
                print('Error with the automatic orientation')

    df = (shipLength-1)
    if orientation.upper() == 'V':
        endX = originX
        if originY-df>=1 and originY+df<=8:
            if user.type == 1:
                print('[1]. Your ship could end in X:{x} Y:{y}'.format(x=endX,y=originY-df))
                print('[2]. Your ship could end in X:{x} Y:{y}'.format(x=endX,y=originY+df))
            validOption = False
            while not validOption:
                option = int(input('Choose one between [1] and [2]: ')) if user.type == 1 else random.randint(1,2)
                if option == 1:
                    endY = originY-df
                    validOption = True
                elif option == 2:
                    endY = originY+df
                    validOption = True
        elif originY-df>=1:
            if user.type == 1:
                print('Your ship only can end in X:{x} Y:{y}'.format(x=endX,y=originY-df))
            endY = originY-df
        elif originY+df<=8:
            if user.type == 1:
                print('Your ship only can end in X:{x} Y:{y}'.format(x=endX,y=originY+df))
            endY = originY+df
    elif orientation.upper() == 'H':
        endY = originY
        if originX-(shipLength-1)>=1 and originX+df<=8:
            if user.type == 1:
                print('[1]. Your ship could end in X:{x} Y:{y}'.format(x=originX-df,y=endY))
                print('[2]. Your ship could end in X:{x} Y:{y}'.format(x=originX+df,y=endY))
            validOption = False
            while not validOption:
                option = int(input('Choose one between [1] and [2]: ')) if user == 1 else random.randint(1,2)
                if option == 1:
                    endX = originX-df
                    validOption = True
                elif option == 2:
                    endX = originX+df
                    validOption = True
        elif originX-df>=1:
            if user.type == 1:
                print('Your ship only can end in X:{x} Y:{y}'.format(x=originX-df,y=endY))
            endX = originX-df
        elif originX+df<=8:
            if user.type == 1: 
                print('Your ship only can end in X:{x} Y:{y}'.format(x=originX+df,y=endY))
            endX = originX+df
    if user.type == 1:
        print('The final coordinate is\nOrigin: [{xo},{yo}]\nEnd: [{xe},{ye}]'.format(xo=originX,yo=originY,xe=endX,ye=endY))
    cooOrigin = [originX,originY] #List with the coordinates [x,y]
    cooEnd = [endX,endY] #List with the coordinates [x,y]
    return {'Origin':cooOrigin,'End':cooEnd,'Orientation':orientation.upper()}

def putShipOnBoard(board,ship):
    if ship.orientation == 'V':
        itV = 1 if ship.origin[1]<ship.end[1] else -1
        for i in range(ship.origin[1],ship.end[1]+(itV),itV):
            board[i-1][ship.origin[0]-1] = ship.length #[Y][X]
            #ship.body.append([ship.origin[0],i])
    elif ship.orientation == 'H':
        itH = 1 if ship.origin[0]<ship.end[0] else -1
        for i in range(ship.origin[0],ship.end[0]+(itH),itH):
            board[ship.origin[1]-1][i-1] = ship.length #[Y][X]
            #ship.body.append([i,ship.origin[1]])
    else:
        print('Error wwith the ship Orientation (putShipOnBoard)')

def validSpace(board,ship, user):
    if ship.orientation == 'V':
        itV = 1 if ship.origin[1]<ship.end[1] else -1
        for i in range(ship.origin[1],ship.end[1]+(itV), itV):
            if board[i-1][ship.origin[0]-1] != ' ':
                if user.type == 1:
                    print('In the square [{}][{}] there is something'.format(ship.origin[1]+2,i))
                return False
            else:
                if user.type == 1:
                    print('The square [{}][{}] is free'.format(ship.origin[1],i))
        return True
    elif ship.orientation == 'H':
        itH = 1 if ship.origin[0]<ship.end[0] else -1
        for i in range(ship.origin[0],ship.end[0]+(itH), itH):
            if board[ship.origin[1]-1][i-1] != ' ':
                if user.type == 1:
                    print('In the square [{}][{}] there is something'.format(i,ship.origin[1]))
                return False
            else:
                if user.type == 1:
                    print('The square [{}][{}] is free'.format(i,ship.origin[1]))
        return True
    else:
        print('Error with the ship Orientation (putShipOnBoard)')

def chooseShipsPositions(shipsList, board, user):
    newShips = []
    for new_ship in shipsList:
        clearConsole()
        if user.type == 1:
            print('{}\'S FLEET\n'.format(user.name.upper()))
            drawBox(board)
        valid_ship = False
        while not valid_ship:
            if user.type == 1:              
                print('\nChoose the coordinates of your ship (Length {})'.format(new_ship.length))
            coo_ship = requestShipData(new_ship.length, user)
            new_ship = S.ship(new_ship.length,coo_ship['Origin'],coo_ship['End'],coo_ship['Orientation'])            
            if validSpace(board,new_ship, user):
                putShipOnBoard(board,new_ship)
                newShips.append(new_ship)        
                valid_ship = True
            else:
                if user.type == 1:
                    print('\nYOU WON\'T BE ABLE TO PUT YOUR SHIP THERE, BECAUSE ALREADY THERE IS ANOTHER ONE THERE.\nTRY ANOTHER COORDINATE') 
    os.system("pause")
    return newShips