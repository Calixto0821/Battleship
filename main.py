import functions as F
from ship import *
from player import *
import os
F.clearConsole()

if F.mainMenu():
    F.clearConsole()
    playerPC = player('PC',2)
    player1 = player(input('Type your name: '),1)
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
    playerShips = F.chooseShipsPositions([sL3_1,sL3_2,sL4,sL5], player1_Board,player1)
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
    PCShips = F.chooseShipsPositions([PC_sL3_1,PC_sL3_2,PC_sL4,PC_sL5], PC_Board,playerPC)
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
                print('---------------------------------------------------------------------------------------')
                winner = player1
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
                print('---------------------------------------------------------------------------------------')
                winner = playerPC
                break
        else:
            print('PC hit the water...')
        F.drawBox(player1_Board)
        print('---------------------------------------------------------------------------------------')
    print('--------------------------------------STATISTICS---------------------------------------')
    player1.printStatistics()
    print('---------------------------------------------------------------------------------------')
    playerPC.printStatistics()
else:
    F.clearConsole()
    player1 = player(input('First player, type your name: '),1)
    F.clearConsole()
    player2 = player(input('Second player, type your name: '),1)
    print('Ecah player has four ships \n - Two submarines [3 spaces]\n - One Destroyer [4 spaces]\n - One Aircraft carrier [5 spaces]')
    player1_Board = F.createBoard(8,8) #Board[row][column] | [Y][X]
    player1_AttackBoard = F.createBoard(8,8) #
    player2_Board = F.createBoard(8,8) #Board[row][column] | [Y][X]
    player2_AttackBoard = F.createBoard(8,8)

    #Set up on the board Player ships
    player1_sL3_1 = ship(3,[0,0],[0,0],'N')
    player1_sL3_2 = ship(3,[0,0],[0,0],'N')
    player1_sL4 = ship(4,[0,0],[0,0],'N')
    player1_sL5 = ship(5,[0,0],[0,0],'N')
    F.drawBox(player1_Board)
    player1Ships = F.chooseShipsPositions([player1_sL3_1,player1_sL3_2,player1_sL4,player1_sL5], player1_Board,player1)
    player1_sL3_1 = player1Ships[0]
    player1_sL3_2 = player1Ships[1]
    player1_sL4 = player1Ships[2]
    player1_sL5 = player1Ships[3]
    player1.setUpShips(player1_sL3_1,player1_sL3_2,player1_sL4,player1_sL5)
    
    #Set up on the board PC ships
    player2_sL3_1 = ship(3,[0,0],[0,0],'N')
    player2_sL3_2 = ship(3,[0,0],[0,0],'N')
    player2_sL4 = ship(4,[0,0],[0,0],'N')
    player2_sL5 = ship(5,[0,0],[0,0],'N')        
    F.drawBox(player2_Board)
    player2Ships = F.chooseShipsPositions([player2_sL3_1,player2_sL3_2,player2_sL4,player2_sL5], player2_Board,player2)
    player2_sL3_1 = player2Ships[0]
    player2_sL3_2 = player2Ships[1]
    player2_sL4 = player2Ships[2]
    player2_sL5 = player2Ships[3]
    player2.setUpShips(player2_sL3_1,player2_sL3_2,player2_sL4,player2_sL5)
    
    F.clearConsole()
    print('---------------------------------------------------------------------------------------')
    print('------------------------------------STAR THE GAME--------------------------------------')
    game = True
    while game:
        #Player1's turn
        print('---------------------------------------------------------------------------------------')
        print('{}\'S TURN\nThat is your Attack Board'.format(player1.name.upper()))
        F.drawBox(player1_AttackBoard)       
        playerAttack = player1.attackShip(player1_AttackBoard,player2_Board,player1)
        if playerAttack[0]:
            print('{} hit one ship!'.format(player1.name.capitalize()))
            print(checkStatus([player2_sL3_1,player2_sL3_2,player2_sL4,player2_sL5],playerAttack[1],playerAttack[2]))
            game = player2.checkShips(player2Ships)
            if not game:
                F.drawBox(player1_AttackBoard)
                print('{}, YOU ARE THE WINNER!! CONGRATULATIONS!!'.format(player1.name))
                print('---------------------------------------------------------------------------------------')
                winner = player1
                break
        else:
            print('Oh no! You hit the water')
        print('---------------------------------------------------------------------------------------')
        os.system("pause")
        F.clearConsole()
        #Player2's turn
        print('---------------------------------------------------------------------------------------')       
        print('{}\'S TURN'.format(player2.name.upper()))
        F.drawBox(player2_AttackBoard)
        PCAttack = player2.attackShip(player2_AttackBoard,player1_Board,player2)
        if PCAttack[0]:
            print('{} hit one ship!'.format(player2.name.capitalize()))
            checkStatus([player1_sL3_1,player1_sL3_2,player1_sL4,player1_sL5],PCAttack[1],PCAttack[2])
            game = player1.checkShips(player1Ships)
            if not game:
                print('{}, YOU ARE THE WINNER!! CONGRATULATIONS!!'.format(player2.name))
                print('---------------------------------------------------------------------------------------')
                winner = player2
                break
        else:
            print('Oh no! You hit the water')
        print('---------------------------------------------------------------------------------------')
        os.system("pause")
        F.clearConsole()

        print('DATA GAME\n----------------------------')
        print('PLAYER 1')
        F.drawBox(player1_Board)
        player1.printData()
        print('----------------------------')
        print('PLAYER 2')
        F.drawBox(player2_Board)
        player2.printData()
        os.system("pause")


    print('--------------------------------------STATISTICS---------------------------------------')
    player1.printStatistics()
    print('---------------------------------------------------------------------------------------')
    player2.printStatistics()