import pyautogui
import keyboard
import time
from PIL import Image
import numpy
from miningbot import gather, db_gui

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
"""
index = 0
for y in range (0, 3):
  #print('%(language)s has %(number)03d quote types.' % \
  #  {'language': "Python", "number": 2})
  #print('[%(x)02d, %(y)02d]' % {"x": x, "y": y})
  index = index + 1
  print('[%(index)03d]' % {"index": index})
"""

"""
charName = pyautogui.prompt(text='Name the Heroe', title='Hero\'s name' , default='--')
if charName == '--':
  print('Not a Hero')
else:
  print(charName + ' is a Hero')
"""
"""

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

"""
#im = pyautogui.screenshot()
#im.save("test.png")


dir_list = gather.list_items("PVP Data/Heroes")
db_gui.populate_db(dir_list, "temp.png")