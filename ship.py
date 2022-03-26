class ship():
    length  = 0
    origin = [0,0]
    end = [0,0] 
    orientation = ''
    sunk = False

    def __init__(self, length, origin, end, orientation):
        self.length = length
        self.origin = origin
        self.end = end
        self.orientation = orientation

    def attacked(self):
        print('The ships has been attacked')