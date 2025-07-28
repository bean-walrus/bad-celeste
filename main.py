from cmu_graphics import *
from player import Player
from wall import Wall
from death import Death
from spring import Spring
from clear import Clear
from level import Level

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
    app.level0 = Level([], [], [], [], 31, 400)
    app.levels.append(app.level0)

    app.player.x = app.levels[app.currentLevel].resetX
    app.player.y = app.levels[app.currentLevel].resetY

    app.level0.walls.append(Wall(False, 0, 486, 180, 112))
    app.level0.walls.append(Wall(False, 300, 400, 80, 200))
    app.level0.walls.append(Wall(False, 0, 560, 600, 40))

    # app.level0.walls.append(Wall(True, 306, 373, 68, 38))

    # app.level0.springs.append(Spring(250, 300, 68, 38))
    

    app.level0.walls.append(Wall(False, 0, 0, 69, 293))
    app.level0.walls.append(Wall(False, 69, 223, 112, 70))
    app.level0.walls.append(Wall(False, 456, 114, 150, 76))
    app.level0.walls.append(Wall(False, 564, 0, 36, 600))
    app.level0.walls.append(Wall(False, 0, 0, 434, 30))

    app.level0.deaths.append(Death(180, 544, 120, 20))
    app.level0.deaths.append(Death(380, 541, 184, 20))

    app.level0.clears.append(Clear(434, 0, 130, 1))

    # Level 1
    app.level1 = Level([], [], [], [], 50, 500)
    app.levels.append(app.level1)


    app.level1.walls.append(Wall(False, 0, 562, 276, 38))
    app.level1.walls.append(Wall(False, 0, 263, 147, 184))
    app.level1.walls.append(Wall(False, 0, 0, 41, 264))
    app.level1.walls.append(Wall(False, 0, 0, 433, 41))
    app.level1.walls.append(Wall(False, 393, 0, 41, 217))
    app.level1.walls.append(Wall(False, 262, 226, 37, 374))
    # app.level1.walls.append(Wall(False, 297, 525, 114, 73))
    app.level1.walls.append(Wall(False, 562, 0, 38, 410))
    app.level1.walls.append(Wall(False, 522, 225, 40, 185))
    app.level1.walls.append(Wall(False, 459, 346, 99, 64))

    app.level1.deaths.append(Death(262, 216, 37, 10))

    app.level1.clears.append(Clear(434, 1, 128, 1))

    #Level 2
    app.level2 = Level([], [], [], [], 31, 470)
    app.levels.append(app.level2)

    app.level2.walls.append(Wall(False, 188, 562, 37, 38))
    app.level2.walls.append(Wall(False, 263, 450, 148, 35))
    app.level2.walls.append(Wall(False, 301, 482, 73, 118))
    app.level2.walls.append(Wall(False, 488, 562, 110, 38))
    app.level2.walls.append(Wall(False, 526, 298, 74, 296))
    app.level2.walls.append(Wall(False, 0, 0, 185, 184))
    app.level2.walls.append(Wall(False, 132, 0, 167, 37))
    app.level2.walls.append(Wall(False, 0, 180, 263, 111))
    app.level2.walls.append(Wall(False, 259, 253, 152, 38))
    app.level2.walls.append(Wall(False, 0, 525, 110, 75))

    app.level2.walls.append(Wall(False, 474, 0, 126, 116))
    app.level2.walls.append(Wall(False, 587, 115, 13, 185))
    app.level2.walls.append(Wall(False, 261, 290, 150, 35))

    app.level2.deaths.append(Death(263, 434, 148, 16))
    app.level2.deaths.append(Death(263, 237, 148, 16))

    app.level2.springs.append(Spring(188, 552, 37, 10))
    app.level2.springs.append(Spring(488, 552, 38, 10))

    app.level2.clears.append(Clear(299, 0, 175, 1))

    
    

def safeIndex(lst, item):
    return lst.index(item) if item in lst else -1

def handleWallCollision(wall):
    if wall.vanish and wall.visible:
        wall.visible = False

def redrawAll(app):
    # drawImage('bad-celeste\images\level2.png', 0, 0, width = 600, height = 600)
    for wall in app.levels[app.currentLevel].walls:
        if wall.visible and not wall.vanish:
            drawRect(wall.x, wall.y, wall.width, wall.height, fill = wall.color)
        else:
            drawRect(wall.x, wall.y, wall.width, wall.height, fill = wall.color, opacity = wall.opacity)
    for death in app.levels[app.currentLevel].deaths:
        drawRect(death.x, death.y, death.width, death.height, fill = death.color)
    for spring in app.levels[app.currentLevel].springs:
        drawRect(spring.x, spring.y, spring.width, spring.height, fill = spring.color)
    for clear in app.levels[app.currentLevel].clears:
        drawRect(clear.x, clear.y, clear.width, clear.height, fill = clear.color, opacity = 0)
    drawRect(app.player.x, app.player.y, app.player.size, app.player.size, fill = app.player.fill)

