import pyautogui
import os

def images(anchor):
    try:
        anchorBox = pyautogui.locateOnScreen(anchor)
    except:
        anchorBox = False
    
    imgList = []
    if anchorBox:
        #print(anchorBox)
        pyautogui.click(anchor)
        xo = anchorBox.left + 1284 - 586
        yo = anchorBox.top + anchorBox.height + 198
        xi, yi = (xo, yo)
        borderSide, borderTop  = (7, 21)  
        iconW = 106
        iconH = 130
        xGap = 14
        yGap = 18
        miniW, miniH = (92, 75)             
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
    else:
        print("Void")
    
    return imgList 

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
                    if os.path.isdir(item) and list_dirs:
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