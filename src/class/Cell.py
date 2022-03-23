class Cell:

    def __init__(self, isAlive):
        # On crée un attribut isAlive pour toute les instance de la classe Cell
        self.isAlive = isAlive

    def Clone(self):
        return Cell(self.isAlive)

    def GetNextState(self, nbNeighboor):
        if self.isAlive:
            return nbNeighboor == 2 or nbNeighboor == 3
        else:
            return nbNeighboor == 3
