"""This program pairs people randomly for Secret Santa 
and sends them an email with the person they have to get a preset for."""

import numpy as np
import datetime
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.header import Header

dt = datetime.datetime.now()
date = dt.strftime("%Y-%m-%d at %I:%M%p")

friends = {"Friend 1": "friend1@mail.com", "Friend 2": "friend2@mail.com"}


def notify_secret_santa():
    givers_email = list(friends.values())

    givers = list(
        np.random.choice(list(friends.keys()), len(list(friends.keys())), replace=False)
    )

    receivers = []
    for i in range(-1, len(givers) - 1):
        receivers.append(givers[i])

    secret_santa_df = pd.DataFrame(
        {"givers_email": givers_email, "givers": givers, "receivers": receivers}
    )
    secret_santa_df

    my_email = input("Enter your email: ")
    my_pw = input("Enter you password: ")
    subject = "Secret Santa Pairs"

    smtp_host = "smtp.gmx.com"  # smtp.gmail.com / smtp.yahoo.com / smtp.live.com

    s = smtplib.SMTP(smtp_host, 587, timeout=10)  # or port 465
    # s.set_debuglevel(1)

    for i in range(len(secret_santa_df)):
        s.starttls()
        s.login(my_email, my_pw)

        body = str("Hi, " + givers[i] + "!\n\nYou get a present for " + receivers[i])
        msg = MIMEText(body, "plain", "utf-8")
        msg["subject"] = Header(subject, "utf-8")
        msg["From"] = my_email
        msg["To"] = givers_email[i]

        s.sendmail(msg["From"], msg["To"], msg.as_string())
        print("Email sent!")
        s.quit()


if __name__ == "__main__":
    notify_secret_santa()