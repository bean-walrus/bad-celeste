class Level:
    def __init__(self, resetX, resetY):
        self.walls = []
        self.deaths = []
        self.springs = []
        self.recharges = []
        self.signs = []
        self.clears = []
        self.resetX = resetX
        self.resetY = resetY