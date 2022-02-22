#An automated script to send birthday mails

import datetime as dt
import pandas as pd
import smtplib
import random

bd = pd.read_csv("Automated_birthday_wisher/birthdays.csv")
bd_dict = bd.to_dict(orient="records")
bd_list = bd_dict[0]

my_email = "your mail"
password = "your password"


def happy_birthday():
    with open(f"Automated_birthday_wisher/letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
        letter_to_send = letter.read()

    now = dt.datetime.now()
    for i in bd_dict:
        if now.day == bd_list["day"] and now.month == bd_list["month"]:
            name = bd_list["name"]
            email = bd_list["email"]
            new_format = letter_to_send.replace("[NAME]", name)
            print(new_format)
            with smtplib.SMTP("smtp.gmail.com") as new_connection:
                new_connection.starttls()
                new_connection.login(user=my_email, password=password)
                new_connection.sendmail(from_addr=my_email, to_addrs=email,
                                        msg=f"Subject: It's your birthday! \n\n {new_format}")


happy_birthday()
