from component.Cell import *
import random
from tkinter import *

class Board:
    def __init__(self, boardWidth, boardHeight, cellsWidth, cellsHeight, neighbourRadius):
        self.cellsArr = []
        self.width = boardWidth
        self.height = boardHeight
        self.cellsWidth = cellsWidth  # la largeur en pixel de la cellule
        self.cellsHeight = cellsHeight  # la hauteur en pixel de la cellule*
        self.neighbourRadius = neighbourRadius

    def Init(self):
        random.seed()
        self.cellsArr = []
        pAlive = 60
        # on parcour tout le tableau
        for x in range(0, self.height):
            self.cellsArr.append([])
            for y in range(0, self.width):
                # on init chaque cell avec un probabilité pAlive d'etre en vie
                alive = (random.randint(1, 100) <= pAlive)
                self.cellsArr[x].append(Cell(alive))

    def CloneArrCells(self):
        clone = []
        # on parcour tout le tableau
        for x in range(0, self.height):
            clone.append([])
            for y in range(0, self.width):
                clone[x].append(self.cellsArr[x][y].Clone())
        return clone

    # Pour le debug on affiche le tablau dans la console
    def Show(self):
        for x in range(0, self.height):
            line = "["
            for y in range(0, self.width):
                currentCell = self.cellsArr[x][y]
                if currentCell.isAlive:
                    line += "1"
                else:
                    line += "0"
                if y < self.width - 1:
                    line += ","
            line += "]"
            print(line)
        
    def CellCoordonateExist(self, x, y):
        return x >= 0 and x < self.height and y >= 0 and y < self.width
            
    def GetNbNeighbour(self, x, y, oldArr):
        nbNeighboor = 0
        for i in range(-self.neighbourRadius, self.neighbourRadius + 1):
            for j in range(-self.neighbourRadius, self.neighbourRadius + 1):
                if ((j != 0 or i != 0) and self.CellCoordonateExist(x + i, y + j)):
                    if oldArr[x + i][y + j].isAlive:
                        nbNeighboor += 1
        return nbNeighboor

    def Update(self, dt):
        oldArr = self.CloneArrCells()
        for x in range(0, self.height):
            for y in range(0, self.width):
                nbNeighboor = self.GetNbNeighbour(x, y, oldArr)
                self.cellsArr[x][y].isAlive = self.cellsArr[x][y].GetNextState(nbNeighboor)

    def Draw(self, graphics):
        graphics.canvas.delete(ALL)
        # on parcour tout le tableau
        for y in range(0, self.height):
            graphics.canvas.create_line(0, y * self.cellsHeight,
                               graphics.screenWidth, y * self.cellsHeight)

        for x in range(0, self.width):
            graphics.canvas.create_line(x * self.cellsWidth, 0, x *
                               self.cellsWidth, graphics.screenHeight)

        # pour les cellules
        for x in range(0, self.height):
            for y in range(0, self.width):
                color = 'white' if self.cellsArr[x][y].isAlive else 'black'
                graphics.canvas.create_rectangle(y * self.cellsWidth, x * self.cellsHeight, y * self.cellsWidth +
                                        self.cellsWidth, x * self.cellsHeight + self.cellsHeight, fill=color)
