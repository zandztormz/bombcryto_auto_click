import pyautogui
import configparser
config = configparser.ConfigParser()
config.read('bomb.conf') #อ่านไฟล์
data_conf = config
import time
import datetime
from functions import go_to_work, login_metamask, login, session_timeout, close_hero_list, select_hero_to_work, find_back_button, click_to_work

j = 0

print("Program bot for bormcrypto start")
print("Open browser for program one by one")
print("Keep all hero to rest")
print("After open 'Treasure Hunt' page and wait for end process")
cycle_time = input("Input cycle time (Min.): \n")
cycle_time = int(cycle_time)
screens = list(pyautogui.locateAllOnScreen('images/'+ config['default']['image'] +'/screen/login.png', confidence=0.99))

while j < 999:
    i = 0
    while i < len(screens):
        m = screens[i]
        screen_x, screen_y, width, height = m
        print('found screen '+ str(i) +' at ', screen_x, screen_y, width, height)
        print('\33[33mfinding login button on screen '+ str(i) +'\33[0m')
        find_if_login = pyautogui.locateOnScreen('images/'+ config['default']['image'] +'/btn-login.png', region=m)
        if find_if_login is not None:
            login(config['default'], i, m)
            login_metamask(config['default'], i, m)
            go_to_work(config['default'], i, m)

        result_find_timeout_button = pyautogui.locateOnScreen('images/'+ config['default']['image'] +'/btn-timeout.png', confidence=0.8, region=m)
        if result_find_timeout_button is not None:
            session_timeout(config['default'], i, m)
            login(config['default'], i, m)
            login_metamask(config['default'], i, m)
            go_to_work(config['default'], i, m)

        find_back_button(config['default'], i, m)
        select_hero_to_work(config['default'], i, m)
        click_to_work(config['default'], i, m)
        close_hero_list(config['default'], i, m)
        go_to_work(config['default'], i, m)
        i +=1

    print("Program ready running re process in (Min)",cycle_time)
    now = datetime.datetime.now()
    print ("Start loop at ", now.strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(60*cycle_time)
