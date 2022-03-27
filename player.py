import random
class player():
    name = ''
    shots = 0
    successfulShots = 0
    missedShots = 0
    floatingShips =[]
    sunkenShips =[]

    def __init__(self, playerName):
        self.name = playerName
    
    def printData(self):
        print('Data Player {}'.format(self.name))
        print('Shots: ',self.shots)
        print('Ships floating [{}]: '.format(len(self.floatingShips)),self.floatingShips)
        print('Ships sunken [{}]: '.format(len(self.sunkenShips)),self.sunkenShips)
    
    def printStatistics(self):
        if len(self.floatingShips) == 0:
            print(self.name,' is the LOSER!')
        else:
            print(self.name,' is the WINNER!')
        #print('With {sF} ships floating and {sS} sunken ships'.format(sF=len(self.floatingShips),sS=len(self.sunkenShips)))
        print('TOTAL SHOTS: ',self.shots)
        print(' -Successful Shots: ',self.successfulShots)
        print(' -Missed Shots: ',self.missedShots)
    
    def setUpShips(self, *ships):
        shipsList = []
        for ship in ships:
            shipsList.append(ship)
        self.floatingShips = shipsList.copy()

    def attackShip(self, playerAttackBoard,enemyBoard,user):  
        validCoors = False
        while not validCoors:
            if user == 1:
                print('Choose the coordinates of your attack')
                attackX = int(input('Coordinate X:'))
                attackY = int(input('Coordinate Y:'))               
            elif user == 2:
                attackX = random.randint(1,8)
                attackY = random.randint(1,8)
            else:
                print('Error with User Type [A1]') 
            
            if enemyBoard[attackY-1][attackX-1] != 'o' and enemyBoard[attackY-1][attackX-1] != '*':
                validCoors = True
            else:
                print('You chose that space before, choose another one different')  
        self.shots += 1
        
        if enemyBoard[attackY-1][attackX-1] != ' ':
            enemyBoard[attackY-1][attackX-1] = '*'
            playerAttackBoard[attackY-1][attackX-1] = '*'
            self.successfulShots += 1
            return [True,attackX,attackY] #Return True because there was an impact
            #Check if the ship still has spaces without attack or if has been sunk
        else:
            enemyBoard[attackY-1][attackX-1] = 'o'
            playerAttackBoard[attackY-1][attackX-1] = 'o'
            self.missedShots += 1
            return [False,attackX,attackY] #Return False because there was no an impact or impact in the water

    def checkShips(self, shipList):
        for ship in shipList:
            if ship.sunk and (ship in self.floatingShips)  :
                self.floatingShips.remove(ship)
                self.sunkenShips.append(ship)                
        if len(self.sunkenShips) == 4:
            return False #Game Over
        elif len(self.floatingShips) > 0:
            return True