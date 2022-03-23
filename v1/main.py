from tkinter import *
import time
from component.Board import *
from component.Cell import *
from component.Graphics import *

TIME = 100

window = Tk()  # l'objet qui va permettre de définir l'ensemble des elements de la fenetre
width = 800
height = 610
canvas = Canvas(window, width=width, height=height,
                bg='white')  # on définie la zone de dessin
canvas.pack(side=TOP, padx=0, pady=0)
graphicSetting = GraphicsSetting(width, height, 16, canvas)

# Crée un tableau/board et l'actualisé
board = Board(width // 16, height // 16, 16, 16, 2)
board.Init()
#board.Show()

dt = 0
def mainLoop():
    oldTimer = time.time()

    board.Update()
    board.Draw(graphicSetting)

    window.after(TIME, mainLoop)
    dt = time.time() - oldTimer


board.Draw(graphicSetting)
mainLoop()
window.mainloop()
