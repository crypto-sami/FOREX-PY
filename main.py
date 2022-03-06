from ast import Return
from operator import truediv
import smtplib
from forex_python.converter import CurrencyRates
import time
from datetime import datetime
import schedule
import json

x = 4
last_price = 0
last_time = 0
last_date = 0
final_change = 0


while True:
    now = datetime.now()
    b = str(now.strftime("%H:%M:%S"))
    if b == '06:00:00':
        email_address = "pytestbot223@gmail.com"
        email_password = json.loads(open("C:/sers/samit/Documents/VScode projects/Foreign-Exchange-Notifier/password.json", "r").read())
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        current_date = datetime.today().strftime('%Y-%m-%d')
        latest = str(round(CurrencyRates().get_rate('GBP', 'AUD'), 3))
        latest_1 = round(CurrencyRates().get_rate('GBP', 'AUD'), 3)
        print("1 GBP buys: ", latest, f"AUD as of {current_time}")

        try:
            increase = latest_1 - float(last_price)
            if last_price == 0:
                print(" ")
            else:
                change = increase/float(last_price)
                final_change = change*100
        except:
            print(" ")

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(email_address, email_password)

            try:
                subject = f'Price as of {str(current_time)}' 
                body = f"1 GBP buys: {str(latest)} AUD as of {str(current_time)}\nThis is a {final_change}% difference compared to the price on {str(last_date)} at {str(last_time)}"
            except: 
                subject = f'Price as of {str(current_time)}' 
                body = f"1 GBP buys: {str(latest)} AUD as of {str(current_time)}"

            msg = f'Subject: {subject}\n\n{body}'

            smtp.sendmail(email_address, 'samiturk8@gmail.com', msg)

        last_price = latest
        last_time = current_time
        last_date = current_date

