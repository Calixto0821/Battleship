from tkinter import N
import functions as F
from ship import *
from player import *
#F.clearConsole()

if F.mainMenu():
    #F.clearConsole()
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
    newPlayerShips = F.chooseShipsPositions([sL3_1,sL3_2,sL4,sL5], player1_Board,1)
    sL3_1 = newPlayerShips[0]
    sL3_2 = newPlayerShips[1]
    sL4 = newPlayerShips[2]
    sL5 = newPlayerShips[3]

    #Set up on the board PC ships
    PC_sL3_1 = ship(3,[0,0],[0,0],'N')
    PC_sL3_2 = ship(3,[0,0],[0,0],'N')
    PC_sL4 = ship(4,[0,0],[0,0],'N')
    PC_sL5 = ship(5,[0,0],[0,0],'N')        
    newPCShips = F.chooseShipsPositions([PC_sL3_1,PC_sL3_2,PC_sL4,PC_sL5], PC_Board,2)
    PC_sL3_1 = newPCShips[0]
    PC_sL3_2 = newPCShips[1]
    PC_sL4 = newPCShips[2]
    PC_sL5 = newPCShips[3]
    print('---------------------------------------------------------------------------------------')
    print('------------------------------------STAR THE GAME--------------------------------------')
    F.drawBox(PC_Board) #Plot enemy board

    print('\nPlayer Bodys\n')
    print(sL3_1.body,sL3_2.body,sL4.body,sL5.body, sep='\n')
    
    """player1.attackShip(player1_AttackBoard,PC_Board,1)
    F.drawBox(player1_AttackBoard)
    F.drawBox(PC_Board)
    player1.attackShip(player1_AttackBoard,PC_Board,1)
    F.drawBox(player1_AttackBoard)
    F.drawBox(PC_Board)"""
else:
    print('The first player choose the positions')