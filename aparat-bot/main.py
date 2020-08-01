from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
import os
import time
import random

username = input('Please enter your user name \n')
password = input('Please enter your password \n')
hashtag = input('Please enter the hashtag you want to follow people from \n')
count = input('Please enter how many time you want to follow people \n')



driver = webdriver.Chrome('chromedriver.exe')


driver.get('https://www.instagram.com/accounts/login/')

time.sleep(5)

enter_username = driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input')
enter_username.send_keys(username)


# 

enter_password = driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input')
enter_password.send_keys(password)

# 
time.sleep(2)
click_login = driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB > button')
click_login.click()

time.sleep(5)

driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))

time.sleep(5)
countint = int(count)
i = 0

while i < countint:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(5)

    post = driver.find_element_by_css_selector('#react-root > section > main > article > div:nth-child(3) > div > div:nth-child(8) > div:nth-child(2) > a > div.eLAPa > div._9AhH0')
    post.click()

    time.sleep(5)
    follow_text = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.bY2yH > button')
    text = follow_text.text

    if text == 'Follow':
        follow = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.bY2yH > button')
        follow.click()
        time.sleep(5)
        exit_post = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button > div > svg')
        exit_post.click()
    else:
        exit_post = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button > div > svg')
        exit_post.click()


    time.sleep(5)

    
    i = i+1

print('Everything is done Propely', count)
driver.close()