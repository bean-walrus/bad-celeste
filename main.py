from cmu_graphics import *
from player import Player
from wall import *
from death import Death
from spring import *
from recharge import Recharge
from clear import Clear
from level import Level
import random

def onAppStart(app):
    app.player = Player()
    app.width = 600
    app.height = 600
    app.speed = 10
    app.stepsPerSecond = 40

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

    addLevels(app)

def addLevels(app):
    # Level 0
    app.level0 = Level(31, 400)
    app.levels.append(app.level0)

    app.player.x = app.levels[app.currentLevel].resetX
    app.player.y = app.levels[app.currentLevel].resetY

    app.level0.walls.append(Wall(0, 486, 180, 112))
    app.level0.walls.append(Wall(300, 400, 80, 200))
    app.level0.walls.append(Wall(0, 560, 600, 40))

    # app.level0.walls.append(VanishWall(306, 373, 68, 38))

    # app.level0.springs.append(Spring(250, 300, 68, 38))
    

    app.level0.walls.append(Wall(0, 0, 69, 293))
    app.level0.walls.append(Wall(69, 223, 112, 70))
    app.level0.walls.append(Wall(456, 114, 150, 76))
    app.level0.walls.append(Wall(564, 0, 36, 600))
    app.level0.walls.append(Wall(0, 0, 434, 30))

    app.level0.deaths.append(Death(180, 544, 120, 20))
    app.level0.deaths.append(Death(380, 541, 184, 20))

    app.level0.clears.append(Clear(434, 0, 130, 1))

    # Level 1
    app.level1 = Level(50, 500)
    app.levels.append(app.level1)


    app.level1.walls.append(Wall(0, 562, 276, 38))
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

    app.level2.clears.append(Clear(299, 0, 175, 1))

    #Level 3
    app.level3 = Level(38, 384)
    app.levels.append(app.level3)

    app.level3.walls.append(Wall(0, 450, 146, 150))
    app.level3.walls.append(Wall(0, 0, 82, 130))
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
    app.level4 = Level(10,377)
    app.levels.append(app.level4)

    app.level4.walls.append(Wall(0, 450, 109, 150))
    app.level4.walls.append(Wall(103, 487, 159, 113))
    app.level4.walls.append(Wall(373, 487, 227, 113))
    app.level4.walls.append(Wall(526, 0, 74, 299))
    app.level4.walls.append(Wall(490, 260, 110, 40))
    app.level4.walls.append(Wall(0, 0, 447, 145))
    app.level4.walls.append(Wall(0, 133, 336, 51))

    app.level4.recharges.append(Recharge(300, 300, 35, 35)) 

    app.level4.clears.append(Clear(446, 0, 80, 2)) 

    #Level 5
    app.level5 = Level(10,524)
    app.levels.append(app.level5)

    app.level5.walls.append(Wall(0, 0, 37, 302))
    app.level5.walls.append(Wall(18, 227, 65, 75))
    app.level5.walls.append(Wall(0, 566, 150, 34))
    app.level5.walls.append(Wall(187, 0, 413, 73))
    app.level5.walls.append(Wall(525, 72, 75, 193))

    app.level5.walls.append(VanishWall(226, 528, 38, 38))
    app.level5.walls.append(VanishWall(264, 528, 38, 38))
    app.level5.walls.append(VanishWall(302, 528, 38, 38))
    app.level5.walls.append(VanishWall(450, 490, 38, 38))
    app.level5.walls.append(VanishWall(525, 265, 38, 38))
    app.level5.walls.append(VanishWall(525, 303, 38, 38))

    app.level5.deaths.append(Death(37, 220, 46, 8))
    app.level5.springs.append(VanishSpring(450, 482, 38, 8))

    app.level5.recharges.append(Recharge(250, 144, 35, 35)) 

    app.level5.clears.append(Clear(37, 0, 150, 2))

    #Level 6
    app.level6 = Level(80,380)
    app.levels.append(app.level6)

    app.level6.walls.append(Wall(0, 565, 600, 75))
    app.level6.walls.append(Wall(326, 585, 274, 35))
    app.level6.walls.append(Wall(0, 0, 70, 200))
    app.level6.walls.append(Wall(74, 480, 36, 100))
    app.level6.walls.append(Wall(530, 0, 70, 200))
    app.level6.walls.append(Wall(190, 0, 600, 70))
    app.level6.walls.append(Wall(414, 516, 84, 64))
    app.level6.walls.append(Wall(190, 0, 70, 150))

    app.level6.deaths.append(Death(0, 545, 74, 21))
    app.level6.deaths.append(Death(110, 545, 304, 21))
    app.level6.deaths.append(Death(498, 545, 102, 21))

    app.level6.springs.append(Spring(414, 505, 84, 11))

    app.level6.recharges.append(Recharge(372, 100, 38, 38))
    app.level6.clears.append(Clear(70, 0, 120, 2))


def safeIndex(lst, item):
    return lst.index(item) if item in lst else -1