def checkWallVeloColide(app):
    originalX = app.player.x
    app.player.x += app.sideWallVelo
    for wall in app.levels[app.currentLevel].walls:
        if app.player.touchingWall(wall):
            handleWallCollision(wall)
            app.player.x = originalX
            app.sideWallVelo = 0
            break

def checkTouchingBottom(app):
    app.player.y += 1
    for wall in app.levels[app.currentLevel].walls:
        if app.player.touchingWall(wall):
            handleWallCollision(wall)
            app.hasDashed = False
    app.player.y -= 1

def updatePos(app):
    if abs(app.player.veloX) < 10 or not app.inSideDash: 
        if not app.player.holdingWall:
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
            handleWallCollision(wall)
            if app.player.veloX > 0: 
                app.player.x = wall.x - app.player.size
            elif app.player.veloX < 0: 
                app.player.x = wall.x + wall.width
            app.player.veloX = 0

    app.player.y += app.player.veloY
    for wall in app.levels[app.currentLevel].walls:
        if app.player.touchingWall(wall):
            handleWallCollision(wall)
            if app.player.veloY > 0: 
                app.player.y = wall.y - app.player.size
            elif app.player.veloY < 0:
                app.player.y = wall.y + wall.height
            app.player.veloY = 0

    if abs(app.player.veloX) > 2:
        app.player.veloX -= 2 * (1 if app.player.veloX > 0 else -1)
    else:
        app.player.veloX = 0

def checkVisibleWall(app):
    for wall in app.levels[app.currentLevel].walls:
        if not wall.visible:
            print(wall.timer)
            if wall.opacity > 0:
                wall.opacity -= 5
            elif 0 <= wall.timer <= 100:
                wall.timer -= 1
            else:
                wall.visible = True
                wall.opacity = 100
                wall.timer = 100
                if app.player.touchingWall(wall):
                    wall.visible = False
                    wall.opacity = 0
                    wall.timer = 0

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
            app.player.jump(app.levels[app.currentLevel].springs, app.jumpHeight * 1.4)
            app.hasDashed = False

def checkClear(app):
    for clear in app.levels[app.currentLevel].clears:
        if app.player.touchingWall(clear):
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

def monitorWallJump(app):
    if app.sideWallVelo > 0:
        app.sideWallVelo -= 2
    elif app.sideWallVelo < 0:
        app.sideWallVelo += 2
    if app.sideWallVelo == 0:
        app.inWallJump = False

def setColor(app):
    if not app.hasDashed:
        app.player.fill = rgb(250, 115, 167)
    else:
        app.player.fill = rgb(41,173,255)

def onStep(app):
    app.player.setHoldingWall(app.wayHoldingWall, app.levels[app.currentLevel].walls)
    updatePos(app)
    checkVisibleWall(app)
    checkClear(app)
    checkFallen(app)
    checkDeath(app)
    checkSpring(app)
    checkWallVeloColide(app)
    monitorWallJump(app)
    checkTouchingBottom(app)
    setColor(app)

def resetHiddenWalls(app):
    for wall in app.levels[app.currentLevel].walls:
        if wall.vanish:
            wall.visible = True
            wall.opacity = 100
            wall.timer = 100

def onMousePress(app, mouseX, mouseY):
    if app.counter == 0:
        app.rX = mouseX
        app.rY = mouseY
    elif app.counter == 1:
        app.rW = mouseX - app.rX
        app.rH = mouseY - app.rY
        print(f'app.level2.walls.append(Wall(False, {app.rX}, {app.rY}, {app.rW}, {app.rH}))')
    app.counter += 1
    if app.counter == 2:
        app.counter = 0

def onKeyPress(app, key):
    if 'c' in key:
        if 'left' in app.keysHeld:
            app.player.x -= 1
            for wall in app.levels[app.currentLevel].walls:
                if app.player.touchingWall(wall):
                    handleWallCollision(wall)
                    app.sideWallVelo += 22
                    app.player.jump(app.levels[app.currentLevel].walls, app.wallJumpHeight)
                    app.inWallJump = True
                    break
            app.player.x += 1
        if 'right' in app.keysHeld:
            app.player.x += 1
            for wall in app.levels[app.currentLevel].walls:
                if app.player.touchingWall(wall):
                    handleWallCollision(wall)
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
                            handleWallCollision(wall)
                            hitWall = True
                            break
                    if hitWall:
                        app.player.x = originalX - (dx - 1)
                        app.wayHoldingWall['left'] = True
                        if app.player.veloY < 0:
                            app.player.veloY = 0
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
                            handleWallCollision(wall)
                            hitWall = True
                            break
                    if hitWall:
                        app.player.x = originalX + (dx - 1)
                        app.wayHoldingWall['right'] = True
                        if app.player.veloY < 0:
                            app.player.veloY = 0
                        break
                    else:
                        app.player.x = originalX + app.speed
                        app.wayHoldingWall['right'] = False

    if app.player.x + app.player.size > app.width:
        app.player.x = app.width - app.player.size


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