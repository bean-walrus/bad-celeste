class Spring:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = 'magenta'

class VanishSpring(Spring):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.timer = 100
        self.visible = True
        self.opacity = 100