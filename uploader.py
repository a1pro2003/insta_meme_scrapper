from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from time import sleep
import pyperclip
import pyautogui
import os
import sys
import shutil

def insta_post(post_dir):
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://www.instagram.com")
    window_before = driver.window_handles[0]
    driver.switch_to_window(window_before)
    print(driver.title)
    sleep(7)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
    sleep(5)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys("broisjokes.v2")
    sleep(5)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys("Poptropica24")
    sleep(5)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]').click()
    sleep(5)
    driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button').click()
    sleep(5)
    driver.find_element_by_xpath('/html/body/div[8]/div/div/div/div[2]/div[2]/div[2]/div/button').click()
    sleep(5)
    # pyautogui.keyDown('alt')
    # sleep(.2)
    # pyautogui.press('tab')
    # sleep(.2)
    # pyautogui.keyUp('alt')
    # sleep(2)
    select_post(post_dir)

    sleep(5)
    driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/div[2]/div[2]/button').click()
    sleep(5)
    driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/div[2]/div[2]/button').click()
    sleep(5)
    driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/textarea').click()

    caption = str()
    with open(os.path.abspath(post_dir + "/" + "caption.txt"), "r") as f:
        lines = f.readlines()
        for line in lines:
            caption += line
    workaround_write(caption)

    sleep(3)
    driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/div[2]/div[2]/button').click()
    sleep(10)
    driver.quit()
    print(post_dir)
    print("Trying to remove")
    shutil.rmtree(post_dir)
    print("hopefully removed")


def select_post(post_dir):
    #counts amount of posts and adds name to list
    num_of_post = int()
    name_of_posts = []
    for fname in os.listdir(post_dir):
        if fname.endswith(".txt"):
            pass
        else:
            num_of_post += 1
            name_of_posts.append(fname)

    for i in range(num_of_post):
        pyautogui.typewrite("\"{}\"".format(os.path.abspath(post_dir + "/" + name_of_posts[i])))#file name
        sleep(1)

    pyautogui.press("enter")



def workaround_write(text):
    """
    This is a work-around for the bug in pyautogui.write() with non-QWERTY keyboards
    It copies the text to clipboard and pastes it, instead of typing it.
    """
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    pyperclip.copy('')






