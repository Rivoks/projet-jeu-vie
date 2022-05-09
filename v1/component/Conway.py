#Implémente a règle de Conway (de base) du jeu de la vie.
from operator import ne
from component.Board import *
from component.Cell import *

class ConwayRule:

    @staticmethod
    def Init():
        pass

    @staticmethod
    def GetNextState(cell, neighboors):
        #pattern
        if cell.state == 0:
            if neighboors == 3:
                return 1
            else:
                return 0
        else:
            if neighboors == 2 or neighboors == 3 :
                return 1
            else:
                return 0

        if cell.state == 0:
            return 1 if neighboors == 3 else 0
        else:
            return 1 if neighboors == 2 or neighboors == 3 else 0

    @staticmethod
    def GetNeighbours(x, y, oldArr, board):
        neighboors = 0
        xTmp, yTmp = 0, 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if j != 0 or i != 0:
                    xTmp, yTmp = board.ConvertCoordonate(x + i, y + j)
                    neighboors += oldArr[yTmp][xTmp].state
        return neighboors

    @staticmethod
    def Update(oldArr, board, dt):
        for x in range(0, board.height):
            for y in range(0, board.width):
                neighboors = ConwayRule.GetNeighbours(x, y, oldArr, board)
                board.cellsArr[x][y].state = ConwayRule.GetNextState(board.cellsArr[x][y], neighboors)