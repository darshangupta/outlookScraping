from cgitb import text
import time
#from typing_extensions import Self
#import requests
import regex
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def has_aria_label_and_readonly(tag):
    return tag.has_attr('aria-label') and tag.has_attr('aria-readonly')
#this function sorts through all the html from the page

substrings = ['@', 'aria-label']
browser = webdriver.Chrome()
browser.get("https://outlook.office.com/people/")
textFile = open('yourTextFile.txt', 'a')
textFile.write('\n')
pyautogui.press('')
time.sleep(6)
pyautogui.write('YourEmail@outlook.com')
pyautogui.press('enter')
time.sleep(6)
pyautogui.write('YourPassword')
pyautogui.press('enter')
time.sleep(4)
pyautogui.moveTo(92, 237)
pyautogui.click()
print("three bars clicked")

time.sleep(11)
pyautogui.moveTo(172, 477)
pyautogui.scroll(-20)
pyautogui.moveTo(166, 607)
pyautogui.click(clicks = 1)
print("directory should be open")
time.sleep(5)

#adjust the x and y coordinates as needed for your computer 

pyautogui.moveTo(464,349)
pyautogui.click()

time.sleep(30) #this long wait is to make sure everything loads as it should 


while True: #while true allows for infinite scroll 
    content = browser.page_source
    soup = BeautifulSoup(content)
    pyautogui.click(clicks = 2)
    print(pyautogui.position())
    #print(soup.find_all(has_aria_label_and_readonly))
    input = str(soup.findAll(has_aria_label_and_readonly)).split('data-is-focusable') #splits around 'data-is-focusable' tags
    for i in input:
        result = regex.findall('aria-label="(.*)Not marked as favorite', i) #this scrapes everything between the 'aria-label' and 'Not marked as favorite'
        print(result)
        textFile.write(' '.join(result))
        textFile.write("\n")
        
    time.sleep(2)
    pyautogui.scroll(-3)

    

