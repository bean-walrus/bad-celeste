class Player:
    def __init__(self):
        self.x = 31
        self.y = 400
        self.size = 20
        self.veloY = 0
        self.veloX = 0
        self.tv = 20
        self.gravity = 1.8
        self.fill = 'black'

        self.holdingWall = False

    def getBottom(self):
        return self.y + self.size
    
    def setHoldingWall(self, dict, walls):
        for wall in walls:
            self.x += 1
            if self.touchingWall(wall):
                for key in dict:
                    if dict[key] == True:
                        self.holdingWall = True
                        self.x -= 1
                        return
            self.x -= 2
            if self.touchingWall(wall):
                for key in dict:
                    if dict[key] == True:
                        self.holdingWall = True
                        self.x += 1
                        return
            self.x += 1
        self.holdingWall = False

    
    def checkInWall(self, walls):
        futureBottom = self.getBottom() + self.veloY
        futureTop = self.y + self.veloY
        futureRight = self.x + self.size + self.veloX
        futureLeft = self.x + self.veloX
        collided = False
        for wall in walls:
            if (futureRight > wall.x and futureLeft < wall.x + wall.width):
                if (wall.y <= futureBottom <= wall.y + wall.height):
                    self.y = wall.y - self.size
                    self.veloY = 0
                    collided = True
                    break
                if (wall.y <= futureTop <= wall.y + wall.height):
                    self.y = wall.y + wall.height + 1
                    self.veloY = 0
                    collided = True
                    break
        if not collided and self.veloY + self.gravity < self.tv:
            self.veloY += self.gravity

    def jump(self, walls, jumpHeight):
        self.y += 1
        for wall in walls:
            if self.touchingWall(wall):
                self.y -= 1
                self.veloY = jumpHeight
                return
        self.y -= 1

    def dash(self, direction):
        self.veloX = direction['horizontal']
        self.veloY = direction['vertical']


    def touchingWall(self, wall):
        return (
            self.x + self.size > wall.x and  # right edge of player past left edge of wall
            self.x < wall.x + wall.width and  # left edge of player before right edge of wall
            self.y + self.size > wall.y and  # bottom edge of player past top edge of wall
            self.y < wall.y + wall.height  # top edge of player before bottom edge of wall
        )

