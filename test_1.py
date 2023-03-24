from ast import Return
from operator import truediv
import smtplib
from forex_python.converter import CurrencyRates
import mailsend
from datetime import datetime
from currency_converter import CurrencyConverter



#c = CurrencyConverter()
#print(c.convert(100, 'EUR', 'USD'))


latest = str(round(CurrencyConverter().convert(100, 'GBP', 'AUD'), 2))
print(latest)

#latest = str(round(CurrencyRates().get_rate('GBP', 'AUD'), 3))
#latest_1 = round(CurrencyRates().get_rate('GBP', 'AUD'), 3)
