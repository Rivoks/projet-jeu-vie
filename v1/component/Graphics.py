class GraphicsSetting:
    
    Graphics = 0
    
    def __init__(self, screenWidth, screenHeight, cellsSize, canvas):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.cellSize = cellsSize
        self.canvas = canvas
        GraphicsSetting.Graphics = self
        