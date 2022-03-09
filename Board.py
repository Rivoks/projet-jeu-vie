from Cell import Cell
import random
from tkinter import *

class Board:
    def __init__(self, canvasWidth, canvasHeight, cellsWidth, cellsHeight):
        self.cellsArr = []
        self.width = canvasWidth // cellsWidth
        self.height = canvasHeight // cellsHeight
        self.cellsWidth = cellsWidth#la largeur en pixel de la cellule
        self.cellsHeight = cellsHeight#la hauteur en pixel de la cellule
        
    def Init(self):
        random.seed(84569)
        self.cellsArr = []
        pAlive = 60
        #on parcour tout le tableau
        for x in range(0, self.height):
            self.cellsArr.append([])
            for y in range(0, self.width):
                #on init chaque cell avec un probabilité pAlive d'etre en vie
                alive = (random.randint(1, 100) <= pAlive)
                self.cellsArr[x].append(Cell(alive))
                
    def CloneArrCells(self):
        clone = []
        #on parcour tout le tableau
        for x in range(0, self.height):
            clone.append([])
            for y in range(0, self.width):
                clone[x].append(self.cellsArr[x][y].Clone())
        return clone
       
    #Pour le debug on affiche le tablau dans la console      
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
            
    def Update(self):
        oldArr = self.CloneArrCells()
        for x in range(0, self.height):
            for y in range(0, self.width):
                nbNeighboor = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if j != 0 or i != 0:
                            if x + i >= 0 and x + i < self.height and y + j >= 0 and y + j < self.width:
                                if oldArr[x + i][y + j].isAlive:
                                    nbNeighboor += 1
                                #nbNeighboor = nbNeighboor + 1 if oldArr[x + i][y + j].isAlive else nbNeighboor
                self.cellsArr[x][y].isAlive = self.cellsArr[x][y].GetNextState(nbNeighboor)
        
        
    def Draw(self, canvas, canvasW, canvasH):
        canvas.delete(ALL)
        #on parcour tout le tableau
        for y in range(0, self.height):
            canvas.create_line(0, y * self.cellsHeight, canvasW, y * self.cellsHeight)
        
        for x in range(0, self.width):
            canvas.create_line(x * self.cellsWidth, 0, x * self.cellsWidth, canvasH)
            #can1.create_rectangle(x, y, x+c, y+c, fill='black')
        
        #pour les cellules
        for x in range(0, self.height):
            for y in range(0, self.width):
                color = 'black' if self.cellsArr[x][y].isAlive else 'white'
                canvas.create_rectangle(y * self.cellsWidth, x * self.cellsHeight, y * self.cellsWidth + self.cellsWidth, x * self.cellsHeight + self.cellsHeight, fill=color)
    