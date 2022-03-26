import random
class player():
    name = ''
    points = 0
    floatingShips = 4
    sunkenShips = 0
    water = 0

    def __init__(self, playerName):
        self.name = playerName

    def attackShip(self, playerAttackBoard,enemyBoard,user):  
        if user == 1:
            print('Choose the coordinates of your attack')
            attackX = int(input('Coordinate X:'))
            attackY = int(input('Coordinate Y:'))
        elif user == 2:
            attackX = random.randint(1,8)
            attackY = random.randint(1,8)
        else:
            print('Error with User Type [A1]')   

        if enemyBoard[attackY-1][attackX-1] != ' ':
            enemyBoard[attackY-1][attackX-1] = '*'
            playerAttackBoard[attackY-1][attackX-1] = '*'
            return [True,attackX,attackY] #Check if the ship still has spaces without attack or if has been sunk
        else:
            enemyBoard[attackY-1][attackX-1] = 'o'
            playerAttackBoard[attackY-1][attackX-1] = 'o'
            return [False,attackX,attackY]

    def chooseSHipsPosition():
        pass