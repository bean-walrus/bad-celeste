from cmu_graphics import *
from player import Player
from wall import *
from death import Death
from spring import *
from recharge import Recharge
from sign import Sign
from clear import Clear
from level import Level
import time

def onAppStart(app):
    app.player = Player()
    app.width = 600
    app.height = 600
    app.speed = 10
    app.stepsPerSecond = 45

    app.inTitle = True #Change later
    app.coverOpacity = 100
    app.changeCover = False
    app.cover1 = True
    app.coverCounter = 0

    app.meters = 100
    app.onReset = True #Change later
    app.resetTimer = 0
    app.fakeY = 600
    app.resetIter = 7

    app.levels = []
    app.currentLevel = 0

    app.jumpHeight = -20
    app.wallJumpHeight = -20
    app.sideWallVelo = 0
    app.keysHeld = []
    app.inWallJump = False
    app.inSideDash = False
    app.hasDashed = False

    app.direction = {'horizontal': 0,'vertical': 0}
    app.wayHoldingWall = {'left': False, 'right': False}

    app.counter = 0
    app.rX = 0
    app.rY = 0
    app.rW = 0
    app.rH = 0

    app.startTime = 0
    app.finalTime = 0
    app.deaths = 0

    app.currentSong = 0
    app.menu = Sound('sounds/menu.mp3')
    app.game = Sound('sounds/game.mp3')
    app.checkpoint = Sound('sounds/checkpoint.mp3')
    app.win = Sound('sounds/win.mp3')
    app.won = False

    addLevels(app)

