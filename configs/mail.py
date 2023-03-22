import smtplib

#info
print("--------------------------")

#app password for Google
password = "gfnaoaftdbdwmydy"

message1 = input("message to send: ")

rec = input("email to spam: ")




while True:
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("savvythepig@gmail.com", password)
    s.sendmail("savvythepig@gmail.com", rec, message1)
    print("success")
