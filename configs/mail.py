import smtplib
import os
from extra import mailpresets
import subprocess



os.system('cls')
mailai = input("Would you like to use ai to write your email?: "
               "\n [1] Y"
               "\n [2] N"
               "\n  : ")
if mailai == "1":
    subprocess.run (["python", "D:\Auto\extra\mailai.py"])







#info
print("--------------------------")
rec = input("put receiver email to spam here: ")

#app password for Google
ap1 = input("use saved app password or new {1} yes 2 {2}: ")

if ap1 == "1":
    password = "zkwrayxvlojysbdz"

if ap1 == "2":
    print("for now go to mail.py and change the password = ")



message1 = input("""what message to send
1: - Entertainment system upgrade script 
2: - Religion template
3: - custom template
4:



        : """)
os.system('cls')
if message1 == "1":
    message1 = mailpresets.mailscript1
if message1 == "2":
    message1 = mailpresets.mailscript2
if message1 == "3":
    mailscript3 = input("Put your custom script here. : ")

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