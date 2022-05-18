# Implémente a règle de larger than life en utilisant des poids.
from component.Board import *
from component.Cell import *
from component.Useful import *
from component.ButtonsManager import *
from main import *
import random

class LTL2:

    weigth = []
    stateRange = []  # les intervalles de naissance/survie pour tout les états

    @staticmethod
    def Init():
        LTL2.ChangeWeight(Cell.neighbourRadius)
        # [a, b, c, d] si une cellule est à l'état 0, elle passe a l'état c si elle a entre a et b voisines,
        # sinon elle va à l'état d 
        LTL2.stateRange = [ #super clignotant
            [15, 50, 1, 2],
            [15, 50, 2, 3],
            [15, 50, 3, 4],
            [15, 50, 4, 0],
            [15, 50, 1, 2],
        ]
        # LTL2.stateRange = [
        #     [1, 12, 1, 2],
        #     [1, 12, 2, 3],
        #     [1, 12, 3, 4],
        #     [1, 12, 4, 0],
        #     [1, 12, 1, 2],
        # ]

    @staticmethod
    def ChangeWeight(newRadius):
        print("newRadius", newRadius)
        LTL2.weigth = []
        for i in range(0, 2 * newRadius + 1):
            LTL2.weigth.append(Useful.Lerp(0, 1, i / (2.0 * newRadius)))

    @staticmethod
    def GetNextState(cell, sumNeighboor):
        if LTL2.stateRange[cell.state][0] >= sumNeighboor and sumNeighboor <= LTL2.stateRange[cell.state][1]:
            return LTL2.stateRange[cell.state][2]
        else:
            return LTL2.stateRange[cell.state][3]

    @staticmethod
    def GetSumNeighbours(x, y, oldArr, board):
        sum = 0.0
        for i in range(-Cell.neighbourRadius, Cell.neighbourRadius + 1):
            for j in range(-Cell.neighbourRadius, Cell.neighbourRadius + 1):
                if j != 0 or i != 0:
                    xTmp, yTmp = board.ConvertCoordonate(x + i, y + j)
                    sum += oldArr[yTmp][xTmp].state * \
                        LTL2.weigth[abs(i) + abs(j)]
        return sum

    @staticmethod
    def Update(oldArr, board, dt):
        for x in range(0, board.height):
            for y in range(0, board.width):
                sum = LTL2.GetSumNeighbours(x, y, oldArr, board)
                board.cellsArr[x][y].state = LTL2.GetNextState(board.cellsArr[x][y], sum)
