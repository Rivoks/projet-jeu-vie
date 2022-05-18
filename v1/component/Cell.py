from component.Colors import linear_gradient
# https://bsouthga.dev/posts/color-gradients-with-python


class Cell:

    NB_STATE = 0  # static attribute!
    neighbourRadius = 0
    colors = []

    @staticmethod
    def SetColors():
        Cell.colors = linear_gradient("#FFFFFF", "#000000", Cell.NB_STATE)
        print(Cell.colors)
        # Cell.colors = ['#ffffff', '#bfbfbf', '#7f7f7f', '#3f3f3f', '#000000']
        # Cell.colors.append('#000000')
        # Cell.colors.append('#323232')
        # Cell.colors.append('#7d7d7d')
        # Cell.colors.append('#c8c8c8')
        # Cell.colors.append('#ffffff')

    def __init__(self, state):
        self.state = state  # on étend les états d'un cellule a plus que 2

    def Clone(self):
        return Cell(self.state)

    def GetColor(self):
        return Cell.colors[self.state]
