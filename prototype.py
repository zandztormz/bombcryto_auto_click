import pyautogui
import configparser
config = configparser.ConfigParser()
config.read('bomb.conf')
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
is_login = True
# screens = list(pyautogui.locateAllOnScreen('images/'+ config['default']['image'] +'/screen/login.png', confidence=0.99))
# screens = list(pyautogui.locateAllOnScreen('images/'+ config['default']['image'] +'/screen/screen.png', confidence=0.99))
# if len(screens) == 1:
#     print('Found login screen')
#     is_login = True

# screens = list(pyautogui.locateAllOnScreen('images/'+ config['default']['image'] +'/btn-back.jpg', confidence=0.85))
screens = list(pyautogui.locateAllOnScreen('images/'+ config['default']['image'] +'/screen/screen.png', confidence=0.99))
print(screens)
while j < 999:
    i = 0
    while i < len(screens):
        m = screens[i]
        screen_x, screen_y, width, height = m
        width = width + 485
        height = height + 309
        find_if_login = pyautogui.locateOnScreen('images/'+ config['default']['image'] +'/btn-login.png', region=(screen_x, screen_y, width, height ))
        if find_if_login is not None:
            login(i, (screen_x, screen_y, width, height ))
            login_metamask(i, (screen_x, screen_y, width, height ))
            go_to_work(i, (screen_x, screen_y, width, height ))

        # print('\33[33mfinding login button on screen '+ str(i) +'\33[0m')
        # find_if_login = pyautogui.locateOnScreen('images/'+ config['default']['image'] +'/btn-login.png', region=(screen_x, screen_y, width, height ))
        # if find_if_login is not None:
        #     login(i, (screen_x, screen_y, width, height ))
        #     login_metamask(i, (screen_x, screen_y, width, height ))
        #     go_to_work(i, (screen_x, screen_y, width, height ))

        result_find_timeout_button = pyautogui.locateOnScreen('images/'+ config['default']['image'] +'/btn-timeout.png', confidence=0.8, region=(screen_x, screen_y, width, height ))
        if result_find_timeout_button is not None:
            session_timeout(i, (screen_x, screen_y, width, height ))
            login(i, (screen_x, screen_y, width, height ))
            login_metamask(i, (screen_x, screen_y, width, height ))
            go_to_work(i, (screen_x, screen_y, width, height ))

        find_back_button(i, (screen_x, screen_y, width, height ))
        # select_hero_to_work(i, (screen_x, screen_y, width, height ))
        # click_to_work(i, (screen_x, screen_y, width, height ))
        # close_hero_list(i, (screen_x, screen_y, width, height ))
        go_to_work(i, (screen_x, screen_y, width, height ))
        i +=1

    print("Program ready running re process in (Min)",cycle_time)
    now = datetime.datetime.now()
    print ("Start loop at ", now.strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(60*cycle_time)
