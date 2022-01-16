import pyautogui
import configparser
config = configparser.ConfigParser()
config.read('bomb.conf') #อ่านไฟล์
data_conf = config
import time
import datetime
from functions import go_to_work, login_metamask, login, session_timeout, close_hero_list, select_hero_to_work, find_back_button, click_to_work

j = 0
print(data_conf['default']['image'])
print("Program bot for bormcrypto start")
print("Open browser for program one by one")
print("Keep all hero to rest")
print("After open 'Treasure Hunt' page and wait for end process")
cycle_time = input("Input cycle time (Min.): \n")
cycle_time = int(cycle_time)

while j < 999:
    find_if_login = list(pyautogui.locateAllOnScreen('images/'+ config['default']['image'] +'/btn-login.png', confidence=0.99))
    # find_if_login2 = pyautogui.locateAllOnScreen('images/'+ config['default']['image'] +'/btn-login.png', confidence=0.8)
    # print(find_if_login2)
    # for m in pyautogui.locateAllOnScreen('images/'+ config['default']['image'] +'/btn-login.png', confidence=0.99):
    #     print(m)
    # print(find_if_login)
    if len(find_if_login) > 0:
        print('Found Login Screen')
        login(data_conf['default'], find_if_login)
        login_metamask(data_conf['default'])
        go_to_work(data_conf['default'])
    # for pos in pyautogui.locateAllOnScreen('images/'+ config['default']['image'] +'/btn-login.png', confidence=0.8):
    #     print('Found Login')
    #     login(data_conf['default'], pos)
    #     login_metamask(data_conf['default'])
    #     go_to_work(data_conf['default'])

    # result_find_timeout_button = pyautogui.locateOnScreen('images/'+ config['default']['image'] +'/btn-timeout.jpg', confidence=0.8)
    # if result_find_timeout_button is not None:
    #     session_timeout(data_conf['default'])
    #     login(data_conf['default'])
    #     login_metamask(data_conf['default'])
    #     go_to_work(data_conf['default'])
    
    # find_back_button(data_conf['default'])
    # select_hero_to_work(data_conf['default'])
    # click_to_work(data_conf['default'])
    # close_hero_list(data_conf['default'])
    # go_to_work(data_conf['default'])

    print("Program ready running re process in (Min)",cycle_time)
    now = datetime.datetime.now()
    print ("Start loop at ", now.strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(60*cycle_time)
