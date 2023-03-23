from forex_python.converter import CurrencyRates
import mailtrap as mt

# create mail object
mail = mt.Mail(
    sender=mt.Address(email="sami@sturk.au", name="Sami Turk"),
    to=[mt.Address(email="samiturk8@gmail.com")],
    subject="You are awesome!",
    text="Congrats for sending test email with Mailtrap!",
)

# create client and send
client = mt.MailtrapClient(token="b5e81e553baf2094b3f0f5588b831b3f")
client.send(mail)