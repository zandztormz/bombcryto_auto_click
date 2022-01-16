import pyautogui
import time
pyautogui.FAILSAFE= True

position_green_back_button_x = 0
position_green_back_button_Y = 0

position_select_hero_to_work_x = 0
position_select_hero_to_work_Y = 0

def go_to_work(config):
    print("Go to work")
    
    for pos in pyautogui.locateAllOnScreen('images/'+ config['image'] +'/btn-start.jpg', confidence=0.99):
        time.sleep(5)
        result_find_timeout_button = pyautogui.locateOnScreen('images/'+ config['image'] +'/btn-timeout.jpg', confidence=0.8)
        if result_find_timeout_button is not None: 
            print("Login fail retry ...")
            session_timeout()
            login()
            login_metamask()
        x, y = pyautogui.center(pos)
        pyautogui.click(x, y)

def login_metamask(config):
    print("Signin metamask")
    for result_find_login_metamask_button in pyautogui.locateAllOnScreen('images/'+ config['image'] +'/btn-login-metamask.jpg', confidence=0.99):
        time.sleep(5)
        print("Found login metamask button")
        x, y = pyautogui.center(result_find_login_metamask_button)
        position_login_metamask_button_x = x
        position_metamask_button_Y = y
        print("Save position metamask_button button")
        print(x,y)
        pyautogui.moveTo(x,y)
        pyautogui.doubleClick(x,y)

def login(config, nums):
    time.sleep(5)
    print("Login")
    for pos in nums:
        print("Found login button")
        x, y = pyautogui.center(pos)
        print("Save position login button")
        print(x,y)
        pyautogui.moveTo(x,y)
        pyautogui.doubleClick(x,y)
        print("Click login button")

def session_timeout(config):
    print("Session timeout go to login screen")
    result_find_timeout_button = None
    while result_find_timeout_button is None:
        result_find_timeout_button = pyautogui.locateOnScreen('images/'+ config['image'] +'/btn-timeout.jpg', confidence=0.8)
    x, y = pyautogui.center(result_find_timeout_button)
    position_timeout_button_x = x
    position_timeout_button_y = y
    print("Save position timeout_button")
    print(x,y)
    pyautogui.moveTo(x,y)
    pyautogui.click()
    pyautogui.click()

def close_hero_list(config):
    print("close hero list")
    result_find_close_button = None
    while result_find_close_button is None:
        result_find_close_button = pyautogui.locateOnScreen('images/'+ config['image'] +'/btn-close.jpg', confidence=0.8)
    x, y = pyautogui.center(result_find_close_button)
    print("Save position close_hero_list")
    print(x,y)
    time.sleep(0.5)
    pyautogui.click(x, y)
    time.sleep(1)
    pyautogui.click(x, y)

def select_hero_to_work(config):
    print("select hero to start")
    for pos in pyautogui.locateAllOnScreen('images/'+ config['image'] +'/list-hero.jpg', confidence=0.8):
        x, y =  pyautogui.center(pos)
        print("Found list-hero button", pos)
        print("Save position select_hero_to_work")
        pyautogui.moveTo(x,y)
        pyautogui.click()
        pyautogui.click()
        
def find_back_button(config):
    print("Process find green button back. Please wait...")
    for pos in pyautogui.locateAllOnScreen('images/'+ config['image'] +'/btn-back.jpg', confidence=0.8):
        print("Found green back button")
        x, y = pyautogui.center(pos)
        print("Save position green back button")
        print(x,y)
        pyautogui.moveTo(x,y)
        pyautogui.click()
        pyautogui.click()
           

def click_to_work(config):
    print("Process find work button ...")
    result_click_btn_work = None
    while result_click_btn_work is None:
        result_click_btn_work = pyautogui.locateOnScreen('images/'+ config['image'] +'/btn-work.jpg', confidence=0.8)
    print("Found work button !!")
    x, y = pyautogui.center(result_click_btn_work)
    time.sleep(3)
    pyautogui.click(x, y)
    print("click work button")
