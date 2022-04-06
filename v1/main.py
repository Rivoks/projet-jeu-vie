from tkinter import *
import time
from component.Board import *
from component.Cell import *
from component.Graphics import *

TARGETEDDELTATIME = 1
window = Tk()  # l'objet qui va permettre de définir l'ensemble des elements de la fenetre
width = 900
height = 500
canvas = Canvas(window, width=width, height=height, bg = 'white')  # on définie la zone de dessin
graphicSetting = GraphicsSetting(width, height, 8, canvas)
# Crée un tableau/board et l'actualisé
board = Board(width // 16, height // 16, 16, 16)
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

def mainLoop():
    global newClock, oldClock
    newClock = time.time()
    dt = (newClock - oldClock) * 1000

    board.Update(dt)
    board.Draw(graphicSetting)
    
    oldClock = newClock
    window.after(TARGETEDDELTATIME, mainLoop)


if __name__ == '__main__':
    Setup()
    #Launch the game
    board.Draw(graphicSetting)
    mainLoop()
    window.mainloop()
