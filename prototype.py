import pyautogui
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

while j < 999:
    check_login = pyautogui.locateOnScreen('images/btn-login.jpg', confidence=0.8)
    if check_login is not None:
        login()
        login_metamask()
        go_to_work()

    result_find_timeout_button = pyautogui.locateOnScreen('images/btn-timeout.jpg', confidence=0.8)
    if result_find_timeout_button is not None:
        session_timeout()
        login()
        login_metamask()
        go_to_work()
    
    find_back_button()
    select_hero_to_work()
    click_to_work()
    close_hero_list()
    go_to_work()

    print("Program ready running re process in (Min)",cycle_time)
    now = datetime.datetime.now()
    print ("Start loop at ", now.strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(60*cycle_time)
