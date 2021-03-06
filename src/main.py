from tkinter import *
import time

from components.Board import Board
from components.Cell import Cell

TIME = 100

window = Tk()  # l'objet qui va permettre de définir l'ensemble des elements de la fenetre
width = 800
height = 610
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

    window.after(TIME, mainLoop)
    dt = time.time() - oldTimer


board.Draw(canvas, width, height)


if __name__ == "__main__":
    mainLoop()
    window.mainloop()
