import pyautogui
import time

selectedPlant = ''
selecting = False
suns = 50

debug = True
# sizes and offsets


cardWidth = 55
firstPlantMenuX = 125
firstPlantMenuY = 70

gridOffsetX = 80
gridOffsetY = 155

gridSizeX = 90
gridSizeY = 110

slotsX = 9
slotsY = 5

def isPausedOrMenu():
    menu = pyautogui.locateOnScreen('assets/menu/menu.png', confidence=0.8)
    paused = pyautogui.locateOnScreen('assets/menu/paused.png', confidence=0.8)

    return menu is not None or paused is not None

# clicks the center of a box (button, card,etc)
def clickBox(button):
    if(button is not None):
        pyautogui.click(button.left + button.width/2, button.top + button.height/2)
        return True
    return False

#resuming/unpausing the game if needed
def resumeGame():

    resumeBtn = pyautogui.locateOnScreen('assets/menu/resume.png', confidence=0.7)
    unpauseBtn = pyautogui.locateOnScreen('assets/menu/unpause.png', confidence=0.7)
    
    
    clickBox(resumeBtn)
    clickBox(unpauseBtn)
    
    time.sleep(0.2)

def collectSun():
    if selecting or isPausedOrMenu():
        return

    sun = pyautogui.locateOnScreen('assets/sun.png', confidence=0.7)
    clickBox(sun)

def selectPlant(index):
    if isPausedOrMenu():
        return
    print('selecting plant', str(index))
    selecting = True

    #windowPosition = pyautogui.locateOnScreen('assets/menu/window.png', confidence=0.7)
    #if(windowPosition is not None):

    # position from the first plant relative to the game window
    plantX = 0 + (cardWidth * int(index)) + firstPlantMenuX
    plantY = 0 + firstPlantMenuY
    
    
    pyautogui.click(plantX, plantY)

def clickSlot(x, y):
    if isPausedOrMenu():
        return

    selecting = False

    posX, posY = gridToPixels(x, y)

    print('putting a plant in', str(x), str(y))
    pyautogui.click(posX, posY)

# clicks every button in the gui to continue
def clickMenuButtons():
    arrow = pyautogui.locateOnScreen('assets/menu/unlock.jpg', confidence=0.8)
    if(arrow is not None):
        pyautogui.click(arrow.left + arrow.width/2, arrow.top + 50)

    tryagain = pyautogui.locateOnScreen('assets/menu/tryagain.png', confidence=0.6)
    clickBox(tryagain)

    nextlevel = pyautogui.locateOnScreen('assets/menu/nextlevel.jpg', confidence=0.6)
    clickBox(nextlevel)
    
    
def gridToPixels(x, y):
    # multiply by the size of the grid
    posX = gridOffsetX + gridSizeX * x
    posY = gridOffsetY + gridSizeY * y

    return posX, posY

def pixelsToGrid(x, y):
    # substract the offset from the position
    x = x - gridOffsetX + gridSizeX/2
    y = y - gridOffsetY + gridSizeY/2

    # divide by the size of the grid
    x = int(x / gridSizeX)
    y = int(y / gridSizeY)

    return x, y
