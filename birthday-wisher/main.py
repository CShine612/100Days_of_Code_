##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime
import smtplib
import random
import pandas

to_send = {}

with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as file:
    letter = file.read()

now = datetime.datetime.now()

birthdays = pandas.read_csv("birthdays.csv")



for row in birthdays.iterrows():
    row = row[1]
    if now.month == row.month and now.day == row.day:
        to_send[row.friend_name] = row.email

if len(to_send) > 0:
    for name in to_send.keys():
        message = letter.replace("[NAME]", str(name))


        my_email = "email@gmail.com"

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()

        connection.login(my_email, "Password")

        connection.sendmail(my_email, to_send[name], msg=f"subject:Happy Birthday\n\n {message}")


