import itertools
import threading
import time
import sys
import smtplib
import os
import subprocess
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from extra import mailpresets

#google app password

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
time.sleep(5)
done = True
print("welcome to ai mail")


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
#op.add_argument("headless")
driver = webdriver.Chrome(service=ser, options=op)

driver.get("ai website")

#make prompt wile screen not showing with prompt asked
















rec = input("rec address: ")

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
        s.sendmail("savvythepig@gmail.com", rec, message1)
        print("success")

if sendquestion == "2":
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("savvythepig@gmail.com", password)
    s.sendmail("savvythepig@gmail.com", rec, message1)
    print("success")

























time.sleep(100)
