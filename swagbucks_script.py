import selenium
import cons
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
import time
import os

USER = 'savvythepig@gmail.com'
PASS = 'TacoBell12'




ser = Service(r"D:\chromedriver.exe")
op = webdriver.ChromeOptions ()
driver = webdriver.Chrome(service=ser, options=op)


driver.get("https://www.swagbucks.com/p/login")




#sign in script
sign1 = driver.find_element(by="xpath", value='//*[@id="sbxJxRegEmail"]')
sign1.send_keys(USER)
sign2 = driver.find_element(by="xpath", value='//*[@id="sbxJxRegPswd"]')
sign2.send_keys(PASS)
sign3 = driver.find_element(by="xpath", value='//*[@id="loginBtn"]').click()

print("Signing in...")







time.sleep(100)