import pyautogui
import os
from miningbot import gather

go_flag = False
try:
    pyautogui.click('NoxLogo.PNG')
    go_flag = True
except:
    print("Emulator not on Screen")

if go_flag:

    base_dir_path = "PVP Data/Heroes"    
    all_images = gather.seek_all(base_dir_path)
    count = 0

    for single_image in all_images:
        file_path = os.path.normpath(single_image)
        file_path = file_path.replace("\\", "/")
        #print(file_path)
        try:
            #print(pyautogui.locateOnScreen(currentHDir, confidence=0.6, grayscale=True))
            heroLocation = pyautogui.locateOnScreen(file_path, grayscale=True, confidence=0.9)
            print(single_image.name)
            heroPoint = pyautogui.center(heroLocation)
            pyautogui.moveTo(heroPoint.x, heroPoint.y)
            count = count + 1
        except:
            #print("Item not Found")
            errCount = 1
    
    print("Detected: %(count)01d" % {"count": count})

