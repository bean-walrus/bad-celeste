from cmu_graphics import rgb
class Sign:
    def __init__(self, message, x, y):
        self.message = message
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.counter = 0
        self.color = rgb(135, 85, 43)
        self.display = False