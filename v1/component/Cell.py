import random
from component.Board import *

class Cell:
    
    NB_STATE = 0 # static attribute!
    neighbourRadius = 0
    colors = []

    @staticmethod
    def SetColors():
        Cell.colors = []
        Cell.colors.append('#000000')
        Cell.colors.append('#323232')
        Cell.colors.append('#7d7d7d')
        Cell.colors.append('#c8c8c8')
        Cell.colors.append('#ffffff')

    def __init__(self, state):
        self.state = state #on étend les états d'un cellule a plus que 2
        
    def Clone(self):
        return Cell(self.state)

    def GetColor(self):
        return Cell.colors[self.state]