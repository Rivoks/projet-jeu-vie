#Implémente a règle de Léonard, càd compte de nombre de cellules dans chaque états.
from component.Board import *
from component.Cell import *
import random

class CustomRules1:

    @staticmethod
    def Init():
        pass

    #return a number between 0 and Cell.NB_STATE - 1
    #neighboors is a list which contain te number of cells which have the state 0 to NB_STATE - 1
    @staticmethod
    def GetNextState(cell, neighboors):
        #pattern
        match cell.state:
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
        if cell.state == 1:
            if neighboors[1] > 6 and neighboors[1] < 13:
                return 1
            else:
                return 0
        else:
            if neighboors[1] == 6 or neighboors[1] == 8 or neighboors[1] == 12:
                return 1
            else:
                return 0

    @staticmethod
    def GetNeighbours(x, y, oldArr, board):
        neighboors = [0] * Cell.NB_STATE # init to a list of 0
        for i in range(-Cell.neighbourRadius, Cell.neighbourRadius + 1):
            for j in range(-Cell.neighbourRadius, Cell.neighbourRadius + 1):
                if j != 0 or i != 0:
                    xTmp, yTmp = board.ConvertCoordonate(x + i, y + j)
                    neighboors[oldArr[yTmp][xTmp].state] += 1
        return neighboors

    @staticmethod
    def Update(oldArr, board, dt):
        for x in range(0, board.height):
            for y in range(0, board.width):
                neighboors = CustomRules1.GetNeighbours(x, y, oldArr, board)
                board.cellsArr[x][y].state = CustomRules1.GetNextState(board.cellsArr[x][y], neighboors)