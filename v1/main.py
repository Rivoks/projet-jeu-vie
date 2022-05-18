from tkinter import *
import time
from component.Board import *
from component.Cell import *
from component.Graphics import *
from component.ButtonsManager import *
from PIL import Image


class MainGame:

    mainGame = 0  # ref au mainGame du jeu

    def __init__(self):
        self.TARGETEDDELTATIME = 1
        self.flag = 0
        # l'objet qui va permettre de définir l'ensemble des elements de la fenetre
        self.window = Tk()
        self.dt, self.oldClock, self.newClock = 0, 0, 0
        self.window.title(string = "Game Of Life")
        self.oldClock = time.time()
        self.newClock = self.oldClock

    def CreateCanvasBoardAndButtons(self):
        # on définie la zone de dessin
        self.canvas = Canvas(self.window, width = self.width, height = self.height, bg = 'white')
        self.canvas.pack(side = TOP, padx = 0, pady = 0)
        self.graphicSetting = GraphicsSetting(
            self.width, self.height, 8, self.canvas)
        self.board = Board(self.width // self.cellSize, self.height //
                           self.cellSize, self.cellSize, self.cellSize, UpdateType.LTL2)
        self.buttonsManager = ButtonsManager(self)
        self.buttonsManager.CreateButtons(self.window)

    def Setup(self):
        self.width = 900
        self.height = 700
        self.cellSize = 8
        self.CreateCanvasBoardAndButtons()
        Cell.NB_STATE = 5
        Cell.SetColors()
        Board.neighbourRadius = 1
        self.board.initTexture = Image.open('./v1/leopaul.png').resize((self.board.width, self.board.height), Image.ANTIALIAS)
        
        
        self.board.Init()
        MainGame.mainGame = self


    def mainLoop(self):
        self.newClock = time.time()
        self.dt = (self.newClock - self.oldClock) * 1000

        print("Temps réel: %.2f ms" % self.dt)

        self.board.Update(self.dt)
        self.board.Draw(self.graphicSetting)
        if self.flag > 0:
            self.oldClock = self.newClock
            self.window.after(self.TARGETEDDELTATIME, self.mainLoop)


if __name__ == '__main__':
    mainGame = MainGame()
    mainGame.Setup()
    # Launch the game
    mainGame.board.Draw(mainGame.graphicSetting)
    mainGame.mainLoop()
    mainGame.window.mainloop()
