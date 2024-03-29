from ast import Return
from operator import truediv
import smtplib
import mailsend
from datetime import datetime
from currency_converter import CurrencyConverter
from forex_python.converter import CurrencyRates  #older method
#mailsend.send_email()
import renderer

x = 4
last_price = 0
last_time = 0
last_date = 0
final_change = 0

while True:
    now = datetime.now()
    b = str(now.strftime("%H:%M:%S"))
    if b == '07:30:10':
    #if int(input()) == 1:
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        current_date = datetime.today().strftime('%Y-%m-%d')
        #latest = str(round(CurrencyRates().get_rate('GBP', 'AUD'), 3))
        #latest_1 = round(CurrencyRates().get_rate('GBP', 'AUD'), 3)
        c = CurrencyRates()
        latest = str(str(round(c.convert('GBP', 'AUD', 100), 2)))
        latest_1 = 1
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

        renderer.render_html(str(current_time), latest)
        mailsend.send_email("samiturk8@gmail.com", "Sami Turk", current_time, latest, final_change, last_date, last_time)
        print("sent")

        #try:
        #    subject = f'Price as of {str(current_time)}' 
        #    body = f"1 GBP buys: {str(latest)} AUD as of {str(current_time)}\nThis is a {final_change}% difference compared to the price on {str(last_date)} at {str(last_time)}"
        #except: 
        #    subject = f'Price as of {str(current_time)}' 
        #    body = f"1 GBP buys: {str(latest)} AUD as of {str(current_time)}"

        #msg = f'Subject: {subject}\n\n{body}'

        last_price = latest
        last_time = current_time
        last_date = current_date

