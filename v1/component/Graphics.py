class GraphicsSetting:
    
    Graphics = 0
    
    def __init__(self, screenWidth, screenHeight, cellsSize, canvas):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.cellSize = cellsSize
        self.canvas = canvas
        GraphicsSetting.Graphics = self
        
    @staticmethod
    def ConvertToGray(img):
        pixels = img.load()
        w = img.size[0]
        h = img.size[1]
        print(pixels[0,0][3])
        for x in range(0, w):
            for y in range(0, h):
                avg = int((pixels[x,y][0] + pixels[x,y][1] + pixels[x,y][2]) * 0.333333333)
                pixels[x, y] = (avg, avg, avg, 255)
        return img