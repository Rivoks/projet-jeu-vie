import random
from component.Board import *

class Cell:
    
    NB_STATE = 0 # static attribute!
    neighbourRadius = 0
    colors = []

    @staticmethod
    def SetColors():
        Cell.colors.append('#000000')
        Cell.colors.append('#323232')
        Cell.colors.append('#7d7d7d')
        Cell.colors.append('#c8c8c8')
        Cell.colors.append('#ffffff')

    def __init__(self, state):
        self.state = state #on étend les états d'un cellule a plus que 2
        
    def Clone(self):
        return Cell(self.state)

    def GetColor(self):
        return Cell.colors[self.state]

    def GetStateLargerThanLife(self, sumNeighboor):
         match self.state:
            case 0 :
                if sumNeighboor > 10 and sumNeighboor < 20 :
                    return 1
                else:
                    return 2
            case 1 :
                if sumNeighboor < 4 or sumNeighboor > 30 :
                    return 2
                else:
                    return 4
            case 2 :
                if random.random() > 0.5:
                    return 3
                else:
                    return 2
            case 3 :
                if  4 + (sumNeighboor % Cell.neighbourRadius) > 7:
                    return 2
                else:
                    return random.randint(0, 4)
            case 4 :
                if sumNeighboor > 15 - Cell.neighbourRadius:
                    return random.randint(0, 3)
                else:
                    return 4
            case _ :
                return 4
    
    #return a number between 0 and Cell.NB_STATE - 1
    #neighboors is a list which contain te number of cells which have the state 0 to NB_STATE - 1
    def GetNextState(self, neighboors):

        #pattern
        match self.state:
            case 0 :
                if neighboors[0] % Cell.neighbourRadius > 3 or (neighboors[2] % Cell.neighbourRadius> 4 and neighboors[3] % Cell.neighbourRadius > 4):
                    return 1
                elif neighboors[4] % Cell.neighbourRadius > 7:
                    return 3
                else:
                    return 2
            case 1 :
                if  neighboors[2] % Cell.neighbourRadius > 2 and neighboors[3] % Cell.neighbourRadius > 2 and neighboors[4] % Cell.neighbourRadius > 2:
                    return 2
                else:
                    return 4
            case 2 :
                if random.random() > 0.5:
                    return 3
                else:
                    return 2
            case 3 :
                if  neighboors[3] > 7 % Cell.neighbourRadius:
                    return 2
                else:
                    return random.randint(0, 4)
            case 4 :
                if neighboors[0] > 5 % Cell.neighbourRadius or (neighboors[2] % Cell.neighbourRadius > 4  and neighboors[3] > 4 and neighboors[4] > 5):
                    return 1
                elif neighboors[4] % Cell.neighbourRadius > 5:
                    return random.randint(0, 3)
                else:
                    return 4
            case _ :
                return 4
        #custom rules 1
        if self.state == 1:
            if neighboors[1] > 6 and neighboors[1] < 13:
                return 1
            else:
                return 0
        else:
            if neighboors[1] == 6 or neighboors[1] == 8 or neighboors[1] == 12:
                return 1
            else:
                return 0
        #rules for the traditionnal game of life
        if self.state == 1:
            if neighboors[1] == 2 or neighboors[1] == 3:
                return 1
            else:
                return 0
        else:
            if neighboors[1] == 3:
                return 1
            else:
                return 0
        