from enum import Enum
from tkinter import *
from component.Cell import *
from component.CustomRules1 import *
from component.LTL import *
from component.LTL2 import *
import random

class UpdateType(Enum):
    Custom1 = 0
    LTL = 1
    LTL2 = 2 #en incluant les poids
    
class Board:

    neighbourRadius = 0 # static attribute!
    maxNeighbours = 0 # static attribute!
    board = 0 # static attribute!

    def __init__(self, boardWidth, boardHeight, cellsWidth, cellsHeight, updateType):
        self.cellsArr = []
        self.width = boardWidth
        self.height = boardHeight
        self.cellsWidth = cellsWidth  # la largeur en pixel de la cellule
        self.cellsHeight = cellsHeight  # la hauteur en pixel de la cellule*
        self.updateType = updateType

    def Init(self):
        Board.maxNeighbours = ((3 + ((Board.neighbourRadius - 1) * 2))**2) - 1
        Board.board = self
        Cell.neighbourRadius = self.neighbourRadius
        random.seed()
        match self.updateType:
            case UpdateType.Custom1:
                CustomRules1.Init()
            case UpdateType.LTL:
                LTL.Init()
            case UpdateType.LTL2:
                LTL2.Init()

        self.cellsArr = []      
        # on parcour tout le tableau
        for x in range(0, self.height):
            self.cellsArr.append([])
            for y in range(0, self.width):
                # on init chaque cell avec un probabilité pAlive d'etre en vie
                randState = random.randint(0, Cell.NB_STATE - 1)
                self.cellsArr[x].append(Cell(randState))

    def CloneArrCells(self):
        clone = []
        # on parcour tout le tableau
        for x in range(0, self.height):
            clone.append([])
            for y in range(0, self.width):
                clone[x].append(self.cellsArr[x][y].Clone())
        return clone

    # Pour le debug on affiche le tablau dans la console
    def Show(self, arr):
        for x in range(0, self.height):
            line = "["
            for y in range(0, self.width):
                line += str(arr[x][y].state)
                if y < self.width - 1:
                    line += ","
            line += "]"
            print(line)
        print("")
        
    def ConvertCoordonate(self, x, y):
        if x < 0:
            x += self.width
        if x >= self.width:
            x -= self.width
        if y < 0:
            y += self.height
        if y >= self.height:
            y -= self.height
        return x, y

    def Update(self, dt):
        oldArr = self.CloneArrCells()
        match self.updateType:
            case UpdateType.Custom1:
                CustomRules1.Update(oldArr, self, dt)
            case UpdateType.LTL:
                LTL.Update(oldArr, self, dt)
            case UpdateType.LTL2:
                LTL2.Update(oldArr, self, dt)

    def Draw(self, graphics):
        graphics.canvas.delete(ALL)
        # on parcour tout le tableau
        for y in range(0, self.height):
            graphics.canvas.create_line(0, y * self.cellsHeight, graphics.screenWidth, y * self.cellsHeight)

        for x in range(0, self.width):
            graphics.canvas.create_line(x * self.cellsWidth, 0, x * self.cellsWidth, graphics.screenHeight)

        # pour les cellules
        for x in range(0, self.height):
            for y in range(0, self.width):
                color = self.cellsArr[x][y].GetColor()
                graphics.canvas.create_rectangle(y * self.cellsWidth, x * self.cellsHeight, y * self.cellsWidth + self.cellsWidth, x * self.cellsHeight + self.cellsHeight, fill=color)
