from tkinter import N
import functions as F
from ship import *
from player import *
F.clearConsole()

if F.mainMenu():
    F.clearConsole()
    playerPC = player('PC')
    player1 = player(input('Type your name: '))
    print('You have four ships \n - Two submarines [3 spaces]\n - One Destroyer [4 spaces]\n - One Aircraft carrier [5 spaces]')
    player1_Board = F.createBoard(8,8) #Board[row][column] | [Y][X]
    player1_AttackBoard = F.createBoard(8,8) #
    PC_Board = F.createBoard(8,8) #Board[row][column] | [Y][X]
    PC_AttackBoard = F.createBoard(8,8)
    F.drawBox(player1_Board)

    #Set up on the board Player ships
    sL3_1 = ship(3,[0,0],[0,0],'N')
    sL3_2 = ship(3,[0,0],[0,0],'N')
    sL4 = ship(4,[0,0],[0,0],'N')
    sL5 = ship(5,[0,0],[0,0],'N')
    playerShips = F.chooseShipsPositions([sL3_1,sL3_2,sL4,sL5], player1_Board,1)
    sL3_1 = playerShips[0]
    sL3_2 = playerShips[1]
    sL4 = playerShips[2]
    sL5 = playerShips[3]
    player1.setUpShips(sL3_1,sL3_2,sL4,sL5)
    
    #Set up on the board PC ships
    PC_sL3_1 = ship(3,[0,0],[0,0],'N')
    PC_sL3_2 = ship(3,[0,0],[0,0],'N')
    PC_sL4 = ship(4,[0,0],[0,0],'N')
    PC_sL5 = ship(5,[0,0],[0,0],'N')        
    PCShips = F.chooseShipsPositions([PC_sL3_1,PC_sL3_2,PC_sL4,PC_sL5], PC_Board,2)
    PC_sL3_1 = PCShips[0]
    PC_sL3_2 = PCShips[1]
    PC_sL4 = PCShips[2]
    PC_sL5 = PCShips[3]
    playerPC.setUpShips(PC_sL3_1,PC_sL3_2,PC_sL4,PC_sL5)
    
    F.drawBox(player1_Board)
    print('These are  your ships\nAre you ready for batte?')
    print('---------------------------------------------------------------------------------------')
    print('------------------------------------STAR THE GAME--------------------------------------')
    game = True
    while game:
        #Player1's turn
        print('---------------------------------------------------------------------------------------')
        print('{}\'S TURN\nThat is your Attack Board'.format(player1.name.upper()))
        F.drawBox(player1_AttackBoard)       
        playerAttack = player1.attackShip(player1_AttackBoard,PC_Board,1)
        if playerAttack[0]:
            print('You hit one ship!')
            print(checkStatus([PC_sL3_1,PC_sL3_2,PC_sL4,PC_sL5],playerAttack[1],playerAttack[2]))
            game = playerPC.checkShips(PCShips)
            if not game:
                F.drawBox(player1_AttackBoard)
                print('{}, YOU ARE THE WINNER!! CONGRATULATIONS!!'.format(player1.name))
                break
        else:
            print('Oh no! You hit the water')
        print('---------------------------------------------------------------------------------------')
        #PC's turn
        print('---------------------------------------------------------------------------------------')       
        print('{}\'S TURN'.format(playerPC.name))
        PCAttack = playerPC.attackShip(PC_AttackBoard,player1_Board,2)
        if PCAttack[0]:
            print('PC shot in [{X}][{Y}]'.format(X=PCAttack[1],Y=PCAttack[2]))
            print('PC hit one ship! :(')
            checkStatus([sL3_1,sL3_2,sL4,sL5],PCAttack[1],PCAttack[2])
            game = player1.checkShips(playerShips)
            if not game:
                print('OH NO, THE PC WON YOU :(')
                break
        else:
            print('PC hit the water...')
        F.drawBox(player1_Board)
        print('---------------------------------------------------------------------------------------')
else:
    print('We\'re still working in this part of the game')