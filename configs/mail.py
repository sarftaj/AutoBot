import smtplib
from extra import mailpresets
import subprocess

#info
print("--------------------------")

#app password for Google
password = "gfnaoaftdbdwmydy"

message1 = input("""what message to send
1: - Entertainment system upgrade script 
2: - Religion template
3: - custom template


     : """)

if message1 == "1":
    message1 = mailpresets.mailscript1
if message1 == "2":
    message1 = mailpresets.mailscript2
if message1 == "3":
    message1 = mailpresets.mailscript3



while True:
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("savvythepig@gmail.com", password)
    s.sendmail("savvythepig@gmail.com", rec, message1)
    print("success")
