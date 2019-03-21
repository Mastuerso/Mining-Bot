import pyautogui
import os
import sys
from PIL import ImageChops
import math
import numpy as np

def images(anchor, save = False):
    try:
        anchorBox = pyautogui.locateOnScreen(anchor)
    except:
        anchorBox = False
    
    imgList = []
    region_list = []
    if anchorBox:
        #print(anchorBox)
        mouse_orogin = pyautogui.position()
        pyautogui.click(anchor)
        pyautogui.moveTo(mouse_orogin)
        xo = anchorBox.left + 1284 - 586
        yo = anchorBox.top + anchorBox.height + 198
        xi, yi = (xo, yo)
        borderSide, borderTop  = (7, 21)  
        iconW = 106
        iconH = 130
        xGap = 14
        yGap = 18
        miniW, miniH = (92, 75)
        count = 0             
        for y in range (0, 2):
            if y == 1:            
                yi = yi + iconH + yGap   
                iconH = 129
                borderTop = 20
            for x in range(0, 4):
                if x > 0:
                    xi = xi + iconW + xGap
                else:
                    xi = xo

                if x == 1 or x == 2:
                    iconW = 105
                else:
                    iconW = 106
                if x == 1:
                    borderSide = 6
                else:
                    borderSide = 7
                imgX = xi + borderSide
                imgY = yi + borderTop
                imgList.append(pyautogui.screenshot(region=(imgX, imgY, miniW, miniH)))
                img_region = (imgX, imgY, miniW, miniH)
                region_list.append(img_region)
                if save:                    
                    file_name =  "%(count)03d.png" % {"count": count}
                    print(file_name)
                    imgList[count].save(file_name)
                    count = count + 1
    else:
        print("anchor image not found")
    
    return imgList, region_list

def list_items(directory, *arguments):
    result_list = []
    if os.path.exists(directory):
        verbose = False
        list_dirs = True
        list_files = False
        dir_list = []
        file_list = []
        #print(len(arguments))
        if len(arguments) > 0:
            for arg in arguments:
                if arg == 'v' or arg == 'verbose':
                    verbose = True
                    #print("verbose")
                if arg == 'd' or arg == 'dirs':
                    list_dirs = True
                    #print("Listing Dirs")                    
                if arg == 'f' or arg == 'files':
                    list_files = True
                    list_dirs = False
                    #print("Listing Files")
        
        with os.scandir(directory) as items:
            for item in items:
                if not item.name.startswith('.'):                    
                    if os.path.isdir(item):
                        dir_list.append(item)
                        if verbose:
                            print(item)
                    elif os.path.isfile(item) and list_files:                        
                        file_list.append(item)
                        if verbose:
                            print(item)
        if list_dirs:
            result_list = dir_list
        elif list_files:
            result_list = file_list
    else:
        print("Invalid directory")
    return result_list

def seek_all(directory, file_extension = "png"):
    raw_results = list_items(directory)
    decompress_res = []
    for single_raw_res in raw_results:
        #print (single_raw_res.name)
        compress_res = list_items(single_raw_res, "f")
        if len(compress_res) > 0:
            for single_decompress in compress_res:
                #print(single_decompress)
                decompress_res.append(single_decompress)
    return decompress_res

def rmsdiff(im1, im2):
    """Calculates the root mean square error (RSME) between two images"""
    errors = np.asarray(ImageChops.difference(im1, im2)) / 255
    return math.sqrt(np.mean(np.square(errors)))
    

                
