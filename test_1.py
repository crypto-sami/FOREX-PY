from ast import Return
from operator import truediv
import smtplib
from forex_python.converter import CurrencyRates
import mailsend
from datetime import datetime

latest = str(round(CurrencyRates().get_rate('GBP', 'AUD'), 3))
latest_1 = round(CurrencyRates().get_rate('GBP', 'AUD'), 3)