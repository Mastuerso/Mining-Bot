import pyautogui
import keyboard
import os

iconW = 106
iconH = 130
xGap = 14
yGap = 18
miniW, miniH = (92, 75)

try:
    noxApp = pyautogui.locateOnScreen('NoxLogo.PNG')
    noxPoint = pyautogui.center(noxApp)
    pyautogui.click(noxPoint.x, noxPoint.y)
    xo = noxApp.left + 1284 - 586
    yo = noxApp.top + noxApp.height + 198
    xi, yi = (xo, yo)
    borderSide, borderTop  = (7, 21)       
    index = 0
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

            index = index + 1
            fileName = '%(index)03d.png' % {"index": index}
            print(fileName)
            #Ask for names to sort and ignore
            if x == 1:
                borderSide = 6
            else:
                borderSide = 7
            imgX = xi + borderSide
            imgY = yi + borderTop
            pyautogui.screenshot(fileName, region=(imgX, imgY, miniW, miniH))
except:
    print('nothing found')