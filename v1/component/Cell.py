class Cell:
    
    def __init__(self, isAlive):
        self.isAlive = isAlive#On crée un attribut isAlive pour toute les instance de la classe Cell
        
    def Clone(self):
        return Cell(self.isAlive)
        
    def GetNextState(self, nbNeighboor):
        if self.isAlive:
            return nbNeighboor > 6 and nbNeighboor < 13
        else:
            return nbNeighboor == 6 or nbNeighboor == 8 or nbNeighboor == 12
        
        if self.isAlive:
            return nbNeighboor == 2 or nbNeighboor == 3
        else:
            return nbNeighboor == 3
        