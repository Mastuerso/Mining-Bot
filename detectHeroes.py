import pyautogui
import os

#Locate on Screen
#print(os.getcwd())
#print(os.listdir())

pyautogui.click('NoxLogo.PNG')
count = 0

with os.scandir('PVP Data/Heroes') as heroes:
    for heroDir in heroes:
        #print(heroDir.name)
        if not heroDir.name.startswith('.'):
            heroFullDir = 'PVP Data/Heroes/' + heroDir.name
            print(heroDir.name)
            currentHero = heroDir.name        
            with os.scandir(heroFullDir) as heroImgs:            
                for heroImg in heroImgs:
                    print(heroImg.name)
                    currentHDir = 'PVP Data/Heroes/' + heroDir.name + "/" + heroImg.name
                    try:
                        #print(pyautogui.locateOnScreen(currentHDir, confidence=0.6, grayscale=True))
                        heroLocation = pyautogui.locateOnScreen(currentHDir, grayscale=False)
                        heroPoint = pyautogui.center(heroLocation)
                        pyautogui.moveTo(heroPoint.x, heroPoint.y)
                        count = count + 1
                    except:
                        #print("Item not Found")
                        errCount = 1
print("Detected: %(count)01d" % {"count": count})

