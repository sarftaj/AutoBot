import subprocess
import popen
import sys
c = input("Which website would you like to use: (ENTER NUMBER FOR SELECTION) "
           "\n 1.Prolific "
           "\n 2.Youtube Auto Farmer "
           "\n 3.Mail Spammer "
           "\n 4.Swagbucks"
           "\n PUT NUMBER HERE: ")
print("---------------------------------------------------------------------")





if c == "1":
    print("Welcome to Prolific!")
    subprocess.run(["python", "D:\Auto\configs\prolific.py"])
if c == "2":
    print("Welcome to Youtube!")
    subprocess.run(["python", "D:\Auto\configs\config1-youtube.py"])
if c == "3":
    print("Welcome to the mail spammer")
    subprocess.run(["python", "D:\Auto\configs\mail.py"])
if c == "4":
    print("Welcome to swagbucks script")
    print("---------------------------------------------------------------------")
    subprocess.run(["python", "D:\Auto\configs\swagbucks_script.py"])