def addLevels(app):
    # Adds different levels to the levels list
    # Goes through and adds walls and appends them to each individual wall section in the wall list for the class
    # Same goes for other attributes of each level

    # Level 0
    app.level0 = Level(31, 400)
    app.levels.append(app.level0)

    app.player.x = app.levels[app.currentLevel].resetX
    app.player.y = app.levels[app.currentLevel].resetY

    app.level0.walls.append(Wall(0, 486, 180, 112))
    app.level0.walls.append(Wall(300, 400, 80, 200))
    app.level0.walls.append(Wall(0, 560, 600, 40))
    app.level0.walls.append(Wall(0, 0, 69, 293))
    app.level0.walls.append(Wall(69, 223, 112, 70))
    app.level0.walls.append(Wall(456, 114, 150, 76))
    app.level0.walls.append(Wall(564, 0, 36, 600))
    app.level0.walls.append(Wall(0, 0, 434, 30))
    app.level0.deaths.append(Death(180, 544, 120, 20))
    app.level0.deaths.append(Death(380, 541, 184, 20))
    app.level0.signs.append(Sign('''PRESS C TO JUMP
PRESS X TO DASH IN THE AIR
ARROWS KEYS DIRECT YOUR DASH''', 121, 436))
    app.level0.clears.append(Clear(434, 0, 130, 1))

    # Level 1
    app.level1 = Level(50, 470)
    app.levels.append(app.level1)

    app.level1.walls.append(Wall(0, 532, 276, 68))
    app.level1.walls.append(Wall(0, 263, 147, 184))
    app.level1.walls.append(Wall(0, 0, 41, 264))
    app.level1.walls.append(Wall(0, 0, 433, 41))
    app.level1.walls.append(Wall(393, 0, 41, 217))
    app.level1.walls.append(Wall(262, 226, 37, 374))
    # app.level1.walls.append(Wall(297, 525, 114, 73))
    app.level1.walls.append(Wall(562, 0, 38, 410))
    app.level1.walls.append(Wall(522, 225, 40, 185))
    app.level1.walls.append(Wall(459, 346, 99, 64))

    app.level1.deaths.append(Death(262, 216, 37, 10))
    app.level1.signs.append(Sign('''WHEN NEXT TO A WALL
PRESS C TO WALL JUMP
YOU DON'T NEED TO HOLD ARROW KEYS''', 143, 482))

    app.level1.clears.append(Clear(434, 1, 128, 1))

    #Level 2
    app.level2 = Level(31, 470)
    app.levels.append(app.level2)

    app.level2.walls.append(Wall(188, 562, 37, 38))
    app.level2.walls.append(Wall(263, 450, 148, 35))
    app.level2.walls.append(Wall(301, 482, 73, 118))
    app.level2.walls.append(Wall(488, 562, 110, 38))
    app.level2.walls.append(Wall(526, 298, 74, 296))
    app.level2.walls.append(Wall(0, 0, 185, 184))
    app.level2.walls.append(Wall(132, 0, 167, 37))
    app.level2.walls.append(Wall(0, 180, 263, 111))
    app.level2.walls.append(Wall(259, 253, 152, 38))
    app.level2.walls.append(Wall(0, 525, 110, 75))

    app.level2.walls.append(Wall(474, 0, 126, 116))
    app.level2.walls.append(Wall(587, 115, 13, 185))
    app.level2.walls.append(Wall(261, 290, 150, 35))

    app.level2.deaths.append(Death(263, 434, 148, 16))
    app.level2.deaths.append(Death(263, 237, 148, 16))

    app.level2.springs.append(Spring(188, 552, 37, 10))
    app.level2.springs.append(Spring(488, 552, 38, 10))

    app.level2.signs.append(Sign('''PINK
IS
BOUNCY''', 72, 475))

    app.level2.clears.append(Clear(299, 0, 175, 1))

    #Level 3
    app.level3 = Level(38, 384)
    app.levels.append(app.level3)

    app.level3.walls.append(Wall(0, 450, 146, 150))
    app.level3.walls.append(Wall(0, 0, 82, 120))
    app.level3.walls.append(Wall(0, 100, 245, 35))
    app.level3.walls.append(Wall(186, 0, 414, 24))
    app.level3.walls.append(Wall(559, 0, 41, 186))
    app.level3.walls.append(Wall(449, 490, 151, 110))
    app.level3.walls.append(Wall(225, 280, 70, 336))
    app.level3.walls.append(Wall(375, 189, 74, 151))
    app.level3.walls.append(Wall(417, 299, 66, 71))

    app.level3.deaths.append(Death(225, 259, 70, 21))
    app.level3.deaths.append(Death(375, 168, 74, 21))

    app.level3.clears.append(Clear(82, 0, 104, 2))

    #Level 4
    app.level4 = Level(40,377)
    app.levels.append(app.level4)

    app.level4.walls.append(Wall(0, 450, 109, 150))
    app.level4.walls.append(Wall(103, 487, 159, 113))
    app.level4.walls.append(Wall(373, 487, 227, 113))
    app.level4.walls.append(Wall(526, 0, 74, 299))
    app.level4.walls.append(Wall(490, 260, 110, 40))
    app.level4.walls.append(Wall(0, 0, 447, 145))
    app.level4.walls.append(Wall(0, 133, 336, 51))

    app.level4.recharges.append(Recharge(300, 300, 35, 35)) 

    app.level4.signs.append(Sign('''THAT IS A RECHARGE CRYSTAL
USE IT TO GAIN BACK A DASH
THEY RESPAWN AFTER A LITTLE BIT''', 167, 438))

    app.level4.clears.append(Clear(446, 0, 80, 2)) 

    #Level 5
    app.level5 = Level(40, 435)
    app.levels.append(app.level5)
    app.level5.walls.append(Wall(0, 0, 131, 148))
    app.level5.walls.append(Wall(0, 145, 50, 253))
    app.level5.walls.append(Wall(0, 523, 153, 77))
    app.level5.walls.append(Wall(152, 338, 102, 262))
    app.level5.walls.append(Wall(224, 225, 150, 375))
    app.level5.walls.append(Wall(226, 225, 374, 74))
    app.level5.walls.append(Wall(474, 135, 126, 110))
    app.level5.walls.append(Wall(532, 0, 68, 197))


    app.level5.signs.append(Sign('''_CELESTE MOUNTAIN_
THIS MEMORIAL TO THOSE
WHO PERISHED ON THE CLIMB''', 293, 176))
    
    app.level5.clears.append(Clear(131, 0, 400, 2))
    #Level 6
    app.level6 = Level(40, 435)
    app.levels.append(app.level6)

    app.level6.walls.append(Wall(0, 0, 37, 302))
    app.level6.walls.append(Wall(18, 227, 65, 75))
    app.level6.walls.append(Wall(0, 520, 150, 80))
    app.level6.walls.append(Wall(187, 0, 413, 73))
    app.level6.walls.append(Wall(525, 72, 75, 193))

    app.level6.walls.append(VanishWall(226, 528, 38, 38))
    app.level6.walls.append(VanishWall(264, 528, 38, 38))
    app.level6.walls.append(VanishWall(302, 528, 38, 38))
    app.level6.walls.append(VanishWall(450, 490, 38, 38))
    app.level6.walls.append(VanishWall(525, 265, 38, 38))
    app.level6.walls.append(VanishWall(525, 303, 38, 38))

    app.level6.deaths.append(Death(37, 220, 46, 8))
    app.level6.springs.append(VanishSpring(450, 482, 38, 8))

    app.level6.recharges.append(Recharge(250, 144, 35, 35)) 

    app.level6.signs.append(Sign('''DARK GRAY PLATFORMS DISSAPEAR
THEY RESPAWN AFTER A LITTLE BIT
OR AFTER YOU DIE''', 85, 470))

    app.level6.clears.append(Clear(37, 0, 150, 2))

    #Level 7
    app.level7 = Level(82,407)
    app.levels.append(app.level7)

    app.level7.walls.append(Wall(0, 565, 600, 75))
    app.level7.walls.append(Wall(326, 585, 274, 35))
    app.level7.walls.append(Wall(0, 0, 70, 200))
    app.level7.walls.append(Wall(74, 480, 36, 100))
    app.level7.walls.append(Wall(530, 0, 70, 250))
    app.level7.walls.append(Wall(190, 0, 600, 70))
    app.level7.walls.append(Wall(414, 530, 84, 64))
    app.level7.walls.append(Wall(190, 0, 70, 150))

    app.level7.deaths.append(Death(0, 545, 74, 21))
    app.level7.deaths.append(Death(110, 545, 304, 21))
    app.level7.deaths.append(Death(498, 545, 102, 21))

    app.level7.springs.append(Spring(414, 519, 84, 11))

    app.level7.recharges.append(Recharge(372, 100, 38, 38))
    app.level7.clears.append(Clear(70, 0, 120, 2))

    #Level 8
    app.level8 = Level(20,430)
    app.levels.append(app.level8)

    app.level8.walls.append(Wall(0, 0, 112, 300))
    app.level8.walls.append(Wall(0, 298, 221, 39))
    app.level8.walls.append(Wall(86, 149, 64, 152))
    app.level8.walls.append(Wall(0, 526, 74, 74))
    app.level8.walls.append(Wall(478, 222, 35, 147))
    app.level8.walls.append(Wall(441, 301, 72, 69))
    app.level8.walls.append(Wall(262, 0, 338, 74))
    app.level8.walls.append(Wall(588, 68, 50, 600))

    app.level8.deaths.append(Death(149, 277, 72, 21))
    app.level8.deaths.append(Death(441, 282, 37, 21))

    app.level8.walls.append(VanishWall(186, 525, 38, 38))
    app.level8.walls.append(VanishWall(224, 525, 38, 38))
    app.level8.walls.append(VanishWall(375, 525, 38, 38))
    app.level8.walls.append(VanishWall(413, 525, 38, 38))

    app.level8.clears.append(Clear(110, 0, 152, 2))

    #Level 9
    app.level9 = Level(6,476)
    app.levels.append(app.level9)
    app.level9.walls.append(Wall(0, 526, 38, 74))
    app.level9.walls.append(Wall(190, 562, 38, 38))
    app.level9.walls.append(Wall(0, 0, 182, 408))
    app.level9.walls.append(Wall(172, 114, 312, 73))
    app.level9.walls.append(Wall(484, 150, 38, 34))
    app.level9.walls.append(Wall(370, 75, 114, 185))
    app.level9.walls.append(Wall(370, 145, 38, 153))
    app.level9.walls.append(Wall(523, 338, 77, 112))
    app.level9.walls.append(Wall(446, 0, 154, 35))
    app.level9.walls.append(Wall(180, 0, 136, 132))
    app.level9.walls.append(Wall(291, 75, 91, 45))

    app.level9.walls.append(VanishWall(370, 298, 38, 38))
    app.level9.walls.append(VanishWall(370, 336, 38, 38))

    app.level9.springs.append(Spring(190, 551, 38, 11))

    app.level9.deaths.append(Death(0, 408, 182, 20))
    app.level9.deaths.append(Death(182, 187, 188, 20))

    app.level9.clears.append(Clear(316, 0, 130, 2))

    #Level 10
    app.level10 = Level(6,476)
    app.levels.append(app.level10)
    app.level10.walls.append(Wall(0, 526, 183, 74))
    app.level10.walls.append(Wall(118, 302, 146, 72))
    app.level10.walls.append(Wall(192, 370, 113, 35))
    app.level10.walls.append(Wall(261, 338, 193, 34))
    app.level10.walls.append(Wall(267, 390, 38, 97))
    app.level10.walls.append(Wall(342, 563, 39, 39))
    app.level10.walls.append(Wall(550, 450, 39, 150))
    app.level10.walls.append(Wall(344, 0, 256, 106))
    app.level10.walls.append(Wall(418, 100, 195, 148))

    app.level10.springs.append(Spring(342, 554, 39, 10))
    app.level10.springs.append(Spring(550, 439, 39, 12))

    app.level10.deaths.append(Death(118, 282, 146, 20))
    app.level10.deaths.append(Death(247, 405, 20, 82))
    app.level10.deaths.append(Death(418, 248, 182, 20))
    app.level10.clears.append(Clear(0, 0, 343, 2))

    #Level 11
    app.level11 = Level(42,382)
    app.levels.append(app.level11)
    app.level11.walls.append(Wall(0, 0, 72, 373))
    app.level11.walls.append(Wall(0, 370, 34, 230))
    app.level11.walls.append(Wall(72, 279, 72, 131))
    app.level11.walls.append(Wall(17, 146, 242, 153))
    app.level11.walls.append(Wall(90, 146, 397, 77))
    app.level11.walls.append(Wall(452, 222, 35, 34))
    app.level11.walls.append(Wall(222, 0, 113, 73))
    app.level11.walls.append(Wall(262, 0, 338, 37))

    app.level11.walls.append(VanishWall(34, 410, 38, 38))

    app.level11.deaths.append(Death(452, 255, 35, 12))

    app.level11.recharges.append(Recharge(154, 360, 35, 35))
    app.level11.recharges.append(Recharge(271, 255, 35, 35))
    app.level11.recharges.append(Recharge(525, 248, 35, 35))

    app.level11.clears.append(Clear(72, 0, 150, 2))

    #Summit
    app.summit = Level(42,410)
    app.levels.append(app.summit)

    app.summit.walls.append(Wall(0, 550, 600, 50))
    app.summit.walls.append(Wall(100, 400, 400, 150))
    app.summit.walls.append(Wall(160, 200, 280 ,200))
    app.summit.signs.append(Sign('', 291, 150))

