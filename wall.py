class Wall:
    def __init__(self, vanish, x, y, width, height):
        self.vanish = vanish
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = 'darkGray'
        self.visible = True