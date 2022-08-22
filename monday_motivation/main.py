# ---------------------------- send an email ------------------------------- #
# import smtplib
#
# my_email = "cshinepython@gmail.com"
#
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
#
# connection.login(my_email, "Castlebar0205")
#
# connection.sendmail(my_email, "karissavb@gmail.com", msg="subject:Hello\n\n this is an email")

# ---------------------------- If day, send random quote ------------------------------- #

import datetime
import smtplib
import random

with open("quotes.txt", "r") as file:
    quote_list = file.readlines()

now = datetime.datetime.now()

if now.weekday() == 0:
    my_email = "email@gmail.com"

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()

    connection.login(my_email, "Password")

    connection.sendmail(my_email, "email@gmail.com", msg=f"subject:Monday Motivation\n\n {random.choice(quote_list)}")
