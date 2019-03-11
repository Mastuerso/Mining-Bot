import pyautogui
import time
print("Ready")
time.sleep(5) # 5 Seconds pause
#pyautogui.PAUSE = 1
distance = 200
while distance > 0:   
    pyautogui.dragRel(distance, 0, duration=0)   # move right
    distance -= 5
    pyautogui.dragRel(0, distance, duration=0)   # move down
    pyautogui.dragRel(-distance, 0, duration=0)  # move left
    distance -= 5
    pyautogui.dragRel(0, -distance, duration=0)  # move up
print("Success")