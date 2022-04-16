import functions as F
from ship import *
from player import *
import os
F.clearConsole()

gameMode = F.mainMenu()
player1 = player(input('Type your name: '),1)
print('You have four ships \n - Two submarines [3 spaces]\n - One Destroyer [4 spaces]\n - One Aircraft carrier [5 spaces]')
player1_Board = F.createBoard(8,8) #Board[row][column] | [Y][X]
player1_AttackBoard = F.createBoard(8,8) #
F.drawBox(player1_Board)
#Set up on the board Player ships
player1_sL3_1 = ship(3,[0,0],[0,0],'N')
player1_sL3_2 = ship(3,[0,0],[0,0],'N')
player1_sL4 = ship(4,[0,0],[0,0],'N')
player1_sL5 = ship(5,[0,0],[0,0],'N')
player1Ships = F.chooseShipsPositions([player1_sL3_1,player1_sL3_2,player1_sL4,player1_sL5], player1_Board,player1)
player1_sL3_1 = player1Ships[0]
player1_sL3_2 = player1Ships[1]
player1_sL4 = player1Ships[2]
player1_sL5 = player1Ships[3]
player1.setUpShips(player1_sL3_1,player1_sL3_2,player1_sL4,player1_sL5)

if gameMode:
    F.clearConsole()
    playerEnemy = player('PC',2)
    Enemy_Board = F.createBoard(8,8)
    Enemy_AttackBoard = F.createBoard(8,8)
else:
    F.clearConsole()
    playerEnemy = player(input('Second player, type your name: '),1)
    print('Ecah player has four ships \n - Two submarines [3 spaces]\n - One Destroyer [4 spaces]\n - One Aircraft carrier [5 spaces]')
    Enemy_Board = F.createBoard(8,8) #Board[row][column] | [Y][X]
    Enemy_AttackBoard = F.createBoard(8,8)

#Set up on the board PC ships
enemy_sL3_1 = ship(3,[0,0],[0,0],'N')
enemy_sL3_2 = ship(3,[0,0],[0,0],'N')
enemy_sL4 = ship(4,[0,0],[0,0],'N')
enemy_sL5 = ship(5,[0,0],[0,0],'N')        
enemyShips = F.chooseShipsPositions([enemy_sL3_1,enemy_sL3_2,enemy_sL4,enemy_sL5], Enemy_Board,playerEnemy)
enemy_sL3_1 = enemyShips[0]
enemy_sL3_2 = enemyShips[1]
enemy_sL4 = enemyShips[2]
enemy_sL5 = enemyShips[3]
playerEnemy.setUpShips(enemy_sL3_1,enemy_sL3_2,enemy_sL4,enemy_sL5)
    
if gameMode:
    F.drawBox(player1_Board)
    print('These are  your ships\nAre you ready for batte?')
    os.system("pause")
F.clearConsole()
    
    
print('---------------------------------------------------------------------------------------')
print('------------------------------------STAR THE GAME--------------------------------------')
game = True
while game:
    #Player1's turn
    print('---------------------------------------------------------------------------------------')
    print('{}\'S TURN\nThat is your Attack Board'.format(player1.name.upper()))
    F.drawBox(player1_AttackBoard)       
    playerAttack = player1.attackShip(player1_AttackBoard,Enemy_Board,player1)
    if playerAttack[0]:
        print('{} hit one ship!'.format(player1.name.capitalize()))
        print(checkStatus(enemyShips,playerAttack[1],playerAttack[2]))
        game = playerEnemy.checkShips(enemyShips)
        if not game:
            F.clearConsole()
            F.drawBox(player1_AttackBoard)
            print('{}, ARE THE WINNER!! CONGRATULATIONS!!'.format(player1.name))
            print('---------------------------------------------------------------------------------------')
            winner = player1
            break
    else:
        print('Oh no! You hit the water')
    print('---------------------------------------------------------------------------------------')
    os.system("pause")
    F.clearConsole()

    #Enemy's turn
    print('---------------------------------------------------------------------------------------')       
    print('{}\'S TURN'.format(playerEnemy.name.upper()))
    if gameMode == False:
        F.drawBox(Enemy_AttackBoard)
    enemyAttack = playerEnemy.attackShip(Enemy_AttackBoard,player1_Board,playerEnemy)
    if enemyAttack[0]:
        if playerEnemy.type == 2:
            F.drawBox(player1_Board)
            print('PC shot in [{X}][{Y}]'.format(X=enemyAttack[1],Y=enemyAttack[2]))
            print('PC hit one ship! :(')
        elif playerEnemy.type ==  1:
            print('{} hit one ship!'.format(playerEnemy.name.capitalize()))
        print(checkStatus(player1Ships,enemyAttack[1],enemyAttack[2]))
        game = player1.checkShips(player1Ships)
        if not game:
            F.clearConsole()
            F.drawBox(Enemy_AttackBoard)
            if playerEnemy.type == 2:
                print('OH NO, THE PC WON YOU :(')
            elif playerEnemy.type ==1:    
                print('{}, YOU ARE THE WINNER!! CONGRATULATIONS!!'.format(playerEnemy.name))
            print('---------------------------------------------------------------------------------------')
            winner = playerEnemy
            break
    else:
        if playerEnemy.type == 2:
            print('PC shot in [{X}][{Y}]'.format(X=enemyAttack[1],Y=enemyAttack[2]))
            F.drawBox(player1_Board)
        print('{} hit the water...'.format(playerEnemy.name.capitalize()))
    
    
    os.system("pause")
    F.clearConsole()
    print('---------------------------------------------------------------------------------------')
    print('PLAYER SHIPS')
    for playerShip in player1Ships:
        print('----*----')
        playerShip.printData()
    print('---------------------------------------------------------------------------------------')
    print('ENEMY SHIPS')
    for enemyShip in enemyShips:
        print('----*----')
        enemyShip.printData()
    os.system("pause")
    F.clearConsole()

print('--------------------------------------STATISTICS---------------------------------------')
player1.printStatistics()
print('---------------------------------------------------------------------------------------')
playerEnemy.printStatistics()

os.system("pause")
F.clearConsole()

print('DATA GAME\n----------------------------')
print('PLAYER 1')
F.drawBox(player1_Board)
player1.printData()
print('----------------------------')
print('PLAYER 2')
F.drawBox(Enemy_Board)
playerEnemy.printData()
os.system("pause")