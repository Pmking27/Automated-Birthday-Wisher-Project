import pandas
import random
import smtplib
import datetime as dt

my_email="Your Email"
my_password="Your Email Password Or If you using Gmail Then App Key"

current_date_time=dt.datetime.now()
current_day=current_date_time.day
current_month=current_date_time.month
data=pandas.read_csv("birthdays.csv")

data_name=data["name"].tolist()
data_day=data["day"].tolist()
data_month=data["month"].tolist()
data_email=data["email"].tolist()

for i in range(len(data_day)):
    if current_day == data_day[i] and current_month == data_month[i]:
        number=random.randint(1,3)
        with open(f"letter_templates/letter_{number}.txt","r") as latter:
            letter_text=latter.read()
        bdp_name=data_name[i]
        bdp_email=data_email[i]
        new_letter_text=letter_text.replace("[NAME]",bdp_name)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=bdp_email,
                msg=f"Subject:Happy Birthday - {bdp_name}\n\n{new_letter_text}"
                )
