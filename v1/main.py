from tkinter import *
import time

from v1.Board import Board
from v1.Cell import Cell

window = Tk()  # l'objet qui va permettre de définir l'ensemble des elements de la fenetre
width = 800
height = 609
canvas = Canvas(window, width=width, height=height,
                bg='white')  # on définie la zone de dessin
canvas.pack(side=TOP, padx=0, pady=0)

# Crée un tableau/board et l'actualisé
board = Board(width, height, 16, 16)  # OK
board.Init()
# board.Show()

dt = 0


def mainLoop():
    oldTimer = time.time()

    board.Update()
    board.Draw(canvas, width, height)

    window.after(1, mainLoop)
    dt = time.time() - oldTimer


board.Draw(canvas, width, height)
mainLoop()
window.mainloop()
