import subprocess

import selenium
from selenium.webdriver import ActionChains

import cons
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
import time
import os
from configs import prolificinfo



if os.name == 'posix':  # Unix/Linux/MacOS
    os.system('clear')

#to use auto sign in make another .py named prolificinfo.py then put website1_user and pass in there









#setup with user files
ser = Service(r"D:\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)


#website url
driver.get("https://internal-api.prolific.co/auth/accounts/login/")


#user driver
user = driver.find_element(by="xpath", value='//*[@id="id_username"]')
user.click()

#user sign in - username
user.send_keys(prolificinfo.website1_user)
password = driver.find_element(by="xpath", value='//*[@id="loginForm"]/div[3]/div/div/input')
password.click()

#user sign in - password
password.send_keys(prolificinfo.website1_pass)

#click login
click1 = driver.find_element(by="xpath", value='//*[@id="login"]')
click1.click()


print("Logged In, process will start soon...")
print("---------------------------------------------------------------------")

driver.implicitly_wait(5)
click1 = driver.find_element(by="xpath", value='//*[@id="klaro"]/div/div/div[2]/div/div/div/button[2]')
click1.click()


wait = input("enter any key when the page opens : ")
os.system('cls')


lookforsurvey = driver.find_element("xpath", value='//*[@id="app"]/div[2]/div/div/div/div/div/div')
if lookforsurvey:
    print("no surveys at this moment please wait a little...: ")
    print("closing program....................................")


#main 1


def get_score(title):
    """Computes a score for a survey title."""
    # In this example, the score is based on the length of the title
    return len(title)




# Find the best $
html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')
highest_elem = None
highest_score = float('-inf')







for study_elem in soup.find('div', class_="tags"):
    title = study_elem.text.strip()
    score = get_score(title)  # define a function to compute the score for a survey title
    if score > highest_score:
        highest_elem = study_elem
        highest_score = score
        print(highest_elem.text, "highest paying survey")
        print("---------------------------------------------------------------------")
        os.system('cls')



        #starting survey (need to test)
        botinput = input("Do script for this survey [1] yes [2] no: ")
        driver.find_element ("xpath",
                             value='//*[@id="app"]/div[2]/div/div/div/div/div[2]/div[1]/div[3]/button').click()
        time.sleep(5)
        #start survey from menu
        driver.find_element("xpath",
                             value='//*[@id="app"]/div[2]/div/div/div/section[2]/div/div[3]/div/form/button').click()
        time.sleep(5)
        driver.find_element("xpath", value='/html/body/div[5]/div[2]/section/div/label/span/input').click()



"""change to prolificbot
if botinput == "1":
    action = ActionChains(driver)
    action.click(on_element=highest_elem)
    action.perform()
    click2 = driver.find_element("xpath", value='//*[@id="app"]/div[2]/div/div/div/div/div[2]/div[1]/div[3]/button')
"""

time.sleep(50)
































#check balance for prolific
balance = int(input("Do you want to check your balance?: {1} - Yes {2} - No?: "))
# balance input 1
if balance == 1:
    bal1 = driver.find_element (by="xpath", value='//*[@id="app"]/div[2]/nav/div[2]/div[2]/div/a')
    bal1.click()
    bal2 = driver.find_element (by="xpath",
                                value='//*[@id="app"]/div[2]/nav/div[2]/div[2]/div/div/div[2]/section[1]/span/button')
    bal2.click()
    bal3 = driver.find_element (by="xpath",
                                value='/html/body/div[6]/div[2]/section/div/div/form/table/tr[1]/td[2]/span')
    bal4 = driver.find_element (by="xpath",
                                value='//*[@id="app"]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div/span')
    # bal5 = driver.find_element(by="xpath", value='/html/body/div[5]/div[2]/section/header/button/svg/path')
    print ("Live Amount: ", bal3.text)
    print ("_____________")
    print ("Live Surveys Now: ", bal4.text)

# balance input 2
if balance == 2:
    bal4 = driver.find_element (by="xpath",
                                value='//*[@id="app"]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div/span')
    print ("Live Surveys Now: ", bal4.text)
    print ("_____________")
    print ("Time to farm!")

# Script for quitting after process

quit1 = int(input("Are you done?: [Yes] 1 [No] 2: "))
if quit1 == 1:
    print("quitting... come back soon!")
    driver.quit()










time.sleep(100)
driver.quit()
