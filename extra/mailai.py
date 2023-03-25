import itertools
import threading
import time
import sys
import smtplib
import os
import subprocess

import self as self
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from extra import mailpresets
import tkinter as tk

#google app password
os.system('cls')
password = "zkwrayxvlojysbdz"
print("make sure your app password matches - ", password)




print("---------------------------------------------------------------------")
done = False


# here is the animation
def animate():
    for c in itertools.cycle (['|', '/', '-', '\\']):
        if done:
            break

        sys.stdout.write('\rloading ' + c)

        sys.stdout.flush()
        time.sleep(0.1)

    sys.stdout.write('\r------Loading completed... Process Starting Now!------')


t = threading.Thread(target=animate)
t.start()

# long process here
time.sleep(3)
done = True
print("")
print("---------------------------------------------------------------------")

#paths for google
CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH

ser = Service(r"D:\chromedriver.exe")
op = webdriver.ChromeOptions()
op.add_argument("headless")
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://aiseo.ai/templates/email-generator.html")

#make prompt wile screen not showing with prompt asked

driver0 = driver.find_element("xpath", value='//*[@id="input-title"]').clear()
driver1 = driver.find_element("xpath", value='//*[@id="input-title"]')
q1 = input("Main Topic Prompt:")
driver1.send_keys(q1)
print("---------------------------------------------------------------------")
driver2 = driver.find_element("xpath", value='//*[@id="input-intro"]').clear()
driver3 = driver.find_element("xpath", value='//*[@id="input-intro"]')
q2 = input("main points to cover: ")
driver3.send_keys(q2)
driver4 = driver.find_element("xpath", value='//*[@id="generate_btn"]').click()
time.sleep(15)
driver5 = driver.find_element("xpath", value='//*[@id="generatedCommands"]/div[1]/div[2]/button[1]').click()
root = tk.Tk()
prompt = root.clipboard_get()
print(prompt)


















q3 = input("Would you like to use this prompt: [1] y [2] n")
if q3 == "1":
    rec = input("rec address: ")
if q3 == "2":
    print("add fuction to go back")



sendquestion = input("""
Would you like this to send infinite or only once?
{1} yes
{2} no
""")

if sendquestion == "1":
    while True:
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login("savvythepig@gmail.com", password)
        s.sendmail("savvythepig@gmail.com", rec, prompt)
        print("success")

if sendquestion == "2":
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("savvythepig@gmail.com", password)
    s.sendmail("savvythepig@gmail.com", rec, prompt)
    print("success")

























time.sleep(100)
