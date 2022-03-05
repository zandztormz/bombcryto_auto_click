import pyautogui
pyautogui.FAILSAFE= True
import configparser
import time
config = configparser.ConfigParser()
config.read('bomb.conf')
data_conf = config
timeout_config = 3
position_green_back_button_x = 0
position_green_back_button_Y = 0

position_select_hero_to_work_x = 0
position_select_hero_to_work_Y = 0

def go_to_work(index, pos):
    print('\33[33mfinding start button on screen '+ str(index) +'\33[0m')
    timeout = time.time() + timeout_config
    btn_start = None
    while btn_start is None:
        # if time.time() > timeout:
        #     break
        # done = time.time()
        # elapsed = done - start
        # if elapsed > 7:
        #     refresh_button = pyautogui.locateOnScreen('images/'+ config['default']['image'] +'/refresh.png', confidence=0.8, region=(screen_x, screen_y - 130, width, height))
        #     x, y = pyautogui.center(refresh_button)
        #     pyautogui.click(x,y)
        #     login(index, pos)
        #     login_metamask(index, pos)
        #     elapsed = 0
        #     done = None
        #     print(elapsed)
        result_find_timeout_button = pyautogui.locateOnScreen('images/'+ config['default']['image'] +'/btn-timeout.png', confidence=0.8, region=pos)
        if result_find_timeout_button is not None:
            print("Login fail retrying")
            session_timeout(index, pos)
            login(index, pos)
            login_by_metamask(index, pos)
            login_metamask(index, pos)
        btn_start = pyautogui.locateOnScreen('images/'+ config['default']['image'] +'/btn-start.jpg', region=pos, confidence=0.8)
    if btn_start is not None:
        x, y = pyautogui.center(btn_start)
        print('\33[32mfound start button on screen '+ str(index) +' x='+ str(x) +' y='+ str(y) +'\33[0m')
        pyautogui.click(x,y)
        print('click start button on screen '+ str(index) +'')

def login_metamask(index, pos):
    print('\33[33mfinding metamask button on screen '+ str(index) +'\33[0m')
    screen_x, screen_y, width, height = pos
    btn_metamask = None
    while btn_metamask is None:
        btn_metamask = pyautogui.locateOnScreen('images/'+ config['default']['image'] +'/btn-login-metamask.jpg', region=(screen_x, screen_y, width, height + 250), confidence=0.99)
    x, y = pyautogui.center(btn_metamask)
    print('\33[32mfound metamask button on screen '+ str(index) +' x='+ str(x) +' y='+ str(y) +'\33[0m')
    pyautogui.click(x,y)
    print('click signin metamask on screen '+ str(index) +'')

def login(index, pos):
    find_if_login = None
    while find_if_login is None:
        find_if_login = pyautogui.locateOnScreen('images/'+ config['default']['image'] +'/btn-login.png', region=pos)
    x, y = pyautogui.center(find_if_login)
    print('\33[32mfound login button on screen '+ str(index) +' x='+ str(x) +' y='+ str(y) +'\33[0m')
    pyautogui.click(x,y,clicks=2, interval=0.25)
    print('click login screen '+ str(index) +'')

def login_by_metamask(index, pos):
    btn_connect_metamask = None
    while btn_connect_metamask is None:
        btn_connect_metamask = pyautogui.locateOnScreen('images/'+ config['default']['image'] +'/connect-metamask.png', region=pos,confidence=0.8)
    x, y = pyautogui.center(btn_connect_metamask)
    print('\33[32mfound btn_connect_metamask button on screen '+ str(index) +' x='+ str(x) +' y='+ str(y) +'\33[0m')
    pyautogui.click(x,y)
    print('click btn_connect_metamask screen '+ str(index) +'')

def session_timeout(index, pos):
    find_btn_timeout = None
    while find_btn_timeout is None:
        find_btn_timeout = pyautogui.locateOnScreen('images/'+ config['default']['image'] +'/btn-timeout.png', region=pos, confidence=0.8)
    x, y = pyautogui.center(find_btn_timeout)
    print('\33[32msession timeout '+ str(index) +' x='+ str(x) +' y='+ str(y) +'\33[0m')
    pyautogui.click(x,y,clicks=2, interval=0.25)
    print('click session timeout '+ str(index) +'')

def close_hero_list(index, pos):
    print('\33[33mfinding close hero button on screen '+ str(index) +'\33[0m')
    result_find_close_button = None
    while result_find_close_button is None:
        result_find_close_button = pyautogui.locateOnScreen('images/'+ config['default']['image'] +'/btn-close.png', region=pos, confidence=0.83)
    x, y = pyautogui.center(result_find_close_button)
    print('\33[32mfound close hero button on screen '+ str(index) +' x='+ str(x) +' y='+ str(y) +'\33[0m')
    pyautogui.click(x,y)
    print('click close hero button on screen '+ str(index) +'')

def select_hero_to_work(index, pos):
    print('\33[33mfinding list hero on screen '+ str(index) +'\33[0m')
    btn_list_hero = None
    while btn_list_hero is None:
        btn_list_hero = pyautogui.locateOnScreen('images/'+ config['default']['image'] +'/list-hero.jpg', region=pos, confidence=0.7)
    x, y = pyautogui.center(btn_list_hero)
    print('\33[32mfound list hero on screen '+ str(index) +' x='+ str(x) +' y='+ str(y) +'\33[0m')
    pyautogui.click(x,y)
    print('click green list hero screen '+ str(index) +'')
        
def find_back_button(index, pos):
    print('\33[33mfinding green back button on screen '+ str(index) +'\33[0m')
    btn_back = None
    while btn_back is None:
        btn_back = pyautogui.locateOnScreen('images/'+ config['default']['image'] +'/btn-back.jpg', region=pos, confidence=0.8)
    x, y = pyautogui.center(btn_back)
    print('\33[32mfound green back button on screen '+ str(index) +' x='+ str(x) +' y='+ str(y) +'\33[0m')
    pyautogui.click(x,y,clicks=2, interval=0.25)
    print('click green back button on screen '+ str(index) +'')
           

def click_to_work(index, pos):
    print('\33[33mfinding work button on screen '+ str(index) +'\33[0m')
    time.sleep(2)
    result_click_btn_work = None
    while result_click_btn_work is None:
    # time.sleep(3)
        result_click_btn_work = pyautogui.locateOnScreen('images/'+ config['default']['image'] +'/btn-work.png', region=pos)
    # if result_click_btn_work is not None:
    x, y = pyautogui.center(result_click_btn_work)
    print('\33[32mfound work button on screen '+ str(index) +' x='+ str(x) +' y='+ str(y) +'\33[0m')
    pyautogui.doubleClick(x,y)
    print('click work button on screen '+ str(index) +'')
