from cmu_graphics import rgb

class Wall:
    def __init__(self, x, y, width, height):   
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = rgb(120, 120, 120)

class VanishWall(Wall):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.timer = 100
        self.color = rgb(66, 66, 66)
        self.visible = True
        self.opacity = 100