def safeIndex(lst, item):
    return lst.index(item) if item in lst else -1

def redrawAll(app):
    # If I'm in the title, i draw the cover. Flashes the other cover too occasionaly for effect
    if app.inTitle:
        drawRect(0, 0, 600, 600, fill = 'black')
        if app.cover1:
            drawImage('bad-celeste\images\cover.png', 0, 0, width = 600, height = 600, opacity = app.coverOpacity)
        else:
            drawImage('bad-celeste\images\cover2.png', 0, 0, width = 600, height = 600, opacity = app.coverOpacity)
    else:
    # Otherwise I start drawing everything else
        drawRect(0, 0, 600, 600, fill = rgb(200, 200, 200))
        # Draw all the walls
        for wall in app.levels[app.currentLevel].walls:
            if isinstance(wall, VanishWall):
                drawRect(wall.x, wall.y, wall.width, wall.height, fill = wall.color, opacity = wall.opacity)
            else:
                drawRect(wall.x, wall.y, wall.width, wall.height, fill = wall.color)
        # Draw all the deaths
        for death in app.levels[app.currentLevel].deaths:
            drawRect(death.x, death.y, death.width, death.height, fill = death.color)
        # Draw all the springs
        for spring in app.levels[app.currentLevel].springs:
            if isinstance(spring, VanishSpring):
                drawRect(spring.x, spring.y, spring.width, spring.height, fill = spring.color, opacity = spring.opacity)
            else:
                drawRect(spring.x, spring.y, spring.width, spring.height, fill = spring.color)
        # Draw all the recharges
        for recharge in app.levels[app.currentLevel].recharges:
            if recharge.visible and recharge.opacity == 100:
                drawRect(recharge.x, recharge.y, recharge.sideLength, recharge.sideLength, rotateAngle = 45, 
                         fill = 'lime', align = 'left-top', borderWidth = 2, border = rgb(34, 36, 33))
            else:
                drawRect(recharge.x, recharge.y, recharge.sideLength, recharge.sideLength, 
                         rotateAngle = 45, fill = rgb(220, 220, 220), align = 'left-top', 
                         borderWidth = 2, border = rgb(150, 150, 150))
                drawRect(recharge.x, recharge.y, recharge.sideLength, recharge.sideLength, 
                         rotateAngle = 45, fill = 'lime', align = 'left-top', opacity = recharge.opacity, 
                         borderWidth = 2, border = rgb(34, 36, 33))
        # Update the end signs and also draw signs differently for specific signs
        for sign in app.levels[app.currentLevel].signs:
            if sign.message == '''_CELESTE MOUNTAIN_
THIS MEMORIAL TO THOSE
WHO PERISHED ON THE CLIMB''':
                drawArc(sign.x + 25, sign.y, 50, 40, 0, 180, fill = rgb(54, 54, 54))
                drawRect(sign.x, sign.y, 50, 50, fill = rgb(54, 54, 54))
            elif app.meters == 1300:
                elapsedTime = app.finalTime - app.startTime
                minutes = int(elapsedTime // 60)
                seconds = int(elapsedTime % 60)
                app.levels[app.currentLevel].signs[0].message = f'''TIME: {minutes}:{seconds:02}
DEATHS: {app.deaths}
THANKS FOR PLAYING!'''
                drawRect(sign.x, sign.y, 5, 50, fill = rgb(150, 87, 21))
                drawArc(sign.x + 2.5, sign.y, 5, 5, 0, 180, fill = rgb(150, 87, 21))
                drawPolygon(sign.x + 5, sign.y, sign.x + 5, sign.y + 20, sign.x + 35, 
                            sign.y + 10, fill = rgb(88, 168, 27))
            else:
                drawRect(sign.x, sign.y + 5, 50, 30, fill = sign.color)
                drawRect(sign.x + 22, sign.y + 30, 5, 20, fill = sign.color)
        if not app.onReset:
            drawRect(app.player.x, app.player.y, app.player.size, app.player.size, 
                     fill = app.player.fill, border = 'black', borderWidth = 1.5)
        if app.onReset:
            drawRect(175, 265, 250, 70, fill = 'black')
            drawRect(app.levels[app.currentLevel].resetX, app.fakeY, app.player.size, 
                     app.player.size, fill = app.player.fill, border = 'black', borderWidth = 1.5)
            if app.meters != 1300:
                drawLabel(f'{app.meters} M', 300, 300, font='Bytesized', size=50, fill = 'white')
            else:
                drawLabel('SUMMIT', 300, 300, font='Bytesized', size=50, fill = 'white')
        # Goes through each row of the message in the sign (multiline strings)
        # Since each character in the font is the same width, you can space them evenly
        # Reminder to PLEASE check read me to download "bytesized" font or else this will look awful
        for sign in app.levels[app.currentLevel].signs:
            if sign.display:
                oldCounter = sign.counter
                lineCounter = -1
                drawRect(0, 170, 600, 96, fill = 'black')
                for line in sign.message.splitlines():
                    lineCounter += 1
                    letterCounter = -1
                    for letter in line:
                        letterCounter += 1
                        if sign.counter >= 0:
                            if letter.isspace():
                                sign.counter -= 1
                                continue
                            drawLabel(letter, letterCounter * 16 + ((app.width - 16 * len(line)) // 2), 
                                      187 + lineCounter * 28, font = 'Bytesized', size = 35, fill = 'white')
                            sign.counter -= 1
                sign.counter = oldCounter

# --------------- onStep Methods ---------------

# Below are all of the methods I call each step

def checkSong(app):
    if app.currentSong == 0:
        app.menu.play(loop = True)
    elif app.currentSong == 1:
        app.menu.pause()
        app.game.play(loop = True)
    elif app.currentSong == 2:
        app.game.pause()
        app.checkpoint.play(loop = True)
    elif app.currentSong == 3:
        app.checkpoint.pause()
        app.game.play(loop = True)

def updatePos(app):
    if not app.onReset:
        # If I am holding a wall, I slide down it
        # Also I can't go faster than my terminal velocity in my player class
        app.player.setHoldingWall(app.wayHoldingWall, app.levels[app.currentLevel].walls)
        if abs(app.player.veloX) < 10 or not app.inSideDash: 
            if not app.player.holdingWall or (app.player.holdingWall and app.player.veloY < 0):
                if app.player.veloY + app.player.gravity < app.player.tv:
                    app.player.veloY += app.player.gravity
            else:
                if app.player.veloY + app.player.gravity * 0.25 < app.player.tv:
                    app.player.veloY += app.player.gravity * 0.25
        if abs(app.player.veloX) < 10:
            app.inSideDash = False

# change my x position by velocity of X and don't go into any walls
        app.player.x += app.player.veloX
        for wall in app.levels[app.currentLevel].walls:
            if app.player.touchingWall(wall):
                checkVisibleWall(wall)
                if app.player.veloX > 0: 
                    app.player.x = wall.x - app.player.size
                elif app.player.veloX < 0: 
                    app.player.x = wall.x + wall.width
                app.player.veloX = 0

# same here but for y
        app.player.y += app.player.veloY
        for wall in app.levels[app.currentLevel].walls:
            if app.player.touchingWall(wall):
                checkVisibleWall(wall)
                if app.player.veloY > 0: 
                    app.player.y = wall.y - app.player.size
                elif app.player.veloY < 0:
                    app.player.y = wall.y + wall.height
                app.player.veloY = 0

        if abs(app.player.veloX) > 2:
            app.player.veloX -= 2 * (1 if app.player.veloX > 0 else -1)
        else:
            app.player.veloX = 0
        
        if app.player.x + app.player.size > app.width:
            app.player.x = app.width - app.player.size
        if app.player.x < 0:
            app.player.x = 0
    
def checkVisibleWallTimer(app):
    for wall in app.levels[app.currentLevel].walls:
        if isinstance(wall, VanishWall) and not wall.visible:
            if wall.opacity > 0:
                wall.opacity -= 5
            elif 0 <= wall.timer <= 100:
                wall.timer -= 1
            else:
                wall.visible = True
                wall.opacity = 20
                wall.timer = 100
                if app.player.touchingWall(wall):
                    wall.visible = False
                    wall.opacity = 0
                    wall.timer = 0
        elif isinstance(wall, VanishWall):
            if wall.opacity < 100:
                wall.opacity += 20
                if wall.opacity > 100:
                    wall.opacity = 100

def checkVisibleSpringTimer(app):
    for spring in app.levels[app.currentLevel].springs:
        if isinstance(spring, VanishSpring) and not spring.visible:
            if spring.opacity > 0:
                spring.opacity -= 5
            elif 0 <= spring.timer <= 100:
                spring.timer -= 1
            else:
                spring.visible = True
                spring.opacity = 20
                spring.timer = 100
                if app.player.touchingWall(spring):
                    spring.visible = False
                    spring.opacity = 0
                    spring.timer = 0
        elif isinstance(spring, VanishSpring):
            if spring.opacity < 100:
                spring.opacity += 20

def checkRechargeTimer(app):
    for recharge in app.levels[app.currentLevel].recharges:
        if not recharge.visible:
            if 0 <= recharge.timer <= 100:
                recharge.timer -= 1.5
                recharge.opacity = 0
            else:
                recharge.visible = True
                recharge.timer = 100
        else:
            if recharge.opacity < 100 and recharge.visible:
                recharge.opacity += 25

def checkClear(app):
    for clear in app.levels[app.currentLevel].clears:
        if app.player.touchingWall(clear):
            app.currentLevel += 1
            if app.currentLevel == len(app.levels):
                app.currentLevel = 0
            app.player.x = app.levels[app.currentLevel].resetX
            app.player.y = app.levels[app.currentLevel].resetY
            app.sideWallVelo = 0
            app.player.veloX = 0
            app.player.veloY = 0
            app.inWallJump = False
            app.inSideDash = False
            app.hasDashed = False
            app.onReset = True
            app.meters += 100
            if app.meters == 600 or app.meters == 1300:
                app.currentSong = 2
            else:
                if app.currentSong == 2: 
                    app.currentSong = 3
                else:
                    app.currentSong = 1

def checkFallen(app):
    if app.player.y > app.height:
        app.player.x = app.levels[app.currentLevel].resetX
        app.player.y = app.levels[app.currentLevel].resetY
        app.player.veloX = 0
        app.player.veloY = 0
        app.inWallJump = False
        app.inSideDash = False
        app.hasDashed = False
        app.onReset = True
        app.deaths += 1
        resetHiddenWalls(app)

def checkDeath(app):
    for death in app.levels[app.currentLevel].deaths:
        if app.player.touchingWall(death):
            app.player.x = app.levels[app.currentLevel].resetX
            app.player.y = app.levels[app.currentLevel].resetY
            app.player.veloX = 0
            app.player.veloY = 0
            app.inWallJump = False
            app.inSideDash = False
            app.hasDashed = False
            app.onReset = True
            app.deaths += 1
            resetHiddenWalls(app)

def checkSpring(app):
    for spring in app.levels[app.currentLevel].springs:
        if app.player.touchingWall(spring):
            if isinstance(spring, VanishSpring):
                spring.visible = False
            app.player.jump(app.levels[app.currentLevel].springs, app.jumpHeight * 1.37)
            app.hasDashed = False

def checkRecharge(app):
    for recharge in app.levels[app.currentLevel].recharges:
        if app.player.touchingWall(recharge) and recharge.visible:
            recharge.visible = False
            app.hasDashed = False

def checkSign(app):
    for sign in app.levels[app.currentLevel].signs:
                    if app.player.touchingWall(sign):
                        if app.meters == 1300 and not app.won:
                            app.win.play()
                            app.won = True
                        sign.display = True
                        sign.counter += 1
                    else:
                        sign.display = False
                        sign.counter = 0

def checkWallVeloColide(app):
    # Make sure I don't go into walls when wall jumping off of other walls
    if app.sideWallVelo > 0:
        direction = 1
    else:
        direction = -1
    for i in range(abs(int(app.sideWallVelo))):
        app.player.x += direction
        collided = False
        for wall in app.levels[app.currentLevel].walls:
            if app.player.touchingWall(wall):
                checkVisibleWall(wall)
                app.player.x -= direction
                app.sideWallVelo = 0
                collided = True
                break
        if collided:
            break

def monitorWallJump(app):
    if app.sideWallVelo > 0:
        app.sideWallVelo -= 2
    elif app.sideWallVelo < 0:
        app.sideWallVelo += 2
    if app.sideWallVelo == 0:
        app.inWallJump = False

def checkTouchingBottom(app):
    app.player.y += 1
    for wall in app.levels[app.currentLevel].walls:
        if app.player.touchingWall(wall):
            checkVisibleWall(wall)
            app.hasDashed = False
    app.player.y -= 1

def checkVisibleWall(wall):
    if isinstance(wall, VanishWall) and wall.visible:
        wall.visible = False

def setColor(app):
    if not app.hasDashed:
        app.player.fill = rgb(250, 115, 167)
    else:
        app.player.fill = rgb(41,173,255)

def resetPosAsthetic(app):
    # Makes me look cool when I start a level or die
    if app.onReset:
        nextStep = False
        if app.fakeY > app.levels[app.currentLevel].resetY + 28:
            for newY in ([1] * 10):
                app.fakeY -= newY
                if app.fakeY > app.levels[app.currentLevel].resetY + 28:
                    continue
                else:
                    app.fakeY = app.levels[app.currentLevel].resetY + 28
                    nextStep = True
        else:
            nextStep = True
        if nextStep:
            app.fakeY -= app.resetIter
            app.resetIter -= 1
            if app.resetIter <= -1:
                app.resetIter = 7
                app.fakeY = 600
                app.onReset = False

def checkFinished(app):
    if app.meters >= 1300 and app.finalTime == 0:
        app.finalTime = time.time()
# ----------------------------------------------

def onStep(app):
    checkSong(app)
    if not app.inTitle:
        updatePos(app)
        checkVisibleWallTimer(app)
        checkVisibleSpringTimer(app)
        checkRechargeTimer(app)
        checkClear(app)
        checkFallen(app)
        checkDeath(app)
        checkSpring(app)
        checkRecharge(app)
        checkSign(app)
        checkWallVeloColide(app)
        monitorWallJump(app)
        checkTouchingBottom(app)
        setColor(app)
        resetPosAsthetic(app)
        checkFinished(app)

    elif app.changeCover:
        if app.coverCounter % 4 == 0:
            app.cover1 = not app.cover1
        app.coverCounter += 1
        if app.coverCounter >= 32:
            app.inTitle = False
            app.currentSong = 1
            app.startTime = time.time()

def resetHiddenWalls(app):
    for wall in app.levels[app.currentLevel].walls:
        if isinstance(wall, VanishWall):
            wall.visible = True
            # wall.opacity = 100
            wall.timer = 100
    for recharge in app.levels[app.currentLevel].recharges:
        recharge.visible = True
        recharge.timer = 100
    for spring in app.levels[app.currentLevel].springs:
        spring.visible = True
        spring.timer = 100

def onMousePress(app, mouseX, mouseY):
    # Draws walls for me that I can copy and paste above in my addLevels function
    if app.counter == 0:
        app.rX = mouseX
        app.rY = mouseY
    elif app.counter == 1:
        app.rW = mouseX - app.rX
        app.rH = mouseY - app.rY
        if app.rX < 6:
            app.rX = 0
        if app.rY < 6:
            app.rY = 0
        if 600 - app.rX - app.rW < 12:
            app.rW = 600 - app.rX
        if 600 - app.rY - app.rH < 12:
            app.rH = 600 - app.rY
        print(f'app.level10.deaths.append(Death({app.rX}, {app.rY}, {app.rW}, {app.rH}))')
    app.counter += 1
    if app.counter == 2:
        app.counter = 0

def onKeyPress(app, key):
    if app.inTitle:
        app.changeCover = True
    else:
        if not app.onReset:
            if 'c' in key:
                if app.player.veloY != 0:
                    # Make sure I don't phase again
                    app.player.x -= 1
                    for wall in app.levels[app.currentLevel].walls:
                        if app.player.touchingWall(wall):
                            checkVisibleWall(wall)
                            app.sideWallVelo += 22
                            app.player.jump(app.levels[app.currentLevel].walls, app.wallJumpHeight)
                            app.inWallJump = True
                            break
                    app.player.x += 1
                if app.player.veloY != 0:
                    app.player.x += 1
                    for wall in app.levels[app.currentLevel].walls:
                        if app.player.touchingWall(wall):
                            checkVisibleWall(wall)
                            app.sideWallVelo -= 22
                            app.player.jump(app.levels[app.currentLevel].walls, app.wallJumpHeight)
                            app.inWallJump = True
                            break
                    app.player.x -= 1
                
                app.player.jump(app.levels[app.currentLevel].walls, app.jumpHeight)
            # Set the direction of my dash
            if 'x' in key and not app.hasDashed:
                app.direction['horizontal'] = 0
                app.direction['vertical'] = 0

                if 'up' in app.keysHeld:
                    app.direction['vertical'] -= 20
                if 'down' in app.keysHeld and 'up' not in app.keysHeld:
                    app.direction['vertical'] += 20

                if 'right' in app.keysHeld and 'left' not in app.keysHeld:
                    app.direction['horizontal'] += 20
                if 'left' in app.keysHeld and 'right' not in app.keysHeld:
                    app.direction['horizontal'] -= 20

                if app.direction['horizontal'] == 0 and app.direction['vertical'] == 0:
                    app.direction['vertical'] = -20
                app.hasDashed = True
                if app.direction['horizontal'] == 0 and app.direction['vertical'] != 0:
                    app.direction['vertical'] *= 1.2
                if app.direction['horizontal'] != 0 and app.direction['vertical'] == 0:
                    app.direction['horizontal'] *= 1.2
                    app.inSideDash = True
                app.player.dash(app.direction)
        if 'a' in key:
            print(app.player.x, app.player.y)
            print(app.deaths)
        # Press q to skip levels
        if 'q' in key:
            if app.meters != 1300:
                app.currentLevel += 1
                if app.currentLevel == len(app.levels):
                    app.currentLevel = 0
                app.player.x = app.levels[app.currentLevel].resetX
                app.player.y = app.levels[app.currentLevel].resetY
                app.player.veloX = 0
                app.player.veloY = 0
                app.inWallJump = False
                app.inSideDash = False
                app.hasDashed = False
                app.onReset = True
                app.meters += 100
                if app.meters == 600 or app.meters == 1300:
                    app.currentSong = 2
                else:
                    if app.currentSong == 2: 
                        app.currentSong = 3
                    else:
                        app.currentSong = 1

def onKeyHold(app, key):
    for i in key:
        if i not in app.keysHeld:
            app.keysHeld.append(i)
    originalX = app.player.x
    if not app.onReset:
        # Double check which way I'm going
        # Because keysHeld has a hierarchy of which ones come first I can use this to see which way I'm going
        if not (safeIndex(app.keysHeld, 'left') == -1 and safeIndex(app.keysHeld, 'right') == -1):
            if safeIndex(app.keysHeld, 'left') > safeIndex(app.keysHeld, 'right'):
                if not app.inWallJump and abs(app.player.veloX) < 10:
                    for dx in range(1, app.speed + 1):
                        app.player.x = originalX - dx
                        hitWall = False
                        for wall in app.levels[app.currentLevel].walls:
                            if app.player.touchingWall(wall):
                                checkVisibleWall(wall)
                                hitWall = True
                                break
                        if hitWall:
                            app.player.x = originalX - (dx - 1)
                            app.wayHoldingWall['left'] = True
                            break
                        else:
                            app.player.x = originalX - app.speed
                            app.wayHoldingWall['left'] = False
                        if app.player.x < 0:
                            app.player.x = 0
            else:
                if not app.inWallJump and abs(app.player.veloX) < 10:
                    for dx in range(1, app.speed + 1):
                        app.player.x = originalX + dx
                        hitWall = False
                        for wall in app.levels[app.currentLevel].walls:
                            if app.player.touchingWall(wall):
                                checkVisibleWall(wall)
                                hitWall = True
                                break
                        if hitWall:
                            app.player.x = originalX + (dx - 1)
                            app.wayHoldingWall['right'] = True
                            break
                        else:
                            app.player.x = originalX + app.speed
                            if app.player.x + app.player.size > app.width:
                                app.player.x = app.width - app.player.size
                            app.wayHoldingWall['right'] = False

def onKeyRelease(app, key):
    if key in app.keysHeld:
        app.keysHeld.remove(key)
    for i in app.wayHoldingWall:
        if i not in app.keysHeld:
            app.wayHoldingWall[i] = False

def main():
    runApp()

main()