def redrawAll(app):
    # drawImage('bad-celeste\images\level6.png', 0, 0, width = 600, height = 600)
    for wall in app.levels[app.currentLevel].walls:
        if isinstance(wall, VanishWall):
            drawRect(wall.x, wall.y, wall.width, wall.height, fill = wall.color, opacity = wall.opacity)
        else:
            drawRect(wall.x, wall.y, wall.width, wall.height, fill = wall.color)
    for death in app.levels[app.currentLevel].deaths:
        drawRect(death.x, death.y, death.width, death.height, fill = death.color)
    for spring in app.levels[app.currentLevel].springs:
        if isinstance(spring, VanishSpring):
            drawRect(spring.x, spring.y, spring.width, spring.height, fill = spring.color, opacity = spring.opacity)
        else:
            drawRect(spring.x, spring.y, spring.width, spring.height, fill = spring.color)
    for recharge in app.levels[app.currentLevel].recharges:
        if recharge.visible and recharge.opacity == 100:
            drawRect(recharge.x, recharge.y, recharge.sideLength, recharge.sideLength, rotateAngle = 45, fill = 'lime', align = 'left-top', borderWidth = 2, border = rgb(34, 36, 33))
        else:
            drawRect(recharge.x, recharge.y, recharge.sideLength, recharge.sideLength, rotateAngle = 45, fill = rgb(220, 220, 220), align = 'left-top', borderWidth = 2, border = rgb(150, 150, 150))
            drawRect(recharge.x, recharge.y, recharge.sideLength, recharge.sideLength, rotateAngle = 45, fill = 'lime', align = 'left-top', opacity = recharge.opacity, borderWidth = 2, border = rgb(34, 36, 33))
    for clear in app.levels[app.currentLevel].clears:
        drawRect(clear.x, clear.y, clear.width, clear.height, fill = clear.color, opacity = 0)
    drawRect(app.player.x, app.player.y, app.player.size, app.player.size, fill = app.player.fill)

# --------------- onStep Methods ---------------

def updatePos(app):
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

    app.player.x += app.player.veloX
    for wall in app.levels[app.currentLevel].walls:
        if app.player.touchingWall(wall):
            checkVisibleWall(wall)
            if app.player.veloX > 0: 
                app.player.x = wall.x - app.player.size
            elif app.player.veloX < 0: 
                app.player.x = wall.x + wall.width
            app.player.veloX = 0

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

def checkFallen(app):
    if app.player.y > app.height:
        app.player.x = app.levels[app.currentLevel].resetX
        app.player.y = app.levels[app.currentLevel].resetY
        app.player.veloX = 0
        app.player.veloY = 0
        app.inWallJump = False
        app.inSideDash = False
        app.hasDashed = False
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
            resetHiddenWalls(app)

def checkSpring(app):
    for spring in app.levels[app.currentLevel].springs:
        if app.player.touchingWall(spring):
            if isinstance(spring, VanishSpring):
                spring.visible = False
            app.player.jump(app.levels[app.currentLevel].springs, app.jumpHeight * 1.4)
            app.hasDashed = False

def checkRecharge(app):
    for recharge in app.levels[app.currentLevel].recharges:
        if app.player.touchingWall(recharge) and recharge.visible:
            recharge.visible = False
            app.hasDashed = False

def checkWallVeloColide(app):
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

# ----------------------------------------------

def onStep(app):
    updatePos(app)
    checkVisibleWallTimer(app)
    checkVisibleSpringTimer(app)
    checkRechargeTimer(app)
    checkClear(app)
    checkFallen(app)
    checkDeath(app)
    checkSpring(app)
    checkRecharge(app)
    checkWallVeloColide(app)
    monitorWallJump(app)
    checkTouchingBottom(app)
    setColor(app)


def resetHiddenWalls(app):
    for wall in app.levels[app.currentLevel].walls:
        if isinstance(wall, VanishWall):
            wall.visible = True
            wall.opacity = 100
            wall.timer = 100
    for recharge in app.levels[app.currentLevel].recharges:
        recharge.visible = True
        recharge.timer = 100
    for spring in app.levels[app.currentLevel].springs:
        spring.visible = True
        spring.timer = 100

def onMousePress(app, mouseX, mouseY):
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
        print(f'app.level6.walls.append(Wall({app.rX}, {app.rY}, {app.rW}, {app.rH}))')
    app.counter += 1
    if app.counter == 2:
        app.counter = 0

def onKeyPress(app, key):
    if 'c' in key:
        if app.player.veloY != 0:
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
    if 'q' in key:
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

def onKeyHold(app, key):
    for i in key:
        if i not in app.keysHeld:
            app.keysHeld.append(i)
    originalX = app.player.x
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
                        app.wayHoldingWall['right'] = False

    if app.player.x + app.player.size > app.width:
        app.player.x = app.width - app.player.size
    if app.player.x < 0:
        app.player.x = 0


    if 'r' in key:
        app.player.x = app.levels[app.currentLevel].resetX
        app.player.y = app.levels[app.currentLevel].resetY
        app.player.velo = 0
        app.inWallJump = False
        app.inSideDash = False
        app.hasDashed = False
        resetHiddenWalls(app)

def onKeyRelease(app, key):
    if key in app.keysHeld:
        app.keysHeld.remove(key)
    for i in app.wayHoldingWall:
        if i not in app.keysHeld:
            app.wayHoldingWall[i] = False

def main():
    runApp()

main()