import smtplib

def send_email(sender, msg, to):

    smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
    smtpObj.starttls()
    smtpObj.login(sender, "oksana-8182")
    smtpObj.sendmail(sender, to, msg)
    smtpObj.quit()

msg = "Hello from Python! I did it!"
send_email("test.oksana.0@gmail.com", msg, "el.piankova@gmail.com")

# smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
# smtpObj.starttls()
#
# smtpObj.login("test.oksana.0@gmail.com", "oksana-8182")
#
# smtpObj.sendmail("test.oksana.0@gmail.com", "alexxeykov@gmail.com", "from python")
#
# smtpObj.quit()
