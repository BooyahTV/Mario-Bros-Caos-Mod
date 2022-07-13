import pvz
import pyautogui
import time
import random

def spawnSunflawer(gridY):
    pvz.selectPlant(1)
    pvz.clickSlot(0, gridY + 1)

# spawn a peashooter in the secound column in front of the zombie
def spawnPeashooter(gridY):
    pvz.selectPlant(0)
    pvz.clickSlot(random.randint(1, 2), gridY + 1)

def checkZombie():
    defaultZombie = pyautogui.locateOnScreen('assets/zombies/default.png', confidence=0.7)

    if(defaultZombie is not None):
        gridX, gridY = pvz.pixelsToGrid(defaultZombie.left - defaultZombie.width /2, defaultZombie.top - defaultZombie.height / 2)

        if(gridX is not None and gridY is not None):
            print('zombie at', str(gridX), str(gridY))
            # random 50/50
            if(random.randint(0, 2) == 0):
                spawnSunflawer(gridY)
            else:
                spawnPeashooter(gridY)


# find suns every 0.2 secounds
while(True):
    checkZombie()

    pvz.collectSun()
    pvz.clickMenuButtons()

    time.sleep(0.2)
