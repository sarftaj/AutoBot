import selenium
import cons
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
import time
import os

ser = Service(r"D:\chromedriver.exe")
op = webdriver.ChromeOptions ()
driver = webdriver.Chrome(service=ser, options=op)


driver.get("")