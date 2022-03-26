import functions as F
from ship import *
F.clearConsole()
mainBoard = F.createBoard(8,8)
F.drawBox(mainBoard)
if F.mainMenu():
    F.clearConsole()
    F.drawBox(mainBoard)
    valid_sL3 = False
    while not valid_sL3:
        print('\nChoose the coordinates of your firts ship (Length 3)')
        coo_sL3 = F.requestShipData(3)
        sL3 = ship(3,coo_sL3['Origin'],coo_sL3['End'],coo_sL3['Orientation'])
        if F.validSpace(mainBoard,sL3):
            F.putShipOnBoard(mainBoard,sL3)
            F.drawBox(mainBoard)           
            valid_sL3 = True
        else:
            print('\nYOU WON\'T BE ABLE TO PUT YOUR SHIP THERE, BECAUSE ALREADY THERE IS ANOTHER ONE THERE.\nTRY ANOTHER COORDINATE') 
    
          
    valid_sL4 = False
    while not valid_sL4:       
        print('\nChoose the coordinates of your firts ship (Length 4)')
        coo_sL4 = F.requestShipData(4)
        sL4 = ship(4,coo_sL4['Origin'],coo_sL4['End'],coo_sL4['Orientation'])
        if F.validSpace(mainBoard,sL4):
            F.putShipOnBoard(mainBoard,sL4)
            F.drawBox(mainBoard)
            valid_sL4 = True
        else:
            print('\nYOU WON\'T BE ABLE TO PUT YOUR SHIP THERE, BECAUSE ALREADY THERE IS ANOTHER ONE THERE.\nTRY ANOTHER COORDINATE')

    """
    print('\nChoose the coordinates of your firts ship (Length 5)')   
    coo_sL5 = F.requestShipData(5)
    sL5 = Ship(5,coo_sL5['Origin'],coo_sL5['End'],coo_sL5['Orientation'])
    F.putShipOnBoard(mainBoard,sL5)
    """

else:
    print('The first player choose the positions')