import pyautogui
import keyboard
import time

#time.sleep(5) # 5 Seconds pause
#mouseX, mouseY = pyautogui.position()
#print (mouseX, mouseY)

#x, y = (800, 800)
#xOffset, yOffset = (200, 0)
#num_seconds = 0.2
#pyautogui.moveTo(x, y, duration=num_seconds)  # move mouse to XY coordinates over num_second seconds
#pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)  # move mouse relative to its current position
#pyautogui.click()

'''
x, y = (1650, 434)
num_seconds = 0.2
pyautogui.dragTo(x, y, duration=num_seconds)  # drag mouse to XY


xOffset, yOffset = (200, 0)
num_seconds = 0.2
pyautogui.dragRel(xOffset, yOffset, duration=num_seconds)  # drag mouse relative to its current position
'''
secs_between_keys = .1

prologue = """ Prólogo
     La presente Tragedia es una de las mejores de Guillermo Shakespeare, y la que con más
   frecuencia y aplauso público se representa en los teatros de Inglaterra. Las bellezas
   admirables que en ella se advierten y los defectos que manchan y oscurecen sus 
   perfecciones, forman un todo extraordinario y monstruoso compuesto de partes tan 
   diferentes entre sí, por su calidad y su mérito, que difícilmente se hallarán reunidas en otra
   composición dramática de aquel autor ni de aquel teatro; y por consecuencia, ninguna otra
   hubiera sido más a propósito para dar entre nosotros una idea del mérito poético de
   Shakespeare, y del gusto que reina todavía en los espectáculos de aquella nación.
"""

'''

pyautogui.typewrite(prologue, interval=secs_between_keys)  # useful for entering text, newline is Enter
'''
'''
pyautogui.hotkey('alt', 'tab')

pyautogui.keyDown('shift')
#pyautogui.press(['left', 'left', 'left', 'left', 'left'])
pyautogui.press('home')
pyautogui.press('decimal')
pyautogui.keyUp('shift')
pyautogui.alert(text='Hey', title='Henry Danger', button='OK')
'''

"""
pyautogui.hotkey('alt', 'tab')
pyautogui.hotkey('num1', 'subtract', 'num1', 'num1', 'num1', 'num1', 'enter')
#pyautogui.hotkey('alt', 'num1', 'num1', 'num1')
#pyautogui.hotkey('alt', '1')  #☺
keyboard.write(prologue, delay=.1)
"""

#Locate on Screen

try:
  print(pyautogui.locateOnScreen('goldLimit.PNG'))
  #print(pyautogui.locateOnScreen('test.png'))
except:
  print("Item not Found")
