"""This program pairs people randomly for Secret Santa 
and sends them an email with the person they have to get a preset for."""

import numpy as np
import datetime
import pandas as pd
import smtplib

dt = datetime.datetime.now()
date = dt.strftime("%Y-%m-%d at %I:%M%p")


def pair_people():
    friends = {
        "Ahmad": "ahmad@mail.com",
        "Bianca": "bianca@mail.com",
        "Chad": "chad@mail.com",
        "Damian": "damian@mail.com",
        "Ellen": "ellen@mail.com",
        "Franz": "franz@mail.com",
    }

    givers = list(
        np.random.choice(list(friends.keys()), len(list(friends.keys())), replace=False)
    )
    receivers = []
    for i in range(-1, len(givers) - 1):
        receivers.append(givers[i])
    print(givers, receivers)

    secret_santa_df = pd.DataFrame({"givers": givers, "receivers": receivers})
    secret_santa_df.to_csv("secret_givers_list.csv", index=False)


def send_email():
    smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    eml = input("Enter your email: ")
    pwd = input("Enter your password: ")
    smtpObj.login(eml, pwd)

    for i in range(len(friends)):
        smtpObj.sendmail(
            eml,
            friends[givers[i]],
            "Subject: Secret Santa Pairs \
        \nHello %s! \
        \n\nThis year you are getting a present for %s! \
        \n\nEmail sent on %s."
            % (givers[i], receivers[i], date),
        )

    smtpObj.quit()


if __name__ == "__main__":
    pair_people()
    send_email()
