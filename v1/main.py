from tkinter import *
import time
from component.Board import *
from component.Cell import *
from component.Graphics import *
from component.ButtonsManager import *

class MainGame:

    mainGame = 0#ref au mainGame du jeu

    def __init__(self):
        self.TARGETEDDELTATIME = 1
        self.flag = 0
        self.window = Tk()  # l'objet qui va permettre de définir l'ensemble des elements de la fenetre
        self.dt, self.oldClock, self.newClock = 0, 0, 0
        self.window.title(string = "Game Of Life")
        self.oldClock = time.time()
        self.newClock = self.oldClock
        
    def CreateCanvasBoardAndButtons(self):
        self.canvas = Canvas(self.window, width = self.width, height = self.height, bg = 'white')  # on définie la zone de dessin
        self.canvas.pack(side = TOP, padx = 0, pady = 0)
        self.graphicSetting = GraphicsSetting(self.width, self.height, 8, self.canvas)
        self.board = Board(self.width // self.cellSize, self.height // self.cellSize, self.cellSize, self.cellSize, UpdateType.LTL2)
        self.buttonsManager = ButtonsManager(self)
        self.buttonsManager.CreateButtons(self.window)

    def Setup(self):
        self.width = 900
        self.height = 500
        self.cellSize = 16
        self.CreateCanvasBoardAndButtons()
        Cell.NB_STATE = 5
        Cell.SetColors()
        Board.neighbourRadius = 3
        self.board.Init()
        MainGame.mainGame = self

    def mainLoop(self):
        self.newClock = time.time()
        self.dt = (self.newClock - self.oldClock) * 1000

        self.board.Update(self.dt)
        self.board.Draw(self.graphicSetting)
        if self.flag > 0:
            self.oldClock = self.newClock
            self.window.after(self.TARGETEDDELTATIME, self.mainLoop)






"""
#to remove
TARGETEDDELTATIME = 1
window = Tk()  # l'objet qui va permettre de définir l'ensemble des elements de la fenetre
width = 900
height = 500
cellSize = 16
canvas = Canvas(window, width = width, height = height, bg = 'white')  # on définie la zone de dessin
graphicSetting = GraphicsSetting(width, height, 8, canvas)
# Crée un tableau/board et l'actualisé
board = Board(width // cellSize, height // cellSize, cellSize, cellSize, UpdateType.LTL2)
dt, oldClock, newClock = 0, 0, 0

def Setup():
    global newClock, oldClock, window
    window.title(string = "Game Of Life")
    oldClock = time.time()
    newClock = oldClock
    canvas.pack(side = TOP, padx = 0, pady = 0)
    Cell.NB_STATE = 5
    Cell.SetColors()
    Board.neighbourRadius = 3
    board.Init()
    ButtonsManager.CreateButtons(window)

def mainLoop():
    global newClock, oldClock
    newClock = time.time()
    dt = (newClock - oldClock) * 1000

    board.Update(dt)
    board.Draw(graphicSetting)
    
    oldClock = newClock
    window.after(TARGETEDDELTATIME, mainLoop)
"""

if __name__ == '__main__':
    mainGame = MainGame()
    mainGame.Setup()
    #Launch the game
    mainGame.board.Draw(mainGame.graphicSetting)
    mainGame.mainLoop()
    mainGame.window.mainloop()
