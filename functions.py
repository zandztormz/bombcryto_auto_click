import pyautogui
import time
from pynput.mouse import Button, Controller
mouse = Controller()
pyautogui.FAILSAFE= True

position_green_back_button_x = 0
position_green_back_button_Y = 0

position_select_hero_to_work_x = 0
position_select_hero_to_work_Y = 0

def go_to_work():
    print("Go to work")
    result_click_btn_work2 = None
    while result_click_btn_work2 is None:
        result_find_timeout_button = pyautogui.locateOnScreen('images/btn-timeout.jpg', confidence=0.8)
        if result_find_timeout_button is not None: 
            print("Login fail retry ...")
            session_timeout()
            login()
            login_metamask()
        result_click_btn_work2 = pyautogui.locateOnScreen('images/btn-start.jpg', confidence=0.8)
    if result_click_btn_work2 is not None:
        x, y = pyautogui.center(result_click_btn_work2)
        pyautogui.click(x, y)

def login_metamask():
    print("Signin metamask")
    result_find_login_metamask_button = None
    while result_find_login_metamask_button is None:
        result_find_login_metamask_button = pyautogui.locateOnScreen('images/btn-login-metamask.jpg', confidence=0.8)
    print("Found login metamask button")
    x, y = pyautogui.center(result_find_login_metamask_button)
    position_login_metamask_button_x = x
    position_metamask_button_Y = y
    print("Save position metamask_button button")
    print(x,y)
    pyautogui.moveTo(x,y)
    pyautogui.click()

def login():
    print("Login")
    result_find_login_button = None
    while result_find_login_button is None:
        result_find_login_button = pyautogui.locateOnScreen('images/btn-login.jpg', confidence=0.8)
    print("Found login button")
    x, y = pyautogui.center(result_find_login_button)
    position_login_button_x = x
    position_login_button_Y = y
    print("Save position login button")
    print(x,y)
    pyautogui.moveTo(x,y)
    pyautogui.click()
    pyautogui.click()
    print("Click login button")

def session_timeout():
    print("Session timeout go to login screen")
    result_find_timeout_button = None
    while result_find_timeout_button is None:
        result_find_timeout_button = pyautogui.locateOnScreen('images/btn-timeout.jpg', confidence=0.8)
    x, y = pyautogui.center(result_find_timeout_button)
    position_timeout_button_x = x
    position_timeout_button_y = y
    print("Save position timeout_button")
    print(x,y)
    pyautogui.moveTo(x,y)
    pyautogui.click()
    pyautogui.click()

def close_hero_list():
    print("close hero list")
    result_find_close_button = None
    while result_find_close_button is None:
        result_find_close_button = pyautogui.locateOnScreen('images/btn-close.jpg', confidence=0.8)
    x, y = pyautogui.center(result_find_close_button)
    print("Save position close_hero_list")
    print(x,y)
    time.sleep(0.5)
    pyautogui.click(x, y)
    time.sleep(1)
    pyautogui.click(x, y)

def select_hero_to_work():
    print("select hero to start")
    t = 0
    while t != 2:
        result_find_list_hero = None
        while result_find_list_hero is None:
            time.sleep(1)
            result_find_list_hero = pyautogui.locateOnScreen('images/list-hero.jpg')
            x, y = pyautogui.center(result_find_list_hero)
            position_select_hero_to_work_x = x
            position_select_hero_to_work_Y = y
            print("Save position select_hero_to_work")
            print(x,y)
            print(position_select_hero_to_work_x,position_select_hero_to_work_Y)
            pyautogui.moveTo(position_select_hero_to_work_x,position_select_hero_to_work_Y)
            pyautogui.click()
            pyautogui.click()
            t += 1
    
   
def find_back_button():
    print("Process find green button back. Please wait...")
    i = 0
    while i != 2:
        result_find_back_button = None
        while result_find_back_button is None:
            result_find_back_button = pyautogui.locateOnScreen('images/btn-back.jpg', confidence=0.8)
            print("Found green back button")
            x, y = pyautogui.center(result_find_back_button)
            position_green_back_button_x = x
            position_green_back_button_Y = y
            print("Save position green back button")
            print(x,y)
            pyautogui.moveTo(position_green_back_button_x,position_green_back_button_Y)
            pyautogui.click()
            pyautogui.click()
            i += 1

def click_to_work():
    print("Process find work button ...")
    result_click_btn_work = None
    while result_click_btn_work is None:
        result_click_btn_work = pyautogui.locateOnScreen('images/btn-work.jpg', confidence=0.8)
    print("Found work button !!")
    x, y = pyautogui.center(result_click_btn_work)
    time.sleep(3)
    pyautogui.click(x, y)
    print("click work button")
