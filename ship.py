class ship():
    length  = 0
    origin = [0,0]
    end = [0,0] 
    orientation = ''
    body = []
    sunk = False

    def __init__(self, length, origin, end, orientation):
        self.length = length
        self.origin = origin
        self.end = end
        self.orientation = orientation
        cooBody = []
        if self.orientation == 'V':
            itV = 1 if self.origin[1]<self.end[1] else -1
            for i in range(self.origin[1],self.end[1]+(itV),itV):
                cooBody.append([self.origin[0],i])
        elif self.orientation == 'H':
            itH = 1 if self.origin[0]<self.end[0] else -1
            for i in range(self.origin[0],self.end[0]+(itH),itH):
                cooBody.append([i,self.origin[1]])
        self.body = cooBody.copy()

    def printData(self):
        print('Ship Lenght: ',self.length)
        print('Ship Body: ',self.body)
        print('Ship Orientation: ',self.orientation)
        if not self.sunk:
            print('The ship is still floating')
        else:
            print('The is sunk')

def checkStatus(shipList,coorX,coorY):
        for ship in shipList:
            if [coorX,coorY] in ship.body:
                ship.body[ship.body.index([coorX,coorY])] = '*'              
                cont = 0
                for space in ship.body:  
                    if space == '*':
                        cont += 1
                if cont == ship.length:
                    ship.sunk = True
                    return 'The ship with length {} has been sunk'.format(ship.length)
                else:
                    return 'The ship still has spaces to attack'
        print('Check Status done')