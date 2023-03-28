import base64
from pathlib import Path
import mailtrap as mt
import renderer
import json

def send_email(addr, name, ctime, latest, final_change, last_date, last_time):
  welcome_image = Path(__file__).parent.joinpath("welcome.png").read_bytes()
  mail = mt.Mail(
    sender=mt.Address(email="me@sturk.au", name="Foreign Exchange Notifier"),
    to=[mt.Address(email=addr, name=name)],
    subject="Foreign Exchange Notifier",
    text="Daily Alert",
    html=str(open("output.html", "r").read()),
    category="Test",
    headers={"X-MT-Header": "Custom header"},
    custom_variables={"year": 2023},
  )
  client = mt.MailtrapClient(token=json.loads(open("token.json", "r").read()))
  client.send(mail)

