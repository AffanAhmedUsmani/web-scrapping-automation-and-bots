import ctypes
from selenium import webdriver
import easygui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# pip install -r /path/to/requirements.txt
#import pandas as pd
import time
MessageBox = ctypes.windll.user32.MessageBoxW  # MessageBoxA in Python2


#email = "Criaratesda12@yahoo.com"
driver = webdriver.Edge(r'C:\Users\user\Downloads\msedgedriver.exe')

driver.get('https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&ru=https%3A%2F%2Fwww.ebay.com%2Fmys%2Fhome%3Fsource%3DGBH')
x = "y"
while x == "y":

    email = easygui.enterbox("Enter The Email")

    box = driver.find_element_by_xpath('//*[@id="userid"]')
    box.send_keys(email)
    box.send_keys(Keys.ENTER)
    select = driver.find_element_by_xpath('//*[@id="signin-continue-btn"]')
    action = ActionChains(driver)
    action.click(on_element=select)
    action.perform()
    time.sleep(2)

    try:
        select = driver.find_element_by_xpath(
            '//*[@id="need-help-signin-link"]')
        action = ActionChains(driver)
        action.click(on_element=select)
        action.perform()
        time.sleep(2)
        select = driver.find_element_by_xpath('//*[@id="fyp-btn"]')
        action = ActionChains(driver)
        action.click(on_element=select)
        action.perform()

    except:
        driver.refresh()
        MessageBox(None, 'not a valid email entered',
                   'BOT Response to your email', 0)

    def check():
        outstr = ""

        if(driver.find_element_by_xpath("""//*[@id="emailWithCode"]""")):
            outstr = "email available"
        if(driver.find_element_by_xpath("""//*[@id="text"]""")):
            outstr = outstr + " phone option available"
        MessageBox(None, outstr, 'BOT Response to your email', 0)

    check()
    x = easygui.enterbox("Press y to test another x to quit")
