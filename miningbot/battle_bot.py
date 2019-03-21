import pyautogui
from time import sleep
import os
from miningbot import gather

def filer_list(dir_list, filter_list):
    filtered_data = []
    for single_filter in filter_list:
        for single_dir in dir_list:        
            if single_dir.name == single_filter:
                filtered_data.append(single_dir)
    return filtered_data
            


def ban():
    #This two could not be hardcoded but Idk 
    # kinda seems unnecessary atm
    max_bans =  2
    base_dir_path = "PVP Data/Heroes"
    dir_list = gather.list_items(base_dir_path)

    ban_list = []
    with open("ban.list") as f: 
        for line in f:
            ban_list.append(line.rstrip())  

    focus_dirs = filer_list(dir_list, ban_list)    
    for single_dir in focus_dirs:                        
        this_dir_imgs = gather.list_items(single_dir, 'f')        
        if max_bans > 0 and len(this_dir_imgs) > 0:
            print("Banning " + single_dir.name)
            for dir_img in this_dir_imgs:
                #print(dir_img)
                file_path = os.path.normpath(dir_img)
                file_path = file_path.replace("\\", "/")
                #print(file_path)
                try:                    
                    heroLocation = pyautogui.locateOnScreen(file_path, grayscale=True, confidence=0.9)
                    #print(single_image.name)
                    heroPoint = pyautogui.center(heroLocation)
                    pyautogui.moveTo(heroPoint.x, heroPoint.y)
                    pyautogui.click()
                    max_bans = max_bans - 1
                    break
                except:
                    print("...")

def play_pvp():
    print("This is me playing XD")

