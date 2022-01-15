import pyautogui

# result_find_back_button = None
# while result_find_back_button is None:
for i in pyautogui.locateAllOnScreen('images/btn-back.jpg', confidence=0.8):
    x, y = pyautogui.center(i)
    print(i)