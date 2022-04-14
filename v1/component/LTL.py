#Implémente a règle de larger than life, mais sans utiliser de poids.
from component.Cell import *
from component.Board import *

class LTL:

    @staticmethod
    def Init():
        pass
    
    @staticmethod
    def GetNextState(cell, sumNeighboor):
        match cell.state:
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

    @staticmethod
    def GetSumNeighbours(x, y, oldArr, board):
        sum = 0
        for i in range(-Cell.neighbourRadius, Cell.neighbourRadius + 1):
            for j in range(-Cell.neighbourRadius, Cell.neighbourRadius + 1):
                if j != 0 or i != 0:
                    xTmp, yTmp = board.ConvertCoordonate(x + i, y + j)
                    sum += oldArr[yTmp][xTmp].state
        return sum

    @staticmethod
    def Update(oldArr, board, dt):
        for x in range(0, board.height):
            for y in range(0, board.width):
                sum = LTL.GetSumNeighbours(x, y, oldArr,)
                board.cellsArr[x][y].state = LTL.GetNextState(board.cellsArr[x][y], sum)