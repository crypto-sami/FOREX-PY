import mailtrap as mt

# create mail object
mail = mt.Mail(
    sender=mt.Address(email="forex@sturk.au", name="Foreign Exchange Notifier"),
    to=[mt.Address(email="samiturk8@gmail.com")],
    subject="Test",
    text="Price is x",
)

# create client and send
client = mt.MailtrapClient(token="8b67ab369bd1f5529245fcacdb42e6b7")
client.send(mail)