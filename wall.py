from cmu_graphics import rgb

class Wall:
    def __init__(self, vanish, x, y, width, height):
        self.vanish = vanish
        if self.vanish:
            self.timer = 100
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        if self.vanish:
            self.color = 'navy'
        else:
            self.color = rgb(80, 80, 80)
        self.visible = True
        self.opacity = 100