class Recharge:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sideLength = (self.width // 2) * (2 ** 0.5)
        self.color = 'lime'
        self.visible = True
        self.timer = 100