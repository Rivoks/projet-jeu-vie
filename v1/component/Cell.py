class Cell:
    
    NB_STATE = 0 # static attribute!
    colors = []

    @staticmethod
    def SetColors():
        Cell.colors.append('black')#0 <=> black
        Cell.colors.append('white')#1 <=> white

    def __init__(self, state):
        self.state = state #on étend les états d'un cellule a plus que 2
        
    def Clone(self):
        return Cell(self.state)

    def GetColor(self):
        return Cell.colors[self.state]

    #return a number between 0 and Cell.NB_STATE - 1
    #neighboors is a list which contain te number of cells which have the state 0 to NB_STATE - 1
    def GetNextState(self, neighboors):

        """
        #custom rules 1
        if self.state == 1:
            if neighboors[1] > 6 and neighboors[1] < 13:
                return 1
            else:
                return 0
        else:
            if neighboors[1] == 6 or neighboors[1] == 8 or neighboors[1] == 12:
                return 1
            else:
                return 0
        """
        #rules for the traditionnal game of life
        if self.state == 1:
            if neighboors[1] == 2 or neighboors[1] == 3:
                return 1
            else:
                return 0
        else:
            if neighboors[1] == 3:
                return 1
            else:
                return 0
        