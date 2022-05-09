#Implémente a règle de Conway (de base) du jeu de la vie.
from operator import ne
from component.Board import *
from component.Cell import *

class ConwayRule:

    @staticmethod
    def Init():
        Cell.NB_STATE = 2
        Cell.neighbourRadius = 1#le rayon du voisinage

    @staticmethod
    def GetNextState(cell, neighboors):
        if cell.state == 0:#morte
            if neighboors == 3:
                return 1
            else:
                return 0
        else:#vivante
            if neighboors == 2 or neighboors == 3 :
                return 1
            else:
                return 0

    @staticmethod
    def GetNeighbours(x, y, oldArr, board):
        neighboors = 0
        xTmp, yTmp = 0, 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if j != 0 or i != 0:
                    #On converti les coordonée car on est dans un monde torique.
                    xTmp, yTmp = board.ConvertCoordonate(x + i, y + j)
                    neighboors += oldArr[yTmp][xTmp].state
        return neighboors

    @staticmethod
    def Update(oldArr, board, dt):
        for x in range(0, board.height):
            for y in range(0, board.width):
                #On compte le nombre de voisines vivantes
                neighboors = ConwayRule.GetNeighbours(x, y, oldArr, board)
                #On actualise sont état.
                board.cellsArr[x][y].state = ConwayRule.GetNextState(board.cellsArr[x][y], neighboors)